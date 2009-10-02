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

# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rImgshed = re.compile("href=\"?http://imgshed\.com", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def imgshed_parse(link):
    imgshed_list = [] # the list that will contain the href tags
    imgshed_list.append(link['href'])
    for i in imgshed_list:
        # get every page linked from the imgshed links
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break
        image_page = response.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of imgshed's images
        src_links = page_soup.findAll('img', id='theimage')
        imgshed_src = []
        for li in src_links:
            imgshed_src.append(li['src']) # add all the src part to a list


        # generate just the filename of the image to be locally saved
        save_extension = re.sub('^\./files/', '', imgshed_src[0]) 
        download_url = 'http://imgshed.com/files/' + save_extension

        savefile = basedir + save_extension
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
