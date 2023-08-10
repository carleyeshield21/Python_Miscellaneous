from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://news.ycombinator.com/news').text
# response.raise_for_status()

# creating a soup from where we will scrape data
the_soap = BeautifulSoup(response, 'html.parser')
# print(the_soap.prettify())

# articles = the_soap.find_all(name='span', class_='titleline')
# item = articles[0]
# print(item)
# print(item.get_text())

# sample of extracting a specific piece of data, here we extract the score
articles1 = the_soap.find_all(name='span', class_='score')
print(articles1[0].get_text())

# looping through each item, then using the split to further extract the numerical data using the the int to convert
# from string into an integer value
for art in articles1:
    print(art.text)
    print(art.text.split(' ')[0])
    print(int(art.text.split(' ')[0]))

# the_text = the_soap.find(name='span',class_='score')
# print(the_text)s