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
rUpmyphoto = re.compile("http://www\.upmyphoto\.com/img", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

myopener = MyUrlOpener()

def upmyphoto_parse(link):
    upmyphoto_list = [] # the list that will contain the href tags
    upmyphoto_list.append(link['href'])
    for i in upmyphoto_list:
        # get every page linked from the upmyphoto links
        image_page = myopener.open(i)
        Rimage_page = image_page.read()
        page_soup = BeautifulSoup(Rimage_page)
        # find the src attribute which contains the real link of upmyphoto's images
        src_links = page_soup.findAll('img', src=rUpmyphoto)
        upmyphoto_src = []
        for li in src_links:
            upmyphoto_src.append(li['src']) # add all the src part to a list

        # Close the page
        image_page.close()

        # generate just the filename of the image to be locally saved
        # First save_extension is for the old links?
        #save_extension = re.split('img/dir[0-9]+/loc[0-9]+/',  upmyphoto_src[0]) 
        save_extension = re.split('/img/', upmyphoto_src[0])
        savefile = basedir + str(save_extension[1])
        download_url = upmyphoto_src[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
