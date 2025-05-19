import products.repositories.keyword as keyword_repo


def get_all():
    """
    Get all categories.
    """
    return keyword_repo.get_all()

def create(data):
    """
    Create a new category.
    """
    return keyword_repo.create(data)

def get(pk):
    """
    Get a specific category.
    """
    return keyword_repo.get(pk)

def update(pk, data):
    """
    Update a category.
    """
    return keyword_repo.update(pk, data)

def delete(pk):
    """
    Delete a category.
    """
    keyword_repo.delete(pk)
