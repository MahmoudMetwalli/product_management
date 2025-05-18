import uuid
from django.db import models, transaction
from django.core.exceptions import ValidationError


class TransliterationMixin:
    def generate_transliteration(self):
        """Generate transliteration from Arabic name"""
        source_text = getattr(self, 'arabic_name', '') or ""
        if not source_text:
            return ""
        return self._arabic_to_latin(source_text)
    
    def generate_reverse_transliteration(self):
        """Generate Arabic transliteration from English name"""
        source_text = getattr(self, 'english_name', '') or ""
        if not source_text:
            return ""
        return self._latin_to_arabic(source_text)
    
    def _arabic_to_latin(self, text):
        """Arabic to Latin transliteration"""
        ARABIC_MAP = {
            'ا': 'a', 'أ': 'a', 'إ': 'e', 'آ': 'aa',
            'ب': 'b', 'ت': 't', 'ث': 'th',
            'ج': 'j', 'ح': 'h', 'خ': 'kh',
            'د': 'd', 'ذ': 'th', 'ر': 'r',
            'ز': 'z', 'س': 's', 'ش': 'sh',
            'ص': 's', 'ض': 'd', 'ط': 't',
            'ظ': 'z', 'ع': 'aa', 'غ': 'gh',
            'ف': 'f', 'ق': 'k', 'ك': 'k',
            'ل': 'l', 'م': 'm', 'ن': 'n',
            'ه': 'h', 'و': 'w', 'ي': 'y',
            'ة': 'a', 'ى': 'a', 'ء': "'",
        }
        result = ""
        for char in text:
            result += ARABIC_MAP.get(char, char) or char
        return result
    
    def _latin_to_arabic(self, text):
        """Latin to Arabic transliteration"""
        LATIN_TO_ARABIC = {
            'a': 'ا', 'b': 'ب', 't': 'ت', 'th': 'ث',
            'j': 'ج', 'h': 'ه', 'kh': 'خ', 'k': 'ك',
            'd': 'د', 'dh': 'ذ', 'r': 'ر', 'z': 'ز',
            's': 'س', 'sh': 'ش', 'ss': 'ص', 'dd': 'ض',
            'tt': 'ط', 'zz': 'ظ', 'aa': 'ع', 'gh': 'غ',
            'f': 'ف', 'q': 'ق', 'l': 'ل', 'm': 'م',
            'n': 'ن', 'w': 'و', 'y': 'ي', "'": 'ء',
            'e': 'ي', 'i': 'ي', 'o': 'و', 'u': 'و', 'sc': 'س',
            'ch': 'ش', 'ou': 'و', 'ae': 'ا', 'au': 'ا',
            'c': 'ك', 'x': 'كس', 'z': 'ز', 'p': 'ب', 'v': 'ف',
            'g': 'ج', 'q': 'ق', 'y': 'ي', ' ': ' ',
        }
        
        result = ""
        i = 0
        text = text.lower()
        
        while i < len(text):
            if i < len(text) - 1:
                two_chars = text[i:i+2]
                if two_chars in LATIN_TO_ARABIC:
                    result += LATIN_TO_ARABIC[two_chars]
                    i += 2
                    continue
            if text[i] in LATIN_TO_ARABIC:
                result += LATIN_TO_ARABIC[text[i]]
            elif text[i] == ' ':
                result += ' '
            i += 1
        
        return result


class BaseModelMixin(models.Model):
    """Base mixin providing common fields for all models."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.PositiveIntegerField(default=1)
    
    class Meta:
        abstract = True
        # Note: indexes and constraints need to be defined in the child classes
        # as index names must be unique across the entire database


class BaseNamedModelMixin(BaseModelMixin, TransliterationMixin):
    """Base mixin for models with Arabic/English names and transliterations."""
    arabic_name = models.CharField(max_length=200, db_index=True)
    english_name = models.CharField(max_length=200, db_index=True)
    name_translit = models.CharField(max_length=200, blank=True)
    arabic_translit = models.CharField(max_length=200, blank=True,
                                      help_text="English to Arabic transliteration")
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.english_name} / {self.arabic_name}"
    
    def save(self, *args, **kwargs):
        """Override save to generate transliterations and handle versioning atomically"""
        with transaction.atomic():
            # Lock the row if updating
            if self.pk is not None:
                try:
                    # Try to get the row with matching ID and version
                    self.__class__.objects.select_for_update().get(pk=self.pk, version=self.version)
                    # Increment version if the object exists
                    self.version = self.version + 1
                except self.__class__.DoesNotExist:
                    # Row doesn't exist with current version, check if it exists at all
                    try:
                        # This will succeed if the row exists but with a different version
                        existing_obj = self.__class__.objects.select_for_update().get(pk=self.pk)
                        # If we get here, the row exists with a different version
                        raise ValidationError(
                            f"Concurrency error: This record has been modified. "
                            f"Current version is {existing_obj.version}, but you have version {self.version}."
                        )
                    except self.__class__.DoesNotExist:
                        # Row doesn't exist at all, treat as new object
                        self.pk = None
                    
            self.name_translit = self.generate_transliteration()
            self.arabic_translit = self.generate_reverse_transliteration()
            super().save(*args, **kwargs)
