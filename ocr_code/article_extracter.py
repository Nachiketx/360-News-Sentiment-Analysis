import fitz  # PyMuPDF
import re

def extract_articles_from_pdf(pdf_path):
    articles = []
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Get the number of pages in the PDF
    num_pages = len(pdf_document)
    
    # Loop through each page
    for page_number in range(num_pages):
        page = pdf_document.load_page(page_number)
        
        # Extract text from the page
        page_text = page.get_text()
        
        # Define patterns to capture metadata and article content
        metadata_pattern = r"Newspaper: (.+)\nPage: (\d+)\nEdition: (.+)\nAuthor: (.+)\n"
        
        # Find metadata matches on the page
        metadata_match = re.search(metadata_pattern, page_text)
        
        if metadata_match:
            # Extract metadata from the match
            newspaper_name, page_num, edition_name, author_name = metadata_match.groups()
            
            # Remove the metadata from the page text
            article_text = re.sub(metadata_pattern, '', page_text)
            
            # Create an article dictionary with metadata
            article = {
                "Newspaper": newspaper_name.strip(),
                "Page": int(page_num.strip()),
                "Edition": edition_name.strip(),
                "Author": author_name.strip(),
                "Content": article_text.strip(),
            }
            
            articles.append(article)
    
    # Close the PDF document
    pdf_document.close()
    
    return articles

# Example usage
pdf_path = 'D:\\Nachiket\\Smart India Hackathon 2023\\test_ocr_images_and_pdf\\split IE HD Delhi 23~09~2023.pdf'
extracted_articles = extract_articles_from_pdf(pdf_path)

# Print the extracted articles with metadata
for article in extracted_articles:
    print(f"Newspaper: {article['Newspaper']}")
    print(f"Page: {article['Page']}")
    print(f"Edition: {article['Edition']}")
    print(f"Author: {article['Author']}")
    print(f"Content: {article['Content']}")
    print("=" * 50)
