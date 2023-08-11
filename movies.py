import requests
from bs4 import BeautifulSoup

movie_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

movie_request = requests.get(movie_url)
response = movie_request.text
response_soup = BeautifulSoup(response,'html.parser')
# print(response_soup.prettify())

movie_tag = response_soup.find_all(name='h3',class_='title')
# for movie in movie_tag:
#     print(movie.get_text())

movie_list = [movie.get_text() for movie in movie_tag]
# print(movie_list)
ordered_movie_list = movie_list[::-1]
print(ordered_movie_list)

with open('movies.txt', mode='w') as file:
    for movie_title in ordered_movie_list:
        file.write(f'{movie_title}\n')