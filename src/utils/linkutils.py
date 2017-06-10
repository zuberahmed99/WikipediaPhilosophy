# -*- coding: utf-8 -*-
"""
Created on Fri May 19 21:31:40 2017

@author: Zuber
"""


from urllib import urlopen
from bs4 import BeautifulSoup
import re

def get_all_links(bsObj):
    allLinks = []
    for links in bsObj.findAll("a"):
        if 'href' in links.attrs:
            allLinks.append(links.attrs['href'])
            print links.attrs['href']
    return allLinks

def get_wiki_beautiful_soup_object(wikiURL):
    if wikiURL.startswith("http"):
        return get_beautiful_soup_object(wikiURL)
    url = "https://en.wikipedia.org" + wikiURL
    return get_beautiful_soup_object(url)

def get_beautiful_soup_object(url):
    html = urlopen(url)
    return BeautifulSoup(html)

def get_refined_links(bsObj):
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def print_links(links):
    for link in links:
        print link
    return

def extract_url_from_anchor(link):
    return link.attrs['href']

def get_parent_of_anchor(link, count):
    #print link.parent
    for i in range (count):
        link = link.parent
    return link

def check_if_parent_is_a_note(link):
    link = get_parent_of_anchor(link, 1)
    link_str = str(link)
    first_line = extract_first_line_of_beautiful_soup_object(link_str)
    if first_line.find("role=\"note\"") == -1:
        return False
    return True
    
def check_if_ancestor_is_a_hidden_table(link):
    link = get_parent_of_anchor(link, 3)
    link_str = str(link)
    link_str = str(link)
    first_line = extract_first_line_of_beautiful_soup_object(link_str)
    nav_content = first_line.find("class=\"hlist\"") == -1
    nav_head = first_line.find("class=\"NavHead\"") == -1
    return nav_content or nav_head

def extract_first_line_of_beautiful_soup_object(link):
    link_str = str(link)
    firstline = ""
    if link_str.startswith("<div>"):

        index = link_str.find("</div>")
        firstline = link_str[index]
    #to do
    return firstline

def get_paragraphs(bsObj):
    return bsObj.find("p");

def get_first_anchor_tag(link):
    link = get_paragraphs(link)
    return link.find("a",href=re.compile("^(/wiki/)((?!:).)*$"))



#links = getRefinedLinks(getBeautifulSoupObject("https://en.wikipedia.org/wiki/Science"))
#parent = getParentOfAnchor(links[288],2)
#print parent
#print extractFirstLineOfBeautifulSoupObject(parent)
#print checkIfParentIsANote(parent)
#getAllLinks(getBeautifulSoupObject("https://en.wikipedia.org"))
#printLinks(getRefinedLinks(getBeautifulSoupObject("https://en.wikipedia.org/wiki/Knowledge")))
#print getFirstAnchorTag(getBeautifulSoupObject("https://en.wikipedia.org/wiki/Science"))