from products.models.brand import Brand
from products.models.keyword import Keyword
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from products.models.base_models import BaseNamedModelMixin

class Product(BaseNamedModelMixin):
    # Only need to define what's unique to Product
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    keywords = models.ManyToManyField(Keyword, related_name='products', blank=True)
    nutrition_facts = models.JSONField(default=dict, blank=True)
    
    class Meta:
        indexes = [
            GinIndex(fields=['arabic_name'], name='prod_arabic_name_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['english_name'], name='prod_english_name_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['name_translit'], name='prod_name_translit_gin_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['arabic_translit'], name='prod_arabic_translit_gin_idx', opclasses=['gin_trgm_ops']),
            models.Index(fields=['version'], name='prod_version_idx'),
        ]
