import os
import re

def find_image_path(text):
    """
    Find the longest existing image file path in the provided text.

    Args:
        text (str): The text to search for image paths.

    Returns:
        str or None: The longest existing image path if found, otherwise None.
    """
    # Pattern to match file paths with image extensions
    pattern = r"[A-Za-z]:\\[^:\n]+?\.(?:jpe?g|png)|/[^:\n]+?\.(?:jpe?g|png)"
    matches = re.finditer(pattern, text, re.IGNORECASE)

    # Filter out non-existing paths and return the longest one
    existing_paths = [match.group() for match in matches if os.path.exists(match.group())]
    return max(existing_paths, key=len, default=None)

