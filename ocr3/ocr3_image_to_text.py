import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def scan_images_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]

        if not image_files:
            print("No image files found in the folder.")
            return

        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            image = Image.open(image_path)

            result = pytesseract.image_to_string(image, lang='mar')  # lang code ithe taaka
            #lang_out = (lang)
            print(f" Detected Languages: {result}")
            print(result)
            print("=" * 50)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\Khairkar\\Desktop\\Literature"
    
    scan_images_in_folder(folder_path)
