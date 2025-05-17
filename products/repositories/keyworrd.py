from products.models import Keyword
from products.serializers import KeywordSerializer
from django.db import transaction
from django.http import Http404
from django.core.exceptions import ValidationError


def get_all():
    """
    Get all categories.
    """
    categories = Keyword.objects.all()
    serializer = KeywordSerializer(categories, many=True)
    data = serializer.data
    return data

def create(data):
    """
    Create a new category.
    """
    serializer = KeywordSerializer(data=data)
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
    category = Keyword.objects.prefetch_related('products').get(pk=pk)
    serializer = KeywordSerializer(category)
    data = serializer.data
    return data

def update(pk, data):
    """
    Update a category.
    """
    with transaction.atomic():
        try:
            category = Keyword.objects.get(pk=pk)
            serializer = KeywordSerializer(category, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return data
            else:
                raise ValidationError(f"Invalid data {serializer.errors}")
        except Keyword.DoesNotExist:
            raise Http404(f"Category not found with id: {pk}")
        except Exception as e:
            raise ValidationError(f"An error occurred: {str(e)}")

def delete(pk):
    """
    Delete a category.
    """
    with transaction.atomic():
        try:
            category = Keyword.objects.get(pk=pk)
            category.delete()
            return None
        except Keyword.DoesNotExist:
            raise Http404(f"Category not found with id: {pk}")
