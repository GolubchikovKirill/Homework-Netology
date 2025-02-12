"""
TASK-3
"""

import os
import requests
from bs4 import BeautifulSoup
from Homework.logger_2 import logger

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/articles/'

LOG_PATH = os.path.join(os.path.dirname(__file__), 'scraping.log')


@logger(LOG_PATH)
def scrapping():
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        title_link = article.find('h2').find('a')
        if not title_link:
            continue

        title = title_link.text.strip()
        relative_link = title_link.get('href', '')
        full_link = f'https://habr.com{relative_link}' if relative_link.startswith('/ru/articles/') else relative_link

        time_tag = article.find('time')
        pub_date = time_tag.get('datetime')[:10] if time_tag else 'Нет даты'

        preview = article.find(class_='tm-article-snippet')
        preview_text = preview.text.strip() if preview else ''

        hubs = article.find_all(class_='tm-article-snippet__hubs-item')
        hubs_text = ' '.join(hub.text.strip() for hub in hubs)

        text_to_check = f'{title} {preview_text} {hubs_text}'.lower()

        if any(keyword in text_to_check for keyword in KEYWORDS):
            print(f'{pub_date} – {title} – {full_link}')


if __name__ == '__main__':
    scrapping()