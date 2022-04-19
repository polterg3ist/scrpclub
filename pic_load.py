import requests
from random import randint,choice
from bs4 import BeautifulSoup



def parse(url):
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    text = soup.find_all('div', class_= "col-lg-4 col-md-6 mb-4")
    return text


def main():
    clothes_and_price = {}
    for page in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'
        info = parse(url)

        for card in info:
            orig = card
            card = card.text
            if '$' in card:
                title, price = list(filter(lambda x: x, card.split('\n')))
                id = "ID_" + "".join([choice("abcdefghijklmnopqrstuvwxyz")+str(randint(0, 9)) for _ in range(3)])
                link = orig.find('a').get('href')
                clothes_and_price[id] = {"title": title, "price": price, "link": link}
    for id in clothes_and_price:
        print(f"Product ID --{id}\nTitle --{clothes_and_price[id]['title']}\nPrice -- {clothes_and_price[id]['price']}\nLink -- {clothes_and_price[id]['link']}\n")


if __name__ == '__main__':
    main() 