import requests
import xml.etree.ElementTree as ET
from bot.models import NewsArticle
from bot.config import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD
import praw

def get_gamestop_news():

    gme_news_url = "https://gamestop.gcs-web.com/rss/news-releases.xml"

    news = requests.get(gme_news_url, timeout=10000)

    parsed_news = ET.fromstring(news.text)

    return parsed_news

def check_update(news=get_gamestop_news()):

    old_news_articles = [x.publication_date_and_time for x in NewsArticle.query()]

    # print(old_news_articles)

    # The root tag is "rss", it's only 1 tag so I just used news[0] to get the 

    for article in news[0].findall("item"):

        title = article.find("title").text
        description = article.find("description").text
        publication_date = article.find("pubDate").text
        link = article.find("link").text

        # print(title)
        # print(description)

        if publication_date in old_news_articles:
            print("This article is stored already.")
        
        else:
            new_article = NewsArticle.create(
                title=title,
                description=description,
                publication_date_and_time=publication_date,
                link = link
            )

            post_to_superstonk(new_article)

            print("This News Article would be posted to r/Superstonk.")

            # break

def post_to_superstonk(article):

    print("Submitting article...")

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=f"<Console:GME News Bot:(0.0.1) (by u/{USERNAME})>",
        username=USERNAME,
        password=PASSWORD
    )

    subreddit = reddit.subreddit("testingground4bots")

    subreddit.submit(title=article.title, url=article.link)

    print("Article submitted.")
    # print("hello world")
    # print(article)
