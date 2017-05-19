# -*- coding: utf-8 -*-
"""
Created on Fri May 19 21:31:40 2017

@author: Zuber
"""


from urllib import urlopen
from bs4 import BeautifulSoup

def getAllLinks(bsObj):
    allLinks = []
    for links in bsObj.findAll("a"):
        if 'href' in links.attrs:
            allLinks.append(links.attrs['href'])
            print links.attrs['href']
    return allLinks

def getBeautifulSoupObject(url):
    html = urlopen(url)
    return BeautifulSoup(html)

getAllLinks(getBeautifulSoupObject("https://www.en.wikipedia.org"))