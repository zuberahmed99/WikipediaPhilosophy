# -*- coding: utf-8 -*-
"""
Created on Fri May 19 21:31:40 2017

@author: Zuber
"""


from urllib import urlopen
from bs4 import BeautifulSoup
import re

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

def getRefinedLinks(bsObj):
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def printLinks(links):
    for link in links:
        print link
    return

#getAllLinks(getBeautifulSoupObject("https://en.wikipedia.org"))
printLinks(getRefinedLinks(getBeautifulSoupObject("https://en.wikipedia.org/wiki/Python_(programming_language)")))