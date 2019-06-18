# Exercise

# https://www.rithmschool.com/blog

import requests
from csv import writer
from bs4 import BeautifulSoup

count = 1

with open('Udemy/Modern_Python3_Bootcamp/blog_data.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Title", "URL", "Date"])

    while True:
        response = requests.get(f'https://www.rithmschool.com/blog?page={count}')
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.findAll('article')

        for article in articles:
            title = article.find('a').get_text()
            url = article.find('a')['href']
            date = article.find('time')['datetime']
            csv_writer.writerow([title, url, date])
            
        count += 1
        
        if not articles:
            break