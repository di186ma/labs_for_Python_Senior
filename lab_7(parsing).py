import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Ошибка: {response.status_code}")
else:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    if not books:
        print("Новости не найдены. Возможно, изменилась структура сайта.")
    else:
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            print(f'Заголовок: {title}\nЦена: {price}\n')
