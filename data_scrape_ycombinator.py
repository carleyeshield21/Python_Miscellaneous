from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://news.ycombinator.com/news').text
# response.raise_for_status()

# creating a soup from where we will scrape data
the_soap = BeautifulSoup(response, 'html.parser')
# print(the_soap.prettify())

links = []
# extracting only the valid links in the bs4 Tag
articles = the_soap.find_all(name='a')
for arts in articles:
    the_link = arts.get('href')
    # print(the_link)
    if 'https://' in the_link:
        # print(the_link)
        links.append(the_link)

scores = []
# sample of extracting a specific piece of data, here we extract the score
articles1 = the_soap.find_all(name='span', class_='score')
# looping through each item, then using the split to further extract the numerical data using the the int to convert
# from string into an integer value
for art in articles1:
    # print(art.text)
    # print(art.text.split(' ')[0])
    print(int(art.text.split(' ')[0]))

score_list = [int(art.text.split(' ')[0]) for art in articles1]
print(score_list)

# # new_list = [new_item for item in list]
# extracting the text from the bs4 Tag
article_text = the_soap.find_all(name='span',class_='titleline')
for text in article_text:
    print(text.get_text())

text_list = [text.get_text() for text in article_text]
print(text_list)
