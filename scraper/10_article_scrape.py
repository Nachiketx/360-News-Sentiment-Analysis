import newspaper
from textblob import TextBlob

keyword = input("Enter a keyword to search for news articles: ")

news_url = "https://timesofindia.indiatimes.com/"

news_source = newspaper.build(news_url, memoize_articles=False)

matching_articles = []
max_articles = 10  

for article in news_source.articles:
    try:
        article.download()
        article.parse()

        title = article.title
        publication_date = article.publish_date

        article.nlp()
        content_summary = article.summary

        if keyword.lower() in title.lower() or keyword.lower() in content_summary.lower():
            blob = TextBlob(content_summary)
            sentiment_score = blob.sentiment.polarity

            if sentiment_score > 0:
                sentiment_label = "Positive"
            elif sentiment_score < 0:
                sentiment_label = "Negative"
            else:
                sentiment_label = "Neutral"

            article_data = {
                "Title": title,
                "Publication Date": publication_date,
                "Content Summary": content_summary,
                "Sentiment Label": sentiment_label,
                "Sentiment Score": sentiment_score,
            }

            matching_articles.append(article_data)

            # Stop after collecting 10 articles
            if len(matching_articles) >= max_articles:
                break

    except Exception as e:
        print(f"Error processing article: {str(e)}")

if matching_articles:
    print(f"Top {max_articles} articles related to '{keyword}':")
    for i, article_data in enumerate(matching_articles, start=1):
        print(f"Article {i} - Title: {article_data['Title']}")
        print(f"Publication Date: {article_data['Publication Date']}")
        print(f"Sentiment: {article_data['Sentiment Label']} ({article_data['Sentiment Score']:.2f})")
        print("-" * 50)
else:
    print(f"No articles related to '{keyword}' found.")