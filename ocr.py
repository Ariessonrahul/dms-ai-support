import easyocr
from PIL import Image
import numpy as np
 
# OCR reader (English by default)
reader = easyocr.Reader(['en'], gpu=False)
 
 
def extract_text(image_file):
    """
    Extract text from uploaded image.
 
    Parameters:
        image_file: Uploaded image file from Streamlit.
 
    Returns:
        str: Extracted text.
    """
    try:
        image = Image.open(image_file).convert("RGB")
        image_np = np.array(image)
 
        results = reader.readtext(image_np, detail=0)
 
        text = "\n".join(results)
 
        return text.strip()
 
    except Exception as e:
        return f"OCR Error: {str(e)}"
 
 
def extract_lines(image_file):
    """
    Return OCR output as a list of lines.
    """
    text = extract_text(image_file)
 
    if text.startswith("OCR Error:"):
        return []
 
    return [line.strip() for line in text.split("\n") if line.strip()]
