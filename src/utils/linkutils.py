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

def getWikiBeautifulSoupObject(wikiURL):
    if wikiURL.startswith("http"):
        return getBeautifulSoupObject(wikiURL)
    url = "https://en.wikipedia.org" + wikiURL
    return getBeautifulSoupObject(url)

def getBeautifulSoupObject(url):
    html = urlopen(url)
    return BeautifulSoup(html)

def getRefinedLinks(bsObj):
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def printLinks(links):
    for link in links:
        print link
    return

def extractURLFromAnchor(link):
    return link.attrs['href']

def getParentOfAnchor(link, count):
    #print link.parent
    for i in range (count):
        link = link.parent
    return link

def checkIfParentIsANote(link):
    link = getParentOfAnchor(link,1)
    link_str = str(link)
    first_line = extractFirstLineOfBeautifulSoupObject(link_str)
    if first_line.find("role=\"note\"") == -1:
        return False
    return True
    
def checkIfAncestorIsAHiddenTable(link):
    link = getParentOfAnchor(link,3)
    link_str = str(link)
    link_str = str(link)
    first_line = extractFirstLineOfBeautifulSoupObject(link_str)
    nav_content = first_line.find("class=\"hlist\"") == -1
    nav_head = first_line.find("class=\"NavHead\"") == -1
    return nav_content or nav_head

def extractFirstLineOfBeautifulSoupObject(link):
    link_str = str(link)
    firstline = ""
    if link_str.startswith("<div>"):

        index = link_str.find("</div>")
        firstline = link_str[index]
    #to do
    return firstline

def getParagraphs(bsObj):
    return bsObj.find("p");

def getFirstAnchorTag(link):
    link = getParagraphs(link)
    return link.find("a",href=re.compile("^(/wiki/)((?!:).)*$"))



#links = getRefinedLinks(getBeautifulSoupObject("https://en.wikipedia.org/wiki/Science"))
#parent = getParentOfAnchor(links[288],2)
#print parent
#print extractFirstLineOfBeautifulSoupObject(parent)
#print checkIfParentIsANote(parent)
#getAllLinks(getBeautifulSoupObject("https://en.wikipedia.org"))
#printLinks(getRefinedLinks(getBeautifulSoupObject("https://en.wikipedia.org/wiki/Knowledge")))
#print getFirstAnchorTag(getBeautifulSoupObject("https://en.wikipedia.org/wiki/Science"))