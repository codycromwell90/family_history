#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:42:41 2023

@author: psk
"""

import requests
from bs4 import BeautifulSoup

url="https://www.winsipedia.com/games/navy/vs/notre-dame"
page = requests.get(url, allow_redirects=True)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    get_list_tag = soup.find('div', {'id': 'vs_game_list'})
    list_items = get_list_tag.findAll('ul')
    #print (list_items)
    #synonyms = []  # to fetch synonym anytime used list to append all synonyms
    for i in list_items:
        date = i.find('li', {'class':'col2'}).text
        #print(date)
        location = i.find('li', {'class':'col3'}).text
        navyScore = i.find('li', {'class':'col4'}).text
        print(date, location, navyScore)
    #   etc ...
else:
    print("No information found!")