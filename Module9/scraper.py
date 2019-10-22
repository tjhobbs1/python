"""
Program:  scraper.py
Author:  Ty Hobbs
Last Day Modified:  10/20/2019

The purpose of the program is to go out to a webpage that has been specified and scrape it for HTML and then return it.
It uses an addon that also makes it more readable. 
"""

import requests
import bs4 as bs

url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=202001&Campus=1&Subject=CIS&CourseNumber=CIS189'
response = requests.get(url)
html = response.content
with open("requestResult.txt","w+") as file:
    file.writelines(str(html))

soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())
