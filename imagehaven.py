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
rImagehaven = re.compile("href=\"?http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

myopener = MyUrlOpener()

def imagehaven_parse(link):
    rSrcImagehaven = re.compile("\./images") # regexp for the src link
    imagehaven_list = [] # the list that will contain the href tags
    imagehaven_list.append(link['href'])
    for i in imagehaven_list:
        # get every page linked from the imagehaven links
        image_page = myopener.open(i).read()
        #Rimage_page = image_page.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of imagehaven's images
        src_links = page_soup.findAll('img', src=rSrcImagehaven)
        imagehaven_src = []
        for li in src_links:
            imagehaven_src.append(li['src']) # add all the src part to a list

        # Close the page
        #image_page.close()

        imagehaven_split = re.split('img\.php\?id=', i) # remove the unneeded parts
        imagehaven_split2 = re.split('\.\/', imagehaven_src[0]) 
        try:
            # make up the real image url
            download_url = str(imagehaven_split[0]) + str(imagehaven_split2[1])
        except IndexError:
            # if we get an IndexError just continue (it may means that the image
            # can't be downloaded from the server or there is a host's glitch
            continue
        # generate just the filename of the image to be locally saved
        save_extension = re.split('\./images/[0-9A-Za-z]+/[0-9A-Za-z]+/', imagehaven_src[0]) 
        savefile = basedir + str(save_extension[1])
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 


