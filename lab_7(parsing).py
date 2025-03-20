import requests
from bs4 import BeautifulSoup

url = 'https://lenta.ru/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Ошибка: {response.status_code}")
else:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    news_items = soup.find_all('a', class_='card-mini _topnews')

    if not news_items:
        print("Новости не найдены. Возможно, изменилась структура сайта.")
    else:
        for item in news_items:
            title = item.text.strip()
            link = item['href']
            if not link.startswith('http'):
                link = 'https://lenta.ru' + link
            print(f'Заголовок: {title}\nСсылка: {link}\n')
