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
import urllib2
from urllib import urlretrieve, urlencode
from BeautifulSoup import BeautifulSoup, SoupStrainer

# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rStoreimgs = re.compile("href=\"?http://storeimgs\.com", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def storeimgs_parse(link):
    storeimgs_list = [] # the list that will contain the href tags
    storeimgs_list.append(link['href'])
    for i in storeimgs_list:
        # get every page linked from the storeimgs links

        # make the image url by a couple of substitution and then using a split
        # to dissectate the url and add the 'i' needed before the image name
        download_url = re.sub('show', 'out', i)
        download_url = re.sub('\.html$', '', download_url)

        storeimgs_split = re.split('out.php/', download_url)

        download_url = storeimgs_split[0] + 'out.php/i' + storeimgs_split[1]

        # generate just the filename of the image to be locally saved
        save_extension = storeimgs_split[1]

        savefile = basedir + save_extension
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
