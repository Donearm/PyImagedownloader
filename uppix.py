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



# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2b4) Gecko/20091202 Firefox/3.6b4'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def uppix_parse(link):
    uppix_list = [] # the list that will contain the href tags
    #uppix_list.append(link['href'])
    uppix_list.append(link)
    for i in uppix_list:
        # get every page linked from the uppix links
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

        # find the src attribute which contains the real link of uppix's images
        #src_links = page_soup.findAll('img', id='dpic')
        src_links = page.xpath("//img[@id='dpic']")
        uppix_src = []
        for li in src_links:
            #uppix_src.append(li['src']) # add all the src part to a list
            uppix_src.append(li.get('src', None))

        # generate just the filename of the image to be locally saved
        save_extension = re.sub('S[0-9]+/', '',  uppix_src[0]) 
        uppix_sub = re.sub('Viewer[a-zA-Z]\.php\?file=', '', i)
        savefile = basedir + save_extension
        # finally save the image on the desidered directory
        urlretrieve(uppix_sub, savefile) 
