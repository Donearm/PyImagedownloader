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


# The regexp we'll need to find the link
#rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
#rShareapic = re.compile('http://www\.shareapic\.net', re.IGNORECASE)
#rSrcShareapic = re.compile('http://images\.shareapic\.net')

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def shareapic_parse(link):
    shareapic_list = [] # the list that will contain the href tags
    #shareapic_list.append(link['href'])
    shareapic_list.append(link)
    for i in shareapic_list:
        # get every page linked from the shareapic links
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
        # find the src attribute which contains the real link of shareapic's images
        #src_links = page_soup.findAll('img', src=rSrcShareapic)
        src_links = page.xpath("//img[@title='Click to zoom! ::']")
        shareapic_fullsize = []
        for li in src_links:
            fullsize_li = re.sub(r"images([0-9])", r"fullsize\1", li.get('src', None))
            #fullsize_li = re.sub(r"images([0-9])", r"fullsize\1", li['src'])
            shareapic_fullsize.append(fullsize_li) # add all the src part to a list

        download_url = shareapic_fullsize[0]
        # generate just the filename of the image to be locally saved
        save_extension = re.split('fullsize[0-9]', shareapic_fullsize[0]) 
        savefile = basedir + str(save_extension[1])
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

