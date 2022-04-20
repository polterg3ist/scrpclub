import requests
from bs4 import BeautifulSoup


def parse(url, req="anime"):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    if req == "anime":
        return soup.find_all('article')
    return soup.find("div", class_="b-text_with_paragraphs")


def main():
    anime_top = {}
    last_place = 0
    for page in range(5):
        url = f'https://shikimori.one/animes/page/{page}'
        animes = parse(url)
        for anime in animes:
            last_place += 1
            title = anime.find('span', class_="name-ru").text
            info = anime.find('span', class_="misc").text
            year = info[0:4]
            type = info[4::]
            link = anime.find('a')
            # Code below check if description exist
            if link:
                link = link.get('href')
                desc = parse(link, "description")
                if desc:
                    desc = desc.text
                else:
                    desc = "No description"
            else:
                desc = "No description"
            anime_top[last_place] = {'title': title, 'year': year, 'type': type, 'desc': desc, 'link': link}

    for place in anime_top:
        anime = anime_top[place]
        print(f"Place: {place}\nTitle: {anime['title']}\nYear: {anime['year']}")
        print(f"Type: {anime['type']}\nDescription: {anime['desc']}\nLink: {anime['link']}\n")


if __name__ == '__main__':
    main()
