# -*- coding: utf-8 -*-
"""
Created on Sun May 21 02:03:11 2017

@author: Zuber
"""
import linkutils
import time

PHILOSOPHY_ARTICLE = "/wiki/Science"

def crawlFirstLink(startLink):
    print startLink
    index = 0
    bsObj = linkutils.getWikiBeautifulSoupObject(startLink)
    link = linkutils.getFirstAnchorTag(bsObj)

    return linkutils.extractURLFromAnchor(link)

def getHops(startLink):
    count = 0

    while startLink != PHILOSOPHY_ARTICLE:
        startLink = crawlFirstLink(startLink)
        time.sleep(0.1)
        count += 1

    return count

def main():
    print getHops("https://en.wikipedia.org/wiki/Cricket")
    
main()