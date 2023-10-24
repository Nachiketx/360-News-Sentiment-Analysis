import newspaper
from textblob import TextBlob

# Define the URL of the news website you want to scrape
news_url = "https://timesofindia.indiatimes.com/"

# Initialize the newspaper source and build the article list
news_source = newspaper.build(news_url, memoize_articles=False)

# Define lists to store article titles, text, and sentiment scores
article_titles = []
article_texts = []
article_sentiments = []

# Iterate through the articles and analyze sentiment
for article in news_source.articles[:10]:  # Extract the top 10 articles
    try:
        # Download and parse the article content
        article.download()
        article.parse()

        # Get the article title and text
        title = article.title
        text = article.text

        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity

        # Determine sentiment label based on the score
        if sentiment_score > 0:
            sentiment_label = "Positive"
        elif sentiment_score < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        # Append article details, sentiment, and sentiment score to the lists
        article_titles.append(title)
        article_texts.append(text)
        article_sentiments.append((sentiment_label, sentiment_score))

        # Display article details and sentiment score
        print(f"Title: {title}")
        print(f"Sentiment: {sentiment_label}")
        print(f"Sentiment Score: {sentiment_score}")
        print("-" * 50)

    except Exception as e:
        print(f"Error processing article: {str(e)}")

# Save the extracted data to a CSV file, a database, or any desired storage method
