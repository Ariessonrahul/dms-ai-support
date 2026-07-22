from PIL import Image
import pytesseract
 
def extract_text(image):
    text = pytesseract.image_to_string(Image.open(image))
    return text.lower()

