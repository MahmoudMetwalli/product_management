import os
import json
from django.core.cache import cache
import products.repositories.product as product_repo


def get_all():
    """
    Get all categories.
    """
    return product_repo.get_all()

def create(data):
    """
    Create a new category.
    """
    return product_repo.create(data)

def get(pk):
    """
    Get a specific category.
    """
    return product_repo.get(pk)

def update(pk, data):
    """
    Update a category.
    """
    return product_repo.update(pk, data)

def delete(pk):
    """
    Delete a category.
    """
    product_repo.delete(pk)

def search_products_by_word(words: list[str], page=1, page_size=20, similarity_threshold=0.3):
    """Search products by a single word, including fuzzy matching on related brands and keywords."""
    # Input validation
    if not words or not any(len(word.strip()) >= 2 for word in words):
        return []

    # Normalize words
    words = [word.strip()[:100] for word in words if word.strip()]
    # Check cache
    query_key = ':'.join(sorted(word.lower() for word in words)) + f':{page}'
    cache_key = f"search:{query_key}:{page_size}:{similarity_threshold}"
    cached_results = cache.get(cache_key)
    if cached_results:
        return json.loads(cached_results)

    results = product_repo.search_products_by_word(words, page, page_size, similarity_threshold)

    # Cache results
    if results:
        cache.set(cache_key, json.dumps(results), int(os.environ.get('CACHE_TIMEOUT', 60 * 15)))

    return results
