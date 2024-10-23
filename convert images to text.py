from PIL import Image
import pytesseract
import os


# Configure tesseract executable path (required for Windows users)
# For Windows, uncomment the line below and set the path to your Tesseract executable

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(img)

    return text


# Example usage
image_folder = "extracted_images_v2"  # The folder where images are saved
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]

# Process each image and extract text
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    extracted_text = image_to_text(image_path)

    print(f"Text from {image_file}:")
    print(extracted_text)
    print("-" * 40)
