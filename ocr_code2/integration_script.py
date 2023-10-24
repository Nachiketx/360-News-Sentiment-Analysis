import subprocess

# Step 1: Call the first script to convert PDF to images
pdf_to_image_script = "D:\\Nachiket\\Smart India Hackathon 2023\\ocr_code2\\pdf_to_image.py"
pdf_file = "D:\\Nachiket\\Smart India Hackathon 2023\\test file input\\d.pdf"  # Replace with your input PDF file
output_images_dir = "D:\\Nachiket\\Smart India Hackathon 2023\\ocr_code2\\image_output"  # Directory to store the converted images

# Execute the first script
conversion_command = ["python", pdf_to_image_script, pdf_file, output_images_dir]
subprocess.run(conversion_command)

# Step 2: Call the second script to perform OCR on the images
image_ocr_script = "D:\\Nachiket\\Smart India Hackathon 2023\\ocr_code2\\image_ocr_to_text.py"
output_text_file = "D:\\Nachiket\\Smart India Hackathon 2023\\ocr_code2\\text output\\output_text.txt"  # File to store the OCR results

# Execute the second script
ocr_command = ["python", image_ocr_script, output_images_dir, output_text_file]
subprocess.run(ocr_command)

print("PDF to Text conversion complete!")
