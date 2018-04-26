#!/usr/bin/env python

import json
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

#url = 'https://www.toutiao.com/search/?keyword='
url = 'https://www.toutiao.com/search_content/?offset=0&format=json&keyword=btc&autoload=true&count=20&cur_tab=1&from=search_tab'

def getData():
    response = urlopen(url)
    data = response.read()
    response.close()
    #soup = BS(data, 'html.parser')
    #print(soup.title)
    #return soup
    jsonData = json.load(data)
    print(jsonData)
    return jsonData


def main():
    print('Start:\n')
    getData()

if __name__ == '__main__':
    main()
