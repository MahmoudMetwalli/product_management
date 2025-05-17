import re

def is_arabic(word):
    """Determine if a word is primarily Arabic based on its characters."""
    arabic_pattern = re.compile(r'[\u0600-\u06FF]')
    # Check if the word contains Arabic characters
    return bool(arabic_pattern.search(word))
