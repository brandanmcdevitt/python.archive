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

        # for each article on the page, take the title, url and date and write
        # it to the blog_data.csv file
        for article in articles:
            title = article.find('a').get_text()
            url = article.find('a')['href']
            date = article.find('time')['datetime']
            csv_writer.writerow([title, url, date])
        
        # increment by 1 each time to crawl through pagination
        count += 1
        
        # break out of the loop if no articles are found
        if not articles:
            break