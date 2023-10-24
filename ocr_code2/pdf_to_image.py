import os
import sys
from pdf2image import convert_from_path

def pdf_to_images(pdf_file, output_dir):
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Convert the PDF to images
        images = convert_from_path(pdf_file)

        for i, image in enumerate(images):
            # Save each image to the output directory
            image_filename = os.path.join(output_dir, f"page_{i + 1}.jpg")
            image.save(image_filename, "JPEG")
        
        print(f"PDF pages converted to images and saved in '{output_dir}'")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_image.py input.pdf output_directory")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_directory = sys.argv[2]

    pdf_to_images(input_pdf, output_directory)
