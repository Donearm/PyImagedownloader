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
rImageshack = re.compile("href=\"?http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

myopener = MyUrlOpener()

def imageshack_parse(link):
    rSrcImageshack = re.compile('http://img([0-9]{,3})\.imageshack\.us/img[0-9]+/[0-9]+/[0-9a-z]+\.jpg')
    imageshack_list = [] # the list that will contain the href tags
    imageshack_list.append(link['href'])
    for i in imageshack_list:
        # get every page linked from the imageshack links
        image_page = myopener.open(i).read()
        #Rimage_page = image_page.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of imageshack's images
        src_links = page_soup.findAll('img', src=rSrcImageshack)
        imageshack_src = []
        for li in src_links:
            imageshack_src.append(li['src']) # add all the src part to a list

        # Close the page
        #image_page.close()

        # generate just the filename of the image to be locally saved
        save_extension = re.split('img[0-9]{,3}/[0-9]+/', imageshack_src[0]) 
        savefile = basedir + str(save_extension[1])
        download_url = imageshack_src[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
