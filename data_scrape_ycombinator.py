from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://news.ycombinator.com/news').text
# response.raise_for_status()

# creating a soup from where we will scrape data
the_soap = BeautifulSoup(response, 'html.parser')
# print(the_soap.prettify())

# extracting only the valid links in the bs4 Tag
articles = the_soap.find_all(name='a')
for arts in articles:
    the_link = arts.get('href')
    # print(the_link)
    if 'https://' in the_link:
        print(the_link)

# sample of extracting a specific piece of data, here we extract the score
# articles1 = the_soap.find_all(name='span', class_='score')
# print(articles1[0].get_text())

# looping through each item, then using the split to further extract the numerical data using the the int to convert
# from string into an integer value
# for art in articles1:
#     print(art.text)
#     print(art.text.split(' ')[0])
#     print(int(art.text.split(' ')[0]))
