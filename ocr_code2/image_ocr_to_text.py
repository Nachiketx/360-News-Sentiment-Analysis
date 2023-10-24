import os
import sys
import pytesseract
from PIL import Image

def image_ocr_to_text(input_dir, output_text_file):
    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_text_file), exist_ok=True)

        with open(output_text_file, "w", encoding="utf-8") as text_file:
            for root, _, files in os.walk(input_dir):
                for file in files:
                    if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
                        image_path = os.path.join(root, file)
                        text = perform_ocr(image_path)
                        text_file.write(f"Text from {image_path}:\n")
                        text_file.write(text + "\n\n")
        
        print(f"OCR results saved in '{output_text_file}'")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def perform_ocr(image_path):
    try:
        # Open the image using PIL (Pillow)
        image = Image.open(image_path)

        # Perform OCR using pytesseract with auto language detection
        text = pytesseract.image_to_string(image, lang="auto")

        return text.strip()

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_ocr_to_text.py input_images_directory output_text_file.txt")
        sys.exit(1)

    input_images_dir = sys.argv[1]
    output_text_file = sys.argv[2]

    image_ocr_to_text(input_images_dir, output_text_file)
