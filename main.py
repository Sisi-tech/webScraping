import requests
from bs4 import BeautifulSoup


file = open("quotes.txt", 'w')

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')


# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print(authors[i].text)
#     quoteTags = tags[i].find_all('a', class_='tag')
#     for quoteTag in quoteTags:
#         print(quoteTag.text)


for i in range(0, len(quotes)):
    file.write(f"{quotes[i].text}\n")
    file.write(f"{authors[i].text}\n")
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        file.write(f"{quoteTag.text} " "")
    
        