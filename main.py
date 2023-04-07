import datetime
import requests
import csv
from bs4 import BeautifulSoup
URL = "https://www.theverge.com/"
ID = 1

# To name the csv file with format dd/mm/yyyy
Now = datetime.datetime.now()
DateTimeStamp = "{:%d%m%Y}".format(Now)
outFile = (DateTimeStamp) + '_verge'
# To name the csv file with format dd/mm/yyyy

r = requests.get(URL)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

divs = soup.find_all(
    'div', class_='flex grow flex-row border-gray-31 py-16 md:flex-row-reverse md:justify-between md:border-b')

with open(f'{outFile}.csv', 'w', newline='', encoding='utf8') as f:

    # To scrape the data into a csv file
    writer = csv.writer(f)
    headers = ['id','headline', 'link', 'author', 'authorProfile', 'date']
    writer.writerow(headers)
    # To scrape the data into a csv file

    for div_element in divs:
        headline = (div_element.find(
            'a', class_="group-hover:shadow-underline-franklin").text)
        link = (URL + div_element.find('a',
                                       class_="group-hover:shadow-underline-franklin").get('href'))
        author = (div_element.find(
            'a', class_="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8").text)
        authorProfile = (URL + div_element.find('a',
                                                class_="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8").get('href'))
        date = (div_element.find(
            'span', class_="text-gray-63 dark:text-gray-94").text)

        articleInfo = [ID,headline, link, author, authorProfile, date]
        ID = ID+1
        writer.writerow(articleInfo)
