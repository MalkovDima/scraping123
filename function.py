from pprint import pprint
import bs4
import requests
from fake_headers import Headers
headers = Headers(os="mac", headers=True).generate()
url_original = 'https://habr.com'


def all_article(url):
    responce = requests.get(url, headers=headers)
    text = responce.text
    soup2 = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup2.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    pprint(articles[0].text)


def datatime_title_text(url, keywords):
    response = requests.get(url, headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all("article")
    for ar in articles:
        text = ar.find_all(class_="tm-article-body tm-article-snippet__lead")
        end = 0
        for search in keywords:

            if search.lower() in text[0].text.lower():
                datatime = ar.find_all(class_="tm-article-snippet__datetime-published")
                nametitle = ar.find_all(class_="tm-article-snippet__title-link")
                readmore = ar.find_all(class_="tm-article-snippet__readmore")
                urlarticle = url_original + readmore[0].attrs['href']
                print(datatime[0].contents[0].attrs['title'])
                print(nametitle[0].contents[0].text)
                print(urlarticle)
                print('++++++')
                all_article(urlarticle)
                print('++++++')
                end = 1
            if end == 1:
                break
