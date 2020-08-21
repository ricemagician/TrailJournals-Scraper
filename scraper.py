"""
Written By: Jimmy Li 8/20/20
Purpoase: Extract all journal entries from Dutch's AT journal into a singular html file
"""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.keys import Keys

"""
date_journal = soup.findAll("div", {"class": 'col-sm-12 entry-text-center entry-date'})
print(date_journal[0].prettify())
day_journal = soup.findAll("div", {"class": 'col-sm-12 entry'})
print(day_journal[0].prettify())
"""
def printClass(soup, class_item):
    """Find the items corresponding to a specific class name in your soup and print them to stdout"""

    journal = soup.findAll("div", {"class": class_item})

    #This is a check because  destination/starting point/miles hiked sections were duplicating
    #Although it would probably work for all of the elements we're printing  
    if journal and (class_item.endswith("entry-text") or class_item.endswith("entry-text-right")):
        for entry in journal:
            if entry.get_text() not in printed:
                print(entry.prettify(formatter='html'))
                printed.append(entry.get_text())

    elif journal:
        print(journal[0].prettify(formatter='html'))


url = "https://www.trailjournals.com/journal/entry/26845"
page = requests.get(url)
dutchsoup = BeautifulSoup(page.content, 'html.parser')

"""driver = webdriver.Firefox()

opts = Options()
opts.set_headless()

browser = Firefox(options=opts)
browser.get('https://www.trailjournals.com/journal/entry/26845')
"""

for i in range(1000):
    #I was afraid of starting an infinite loop between dota games so I capped it out

    printed = []
    printClass(dutchsoup, 'col-sm-12 entry-text-center entry-date')
    printClass(dutchsoup, 'col-sm-8 entry-text')
    printClass(dutchsoup, 'col-sm-4 entry-text-right')
    print("<br>")
    printClass(dutchsoup, 'col-sm-12 entry')
    printClass
    print("<br><br><p>=========</p><br><br>")

    new_href= dutchsoup.find_all("a", string="Next")
    if new_href == []:
        break
    new_url = f"https://www.trailjournals.com{new_href[0]['href']}"
    next_page = requests.get(new_url)
    dutchsoup = BeautifulSoup(next_page.content, 'html.parser')

    

    
    
