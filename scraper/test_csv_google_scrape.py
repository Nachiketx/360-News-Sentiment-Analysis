import csv
import requests
from bs4 import BeautifulSoup

# Function to scrape Google News URLs for a keyword
def scrape_google_news(keyword):
    base_url = f"https://news.google.com/search?q={keyword}&hl=en-US&gl=US&ceid=US%3Aen"
    
    # Send an HTTP GET request to Google News
    response = requests.get(base_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the article links
        article_links = []
        for link in soup.find_all('a', class_='VDXfz')[:10]:
            article_links.append(link['href'])
        
        return article_links
    else:
        print(f"Failed to fetch Google News for '{keyword}'")
        return []

# Read keywords from the CSV file
with open('keywords.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        keyword = row['Keyword']
        
        # Scrape Google News URLs for the keyword
        article_links = scrape_google_news(keyword)
        
        # Print the results
        print(f"Articles for '{keyword}':")
        for link in article_links:
            print(link)
        print("\n")
