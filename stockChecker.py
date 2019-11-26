import requests
import bs4
import random
import webbrowser
import os



def checkStock(URL, model):
    #even with this still the issue of timing out,
    REQUESTS_MAX_RETRIES = int(os.getenv("REQUESTS_MAX_RETRIES", 4))

    headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    RawHTML =requests.get(URL, headers=headers)
    Page = bs4.BeautifulSoup(RawHTML.text, "lxml")
    RawSizeList = Page.select('.size-dropdown-block')
    Sizes = str(RawSizeList[0].getText().replace('\t',''))
    Sizes = Sizes.replace('\n\n', ' ')
    Sizes = Sizes.split()
    Sizes.remove('Select')
    Sizes.remove('size')
    for size in Sizes:
            print(str(model) + 'Size:' + str(size) + ' Available')
