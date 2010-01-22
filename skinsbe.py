#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008, Gianluca Fiore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__email__ = "forod.g@gmail.com"

import re
import urllib2
from urllib import urlretrieve, urlencode
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import *



values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def skinsbe_parse(link):
    skinsbe_list = [] # the list that will contain the href tags
    #skinsbe_list.append(link['href'])
    skinsbe_list.append(link)
    for i in skinsbe_list:
        # get every page linked from the skinsbe links
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break

        image_page = response.read()
        #page_soup = BeautifulSoup(image_page)
        page = lxml.html.fromstring(image_page)

        # find the src attribute which contains the real link of skinsbe's images
        #src_links = page_soup.findAll('img', id='wallpaper_image')
        src_links = page.xpath("//img[@id='wallpaper_image']")

        skinsbe_src = [li.get('src', None) for li in src_links]

        # generate just the filename of the image to be locally saved
        save_extension = re.sub("^.*[0-9]\/", '', skinsbe_src[0])
        savefile = basedir + save_extension

        download_url = skinsbe_src[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
