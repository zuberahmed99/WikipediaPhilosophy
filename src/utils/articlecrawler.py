# -*- coding: utf-8 -*-
"""
Created on Sun May 21 02:03:11 2017

@author: Zuber
"""
import linkutils
import time

PHILOSOPHY_ARTICLE = "wiki/Philosophy"

def crawlFirstLink(startLink):
    bsObj = linkutils.getWikiBeautifulSoupObject(startLink)
    links = linkutils.getRefinedLinks(bsObj)
    return linkutils.extractURLFromAnchor(links[0])

def getHops(startLink):
    count = 0
    while startLink != PHILOSOPHY_ARTICLE:
        startLink = crawlFirstLink(startLink)
        time.sleep(0.1)
        count += 1
    return count

def main():
    getHops("https://en.wikipedia.org/wiki/Science")
    
main()