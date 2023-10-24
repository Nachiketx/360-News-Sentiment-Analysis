
from newspaper import Article

def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()
    article.download('punkt')
    article.nlp()

    author_string = "Author(s): "
    for author in article.authors:
        author_string += author  
    print(author_string)

    
    date = article.publish_date

  
    print("Top Image Url: " + str(article.top_image))

    
    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image  
    print(image_string)
    print()

    
    print("The Original Article Text")
    print(article.text)
    print("----------------------------------------")
    print("A Quick Article Summary")
    print("----------------------------------------")
    print(article.summary)

   


summarize_article("https://www.ndtv.com/photos/news/justice-for-every-child-a-look-at-the-success-of-the-campaign-102363#photo-431928")