from products.models import Brand
from products.serializers import BrandSerializer
from django.db import transaction
from django.http import Http404
from django.core.exceptions import ValidationError


def get_all():
    """
    Get all categories.
    """
    categories = Brand.objects.all()
    serializer = BrandSerializer(categories, many=True)
    data = serializer.data
    return data

def create(data):
    """
    Create a new category.
    """
    serializer = BrandSerializer(data=data)
    if serializer.is_valid():
        with transaction.atomic():
            serializer.save()
            data = serializer.data
            return data
    else:
        raise ValidationError(f"Invalid data {serializer.errors}")

def get(pk):
    """
    Get a specific category.
    """
    category = Brand.objects.prefetch_related('products').get(pk=pk)
    serializer = BrandSerializer(category)
    data = serializer.data
    return data

def update(pk, data):
    """
    Update a category.
    """
    with transaction.atomic():
        try:
            category = Brand.objects.get(pk=pk)
            serializer = BrandSerializer(category, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return data
            else:
                raise ValidationError(f"Invalid data {serializer.errors}")
        except Brand.DoesNotExist:
            raise Http404(f"Category not found with id: {pk}")
        except Exception as e:
            raise ValidationError(f"An error occurred: {str(e)}")

def delete(pk):
    """
    Delete a category.
    """
    with transaction.atomic():
        try:
            category = Brand.objects.get(pk=pk)
            category.delete()
            return None
        except Brand.DoesNotExist:
            raise Http404(f"Category not found with id: {pk}")
