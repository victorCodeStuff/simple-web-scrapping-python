import requests
from bs4 import BeautifulSoup

website = input("Type your Url:")


result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
title = soup.find('h1').get_text()
text= soup.find('main').get_text()


with open(f'{title}.txt','w') as file:
    file.write(text)



print(text)