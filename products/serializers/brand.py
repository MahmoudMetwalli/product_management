from adrf.serializers import ModelSerializer
from products.models.brand import Brand


class BrandSerializer(ModelSerializer):
    """
    Serializer for Brand model
    """
    class Meta:
        model = Brand
        fields = ('id', 'arabic_name', 'english_name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'arabic_name': {'required': True},
            'english_name': {'required': True}
        }
