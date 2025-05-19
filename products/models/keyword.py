from django.contrib.postgres.indexes import GinIndex
from django.db import models
from products.models.base_models import BaseNamedModelMixin

class Keyword(BaseNamedModelMixin):
    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"
        ordering = ['english_name']
        indexes = [
            GinIndex(fields=['arabic_name'], name='ky_arabic_name_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['english_name'], name='ky_english_name_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['name_translit'], name='ky_translit_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['arabic_translit'], name='ky_arabic_translit_gin_idx', opclasses=['gin_trgm_ops']),
            models.Index(fields=['version'], name='ky_version_idx'),
        ]