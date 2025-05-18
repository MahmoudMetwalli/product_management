from django.contrib.postgres.indexes import GinIndex
from django.db import models
from products.models.base_models import BaseNamedModelMixin


class Brand(BaseNamedModelMixin):
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ['english_name']
        indexes = [
            GinIndex(fields=['arabic_name'], name='br_arabic_name_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['english_name'], name='br_english_name_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['name_translit'], name='br_translit_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['arabic_translit'], name='br_arabic_translit_gin_idx', opclasses=['gin_trgm_ops']),
            models.Index(fields=['version'], name='br_version_idx'),
        ]
