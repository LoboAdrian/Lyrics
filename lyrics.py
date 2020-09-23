from bs4 import BeautifulSoup
import requests

artist = str(input("Artist: "))
song = str(input("Song: "))

hyphenartist = artist.strip().replace(" ", "-")
hyphensong = song.strip().replace(" ", "-")

URL = 'https://genius.com/' + hyphenartist.capitalize() + '-' + hyphensong + '-lyrics'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

lyrics = soup.find(str, attrs={"lyrics"}).get_text()

print(lyrics)