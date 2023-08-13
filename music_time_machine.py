import requests
from bs4 import BeautifulSoup
import re
import random
# # billboard_url = 'https://www.billboard.com/charts/hot-100/#'
billboard_url = 'https://www.billboard.com/charts/hot-100/1980-07-03/'
response_text = requests.get(billboard_url).text
response_soup = BeautifulSoup(response_text,'html.parser')
# print(response_soup.prettify())

song_title = response_soup.find_all(name='h3', class_='a-no-trucate')
song_list = [song.getText().strip() for song in song_title]

song_artist = response_soup.find_all(name='span', class_='a-no-trucate')
artists_names = [artist.get_text().strip() for artist in song_artist]

# student_scores = {student:random.randint(1,100) for student in names}
for n in range(0,100):
    print(f'{song_list[n]} -- {artists_names[n]}')

# # date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# # URL = "https://www.billboard.com/charts/hot-100/"
# URL = 'https://www.billboard.com/charts/hot-100/1980-07-03/'
# # response = requests.get(URL + date)
# response = requests.get(URL)
# website_html = response.text
# soup = BeautifulSoup(website_html, "html.parser")
# song_name = soup.find_all(name="h3", class_="a-no-trucate")
# song_title = [song.getText().strip() for song in song_name]
# for song in song_title:
#     print(song)
