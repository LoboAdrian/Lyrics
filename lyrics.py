from bs4 import BeautifulSoup
import requests

artist = str(input("Artist: "))
song = str(input("Song: "))

hyphensong = song.strip().replace(" ", "-")

print(artist.capitalize())
print(hyphensong)


URL = 'https://genius.com/' + artist.capitalize() + '-' + hyphensong + '-lyrics'


headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

mydivs = soup.findAll("div", {"class": "lyrics"})

for div in mydivs: 
        print(div.text)
