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
from BeautifulSoup import BeautifulSoup, SoupStrainer
from imagevenue import imagevenue_embed
from pyimg import *

# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rUsercash = re.compile("href=\"?http://[0-9]+\.usercash\.com", re.IGNORECASE)
rImagevenue = re.compile("http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def usercash_parse(link):    
    # get every page linked from the usercash links
    request = urllib2.Request(link, data, headers)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        print("An image couldn't be downloaded")
        return
    except urllib2.URLError as e:
        print("An image couldn't be downloaded")
        return

    image_page = response.read()
    page_soup = BeautifulSoup(image_page)
    # find the src attribute which contains the real link of imagevenue's images
    src_links = page_soup.findAll('frame', src=rJpgSrc)

    # give imagevenue_embed the correct link
    correct_link = re.sub("^.*http", 'http', str(src_links))
    correct_link = re.sub("&amp;ref=.*$", '', correct_link)

    if rImagevenue.search(correct_link):
        imagevenue_embed(correct_link)


