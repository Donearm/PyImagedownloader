#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
"""
"""
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__email__ = "forod.g@gmail.com"

import re
from urllib import FancyURLopener, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer



# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
#rBellazon = re.compile('href=\"?http://www\.bellazon\.com/http://www\.bellazon\.com/main/index\.php\?act=attach', re.IGNORECASE)
#rBellazon = re.compile("http://www\.bellazon\.com/", re.IGNORECASE)
rBellazon = re.compile("href.*attach\&amp", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

myopener = MyUrlOpener()

def bellazon_parse(link):
    bellazon_list = []
    #bellazon_list.append(page.findAll('a', title=rJpgSrc))
    #bellazon_href = []
    #for li in bellazon_href:
    #    bellazon_href.append(li['href'])
    #    print li
    if rBellazon.search(str(link)):
        bellazon_list.append(link)
        print link
