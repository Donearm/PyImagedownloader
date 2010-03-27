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
from urllib import urlencode, urlretrieve
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import *
#from http_connector import post_request


# Regexp needed for the src links
#rSrcBlogspot = re.compile('http://[0-9]\.bp\.blogspot\.com/.*\.(jpg|jpeg|gif|png)', re.IGNORECASE)

values = {}
headers = {'User-Agent': user_agent}
data = urlencode(values)

def blogspot_parse(link):
    blogspot_list = [] # the list that will contain the href tags
    #blogspot_list.append(link['href'])
    blogspot_list.append(link)
    for i in blogspot_list:
        #response = post_request(i, data, headers)
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break

        # No need for blogspot to call lxml again, the links in blogspot_list
        # are already the direct urls to the full image

        # generate just the filename of the image to be locally saved
        #save_extension = re.split('(/[0-9A-Za-z_-]+/)*', blogspot_src[0])
        save_extension = re.split('/s1600/', i)

        savefile = basedir + str(save_extension[-1])

        download_url = i
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
