import base64
import os
import tempfile
from html2image import Html2Image


def html_to_base64(code):
    """
    Converts HTML code to a base64 encoded PNG image.

    Args:
        code (str): HTML code to be converted.

    Returns:
        str: Base64 encoded string of the image.
    """
    hti = Html2Image()

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        # Generate the screenshot and save to the temporary file
        hti.screenshot(html_str=code, save_as=tmp_file.name, size=(1280, 720))

        # Read the temporary file and encode it to base64
        try:
            with open(tmp_file.name, "rb") as image_file:
                screenshot_base64 = base64.b64encode(image_file.read()).decode('utf-8')
        finally:
            # Ensure the temporary file is removed
            os.remove(tmp_file.name)

    return screenshot_base64
