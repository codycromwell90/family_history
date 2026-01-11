#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:53:05 2023

@author: psk
"""

from lxml import html
import requests

url="https://www.winsipedia.com/games/navy/vs/notre-dame"

resp = requests.get(url)
print(resp)

tree = html.fromstring(resp.content)
elements = tree.xpath("//div[@id='vs_game_list']/section/ul")

dateCol = tree.xpath("//div[@id='vs_game_list']/section/ul/li[2]/text()")
print(dateCol)

locationCol = tree.xpath("//div[@id='vs_game_list']/section/ul/li[3]/text()")
print(locationCol)

#@class attribute holds a win / loss value - probably used to color code score
#would need to strip out second token in value
navyWinLossAttrCol = tree.xpath("//div[@id='vs_game_list']/section/ul/li[4]/@class")
print(navyWinLossAttrCol)
navyScoreCol = tree.xpath("//div[@id='vs_game_list']/section/ul/li[4]/text()")
print(navyScoreCol)

#etc ...