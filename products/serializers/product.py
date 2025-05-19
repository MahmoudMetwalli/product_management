from adrf.serializers import ModelSerializer
from rest_framework import serializers
from products.models.product import Product
from products.models.brand import Brand
from products.models.keyword import Keyword
from products.serializers.brand import BrandSerializer
from products.serializers.keyword import KeywordSerializer
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Product Example',
            value={
                "arabic_name": "منتج",
                "english_name": "Product",
                "nutrition_facts": {
                    "calories": 200,
                    "fat": "10g",
                    "protein": "5g"
                },
                "brand_id": "uuid-here",
                "keyword_ids": ["uuid-here"],
            },
            request_only=True
        ),
        OpenApiExample(
            'Product Response Example',
            value={
                "id": "uuid-here",
                "arabic_name": "منتج",
                "english_name": "Product",
                "nutrition_facts": {
                    "calories": 200,
                    "fat": "10g",
                    "protein": "5g"
                },
                "brand": {
                    "id": "uuid-here",
                    "arabic_name": "علامة تجارية",
                    "english_name": "Brand"
                },
                "keywords": [
                    {
                        "id": "uuid-here",
                        "arabic_name": "كلمة مفتاحية",
                        "english_name": "Keyword"
                    }
                ],
                "created_at": "2023-10-01T00:00:00Z",
                "updated_at": "2023-10-01T00:00:00Z",
            },
            response_only=True
        )
    ]
)
class ProductSerializer(ModelSerializer):
    brand_id = serializers.PrimaryKeyRelatedField(
        source='brand',
        queryset=Brand.objects.all(),
        write_only=True
    )
    brand = BrandSerializer(read_only=True)

    keyword_ids = serializers.PrimaryKeyRelatedField(
        source='keywords',
        queryset=Keyword.objects.all(),
        many=True,
        write_only=True,
        required=False
    )
    keywords = KeywordSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'arabic_name', 'english_name',
            'nutrition_facts',
            'brand', 'brand_id',
            'keywords', 'keyword_ids',
            'created_at', 'updated_at'
        )
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'brand', 'keywords',
        )
