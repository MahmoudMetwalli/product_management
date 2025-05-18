import products.repositories.brand as brand_repo

def get_all():
    """
    Get all categories.
    """
    return brand_repo.get_all()

def create(data):
    """
    Create a new category.
    """
    return brand_repo.create(data)

def get(pk):
    """
    Get a specific category.
    """
    return brand_repo.get(pk)

def update(pk, data):
    """
    Update a category.
    """
    return brand_repo.update(pk, data)

def delete(pk):
    """
    Delete a category.
    """
    brand_repo.delete(pk)
