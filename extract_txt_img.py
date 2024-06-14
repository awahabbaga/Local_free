import pytesseract
from PIL import Image

# Path to the uploaded image
image_path = 'IMG_1801.PNG'

def extract_schedule_from_image(image_path):
    """
    Extract text from an image using OCR and parse it to determine the schedule.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)  # No language specified
    return text

# Extract schedule information from the image
schedule_info = extract_schedule_from_image(image_path)
print(f"Extracted Schedule Information:\n{schedule_info}")
