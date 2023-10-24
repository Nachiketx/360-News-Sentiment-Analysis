import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    path_to_poppler_exe = Path(r"C:\Program Files\poppler-23.08.0\Library\bin")
    out_directory = Path(r"D:\Nachiket\Smart India Hackathon 2023\test file output").expanduser()
else:
    out_directory = Path("~\Desktop").expanduser()

PDF_file = Path(r"D:\Nachiket\Smart India Hackathon 2023\test file input\d.pdf")

def extract_text_from_newspaper(pdf_path, output_dir):
    with TemporaryDirectory() as tempdir:
        if platform.system() == "Windows":
            pdf_pages = convert_from_path(pdf_path, 500, poppler_path=path_to_poppler_exe)
        else:
            pdf_pages = convert_from_path(pdf_path, 500)
        
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")

            text = str(((pytesseract.image_to_string(Image.open(filename)))))
            text = text.replace("-\n", "")
        
            print(f"Extracted text from page {page_enumeration}:\n{text}\n")

if __name__ == "__main__":
    extract_text_from_newspaper(PDF_file, out_directory)
