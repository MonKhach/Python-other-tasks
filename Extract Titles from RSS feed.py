from urllib.request import urlopen
from bs4 import BeautifulSoup
google_news_url = "https://news.google.com/news/rss"
def get_headlines(rss_url):
    html_page = urlopen(rss_url)
    soup = BeautifulSoup(html_page, 'xml')
    titles = soup.find_all('title')
    headlines = [title.string for title in titles[1:]]

    return headlines
print(get_headlines(google_news_url))