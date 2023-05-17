import requests
from bs4 import BeautifulSoup
import random

elon_musk_quotes1 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes').text
elon_musk_quotes2 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_2').text
elon_musk_quotes3 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_3').text
elon_musk_quotes4 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_4').text
# elon_musk_quotes1.raise_for_status()

soup1 = BeautifulSoup(elon_musk_quotes1, 'lxml')
soup2 = BeautifulSoup(elon_musk_quotes2, 'lxml')
soup3 = BeautifulSoup(elon_musk_quotes3, 'lxml')
soup4 = BeautifulSoup(elon_musk_quotes4, 'lxml')
# print(soup1.prettify())

list_quotes = []

quotes1 = soup1.find_all('a',class_='b-qt')
for quote in quotes1:
    q1 = quote.find('div').text.strip()
    # print(q1)
    list_quotes.append(q1)

quotes2 = soup2.find_all('a',class_='b-qt')
for quote in quotes2:
    q2 = quote.find('div').text.strip()
    # print(q2)
    list_quotes.append(q2)

quotes3 = soup3.find_all('a',class_='b-qt')
for quote in quotes3:
    q3 = quote.find('div').text.strip()
    # print(q3)
    list_quotes.append(q3)

quotes4 = soup4.find_all('a',class_='b-qt')
for quote in quotes4:
    q4 = quote.find('div').text.strip()
    # print(q4)
    list_quotes.append(q4)

# print(list_quotes)
# print(len(list_quotes))

random_quote = random.choice(list_quotes)
print(random_quote)
