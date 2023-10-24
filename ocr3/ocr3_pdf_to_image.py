import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_to_images(pdf_path, output_folder, dpi=300):
 
    pdf_document = fitz.open(pdf_path)

    import os
    os.makedirs(output_folder, exist_ok=True)

    for page_number in range(pdf_document.page_count):
       
        page = pdf_document.load_page(page_number)

        
        image = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)

        output_image_path = os.path.join(output_folder, f"page_{page_number + 1}.png")

        pil_image.save(output_image_path, dpi=(dpi, dpi))

        print(f"Page {page_number + 1} saved as {output_image_path} at {dpi} DPI")

    pdf_document.close()

if __name__ == "__main__":
    
    pdf_file = 'D:\\Nachiket\\Smart India Hackathon 2023\\test file input\\split IE HD Delhi 23~09~2023.pdf'

    output_folder = 'D:\\Nachiket\\Smart India Hackathon 2023\\pdf file output'

    custom_dpi = 150  #  DPI

    convert_pdf_to_images(pdf_file, output_folder, dpi=custom_dpi)
