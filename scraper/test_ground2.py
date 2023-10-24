import newspaper
from textblob import TextBlob

# Define the URL of the news website you want to scrape
news_url = "https://timesofindia.indiatimes.com/"

# Initialize the newspaper source and build the article list
news_source = newspaper.build(news_url, memoize_articles=False)

# Define lists to store article details
articles_data = []

# Iterate through the articles and analyze sentiment
for article in news_source.articles[:10]:  # Extract the top 10 articles
    try:
        # Download and parse the article content
        article.download()
        article.parse()

        # Get article metadata
        title = article.title
        publication_date = article.publish_date
        author = article.authors[0] if article.authors else None
        
        # Get a summary of the article content
        article.nlp()
        content_summary = article.summary

        # Perform sentiment analysis using TextBlob on the content summary
        blob = TextBlob(content_summary)
        sentiment_score = blob.sentiment.polarity

        # Determine sentiment label based on the score
        if sentiment_score > 0:
            sentiment_label = "Positive"
        elif sentiment_score < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        # Store article data in a dictionary
        article_data = {
            "Title": title,
            "Publication Date": publication_date,
            "Author": author,
            "Content Summary": content_summary,
            "Sentiment Label": sentiment_label,
            "Sentiment Score": sentiment_score,
        }

        # Append article data to the list
        articles_data.append(article_data)

    except Exception as error:
        print("Error")

# Display and save the extracted data
for i, article_data in enumerate(articles_data, start=1):
    print(f"Article Number {i} - Title: {article_data['Title']}")
    print(f"Publication Date: {article_data['Publication Date']}")
    print(f"Author: {article_data['Author']}")
#    print(f"Content Summary: {article_data['Content Summary']}")
    print(f"Sentiment: {article_data['Sentiment Label']} ({article_data['Sentiment Score']:.2f})")
    print("-" * 50)

# You can save the articles_data list to a CSV file or a database if needed
