from django.db import transaction
from django.http import Http404
from django.core.exceptions import ValidationError
from django.db.models import Q, FloatField, ExpressionWrapper, F
from django.db.models.functions import Greatest
from products.models.product import Product
from products.serializers.product import ProductSerializer
from django.contrib.postgres.search import TrigramSimilarity
from products.utils.is_arabic import is_arabic

def get_all():
    """
    Get all categories.
    """
    categories = Product.objects.select_related('brand').prefetch_related('keywords').all()
    serializer = ProductSerializer(categories, many=True)
    data = serializer.data
    return data

def create(data):
    """
    Create a new category.
    """
    serializer = ProductSerializer(data=data)
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
    category = Product.objects.select_related('brand').prefetch_related('keywords').get(pk=pk)
    serializer = ProductSerializer(category)
    data = serializer.data
    return data

def update(pk, data):
    """
    Update a category.
    """
    with transaction.atomic():
        try:
            category = Product.objects.get(pk=pk)
            serializer = ProductSerializer(category, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return data
            else:
                raise ValidationError(f"Invalid data {serializer.errors}")
        except Product.DoesNotExist:
            raise Http404(f"Category not found with id: {pk}")
        except Exception as e:
            raise ValidationError(f"An error occurred: {str(e)}")

def delete(pk):
    """
    Delete a category.
    """
    with transaction.atomic():
        try:
            category = Product.objects.get(pk=pk)
            category.delete()
            return None
        except Product.DoesNotExist:
            raise Http404(f"Category not found with id: {pk}")

def search_products_by_word(words: list[str], page=1, page_size=20, similarity_threshold=0.3):
    """Search products by words, requiring ALL words to match (restrictive search)."""

    products = Product.objects.select_related('brand').prefetch_related('keywords')
    
    # Initialize empty list for storing similarity expressions for later sorting
    similarity_expressions = []
    
    # Start with an empty filter that matches everything
    combined_filter = Q()
    
    # First time through, we'll set the filter instead of AND-ing
    first_word = True

    # Process each word
    for i, word in enumerate(words):
        is_arabic_word = is_arabic(word)
        
        # Define annotation names with unique index to avoid conflicts
        name_sim_field = f'name_sim_{i}'
        translit_sim_field = f'translit_sim_{i}'
        brand_name_sim_field = f'brand_name_sim_{i}'
        brand_translit_sim_field = f'brand_translit_sim_{i}'
        keyword_name_sim_field = f'keyword_name_sim_{i}'
        keyword_translit_sim_field = f'keyword_translit_sim_{i}'
        
        # Create annotations dict to apply to queryset
        annotations = {}
        
        if is_arabic_word:
            # Add Arabic annotations
            annotations[name_sim_field] = TrigramSimilarity('arabic_name', word)
            annotations[translit_sim_field] = TrigramSimilarity('arabic_translit', word)
            annotations[brand_name_sim_field] = TrigramSimilarity('brand__arabic_name', word)
            annotations[brand_translit_sim_field] = TrigramSimilarity('brand__arabic_translit', word)
            annotations[keyword_name_sim_field] = TrigramSimilarity('keywords__arabic_name', word)
            annotations[keyword_translit_sim_field] = TrigramSimilarity('keywords__arabic_translit', word)
        else:
            # Add English annotations
            annotations[name_sim_field] = TrigramSimilarity('english_name', word)
            annotations[translit_sim_field] = TrigramSimilarity('name_translit', word)
            annotations[brand_name_sim_field] = TrigramSimilarity('brand__english_name', word)
            annotations[brand_translit_sim_field] = TrigramSimilarity('brand__name_translit', word)
            annotations[keyword_name_sim_field] = TrigramSimilarity('keywords__english_name', word)
            annotations[keyword_translit_sim_field] = TrigramSimilarity('keywords__name_translit', word)
        
        # Apply annotations to queryset
        products = products.annotate(**annotations)
        
        # Build filter for this word
        word_filter = (
            Q(**{f'{name_sim_field}__gt': similarity_threshold}) |
            Q(**{f'{translit_sim_field}__gt': similarity_threshold}) |
            Q(**{f'{brand_name_sim_field}__gt': similarity_threshold}) |
            Q(**{f'{brand_translit_sim_field}__gt': similarity_threshold}) |
            Q(**{f'{keyword_name_sim_field}__gt': similarity_threshold}) |
            Q(**{f'{keyword_translit_sim_field}__gt': similarity_threshold}) |
            Q(nutrition_facts__has_key=word)
        )
        
        if first_word:
            combined_filter = word_filter
            first_word = False
        else:
            combined_filter &= word_filter 
        
        # Create maximum similarity expression for this word
        max_sim = Greatest(
            F(name_sim_field), 
            F(translit_sim_field), 
            F(brand_name_sim_field), 
            F(brand_translit_sim_field), 
            F(keyword_name_sim_field), 
            F(keyword_translit_sim_field), 
            output_field=FloatField()
        )
        
        # Add to expressions list for later sorting
        similarity_expressions.append(max_sim)
    
    # Apply filter to get matching products only
    products = products.filter(combined_filter)
    
    # Combine similarities for sorting (if we have any)
    if similarity_expressions:
        if len(similarity_expressions) == 1:
            # Just one word, use its max similarity directly
            total_sim = similarity_expressions[0]
        else:
            # Multiple words, add all similarities together
            total_sim = similarity_expressions[0]
            for expr in similarity_expressions[1:]:
                total_sim = total_sim + expr
                
        # Add the combined similarity score
        products = products.annotate(
            total_sim=ExpressionWrapper(total_sim, output_field=FloatField())
        )
        order_by = ['-total_sim']
    else:
        order_by = ['english_name']  # Fallback sorting

    # Apply distinct to remove duplicates
    products = products.distinct()
    
    # Paginate
    start = (page - 1) * page_size
    end = start + page_size
    products = products.order_by(*order_by)[start:end]

    # Serialize results
    serializer = ProductSerializer(products, many=True)
    results = serializer.data

    return results
