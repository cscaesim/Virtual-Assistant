import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def get_news():
    news_url = "https://news.google.com/news/rss"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    # lxml because macos wants to be picky for some reason.
    soup_page = soup(xml_page, "lxml")
    news_list = soup_page.findAll("item")

    print("The news for today, from Google News: \n")

    for news in news_list:
        print(news.title.text)
        print(" \n Next up \n")

    print("That was the news for today.")