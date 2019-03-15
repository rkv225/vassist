import requests
from bs4 import BeautifulSoup
import time
from utility import text_to_speech as tts

urls = {}
urls["finance"] = 'https://in.reuters.com/finance'
urls["business"] = 'https://in.reuters.com/finance'
urls["default"] = 'https://in.reuters.com/news/top-news'
urls["world"] = 'https://in.reuters.com/news/world'
urls["globe"] = 'https://in.reuters.com/news/world'
urls["global"] = 'https://in.reuters.com/news/world'
urls["tech"] = 'https://in.reuters.com/news/technology'
urls["sports"] = 'https://in.reuters.com/news/sports'

def tell_news(category):
    page = requests.get(urls[category])
    soup = BeautifulSoup(page.content, 'html.parser')
    headlines_list = soup.find_all('h3', class_='story-title')
    for headlines in headlines_list:
        tts.operation(headlines.get_text())
        time.sleep(1)