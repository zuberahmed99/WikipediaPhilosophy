# -*- coding: utf-8 -*-
"""
Created on Sun May 21 02:03:11 2017

@author: Zuber
"""
import linkutils
import time
RANDOM_ARTICLE = "http://en.wikipedia.org/wiki/Special:Random"
PHILOSOPHY_ARTICLE = "/wiki/Science"

def crawl_first_link(startLink):
    print startLink
    index = 0
    bsObj = linkutils.get_wiki_beautiful_soup_object(startLink)
    link = linkutils.get_first_anchor_tag(bsObj)

    return linkutils.extract_url_from_anchor(link)

def get_hops(startLink):
    count = 0

    while startLink != PHILOSOPHY_ARTICLE:
        startLink = crawl_first_link(startLink)
        time.sleep(0.1)
        count += 1

    return count

def random_article_crawler(num):
    for i in range(num):
        print "crawling random article "
        get_hops(RANDOM_ARTICLE)

def main():
    random_article_crawler(5)
    
main()