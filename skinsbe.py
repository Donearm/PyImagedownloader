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
rSkinsBe = re.compile("href=\"?http://image\.skins\.be", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def skinsbe_parse(link):
    skinsbe_list = [] # the list that will contain the href tags
    skinsbe_list.append(link['href'])
    for i in skinsbe_list:
        # get every page linked from the skinsbe links
        request = urllib2.Request(i, data, headers)
        response = urllib2.urlopen(request)
        image_page = response.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of skinsbe's images
        src_links = page_soup.findAll('img', id='wallpaper_image')
        skinsbe_src = []
        for li in src_links:
            skinsbe_src.append(li['src']) # add all the src part to a list

        # generate just the filename of the image to be locally saved
        #save_extension = re.sub('^\./files/', '', skinsbe_src[0]) 
        #download_url = 'http://skinsbe.com/files/' + save_extension

        download_url = skinsbe_src[0]

        save_extension = re.sub("^.*[0-9]\/", '', skinsbe_src[0])

        savefile = basedir + save_extension
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
