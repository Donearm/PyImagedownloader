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
rShareapic = re.compile('http://www\.shareapic\.net', re.IGNORECASE)
rSrcShareapic = re.compile('http://images\.shareapic\.net')

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

# Instanciate the UrlOpener
myopener = MyUrlOpener()

def shareapic_parse(link):

    shareapic_list = [] # the list that will contain the href tags
    shareapic_list.append(link['href'])
    for i in shareapic_list:
        print i
        # get every page linked from the shareapic links
        image_page = myopener.open(i).read()
        #Rimage_page = image_page.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of shareapic's images
        src_links = page_soup.findAll('img', src=rSrcShareapic)
        shareapic_fullsize = []
        for li in src_links:
            fullsize_li = re.sub(r"images([0-9])", r"fullsize\1", li['src'])
            print fullsize_li
            shareapic_fullsize.append(fullsize_li) # add all the src part to a list

        # Close the page
        #image_page.close()

        download_url = shareapic_fullsize[0]
        # generate just the filename of the image to be locally saved
        save_extension = re.split('fullsize[0-9]', shareapic_fullsize[0]) 
        savefile = basedir + str(save_extension[1])
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

