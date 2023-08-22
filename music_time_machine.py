import requests
from bs4 import BeautifulSoup

chosen_date = input('Choose a date in this format: YYYY-MM-DD\n')
billboard_url = 'https://www.billboard.com/charts/hot-100/' + chosen_date
response_text = requests.get(billboard_url).text
response_soup = BeautifulSoup(response_text,'html.parser')
# print(response_soup.prettify())

song_title = response_soup.find_all(name='h3', class_='a-no-trucate')
song_list = [song.getText().strip() for song in song_title]

song_artist = response_soup.find_all(name='span', class_='a-no-trucate')
artists_names = [artist.get_text().strip() for artist in song_artist]

# student_scores = {student:random.randint(1,100) for student in names}
for n in range(0,100):
    print(f'{n+1}. {song_list[n]} -- {artists_names[n]}')

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

# ==============================================================================

# import requests
# from bs4 import BeautifulSoup

# # chosen_date = input('Choose a date in this format: YYYY-MM-DD\n')
# # billboard_url = 'https://www.billboard.com/charts/hot-100/' + chosen_date
# billboard_url = 'https://www.billboard.com/charts/hot-100/1990-12-25'
# response_text = requests.get(billboard_url).text
# response_soup = BeautifulSoup(response_text,'html.parser')

# peak = response_soup.select('li ul li span', class_=['o-chart-results-list__item'])
# list = [pos.get_text().strip() for pos in peak]
# wks_on_chart = []
# n = 3
# for num in range(n,103):
#     wks_on_chart.append(int(list[n]))
#     n+=7

# peak_pos = []
# m= 2
# for num in range(m,102):
#     peak_pos.append(int(list[m]))
#     m+=7

# print(wks_on_chart)
# print(peak_pos)


# # ===============================================================
# song_title = response_soup.find_all(name='h3', class_='a-no-trucate')
# song_list = [song.getText().strip() for song in song_title]

# song_artist = response_soup.find_all(name='span', class_='a-no-trucate')
# artists_names = [artist.get_text().strip() for artist in song_artist]

# # student_scores = {student:random.randint(1,100) for student in names}
# for n in range(0,100):
#     print(f'{n+1}. {song_list[n]} -- {artists_names[n]}')
