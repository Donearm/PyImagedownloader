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
import lxml.html
from pyimg import *



# values for age verification
values = { 'month': '01', 'day' : '1', 'year' : '1978', 'verifyAge' : 'Confirm'}
headers = { 'User-Agent' : user_agent }
data = urlencode(values, 1)

def imagesocket_parse(link):
    # supply the age verification informations before the first file
    #
    # splitting the url to get only the file name
    filename = link.split('/')
    age_request = urllib2.Request('http://imagesocket.com/warning/' + filename[-1], data, headers)
    age_response = urllib2.urlopen(age_request)

    imagesocket_list = [] # the list that will contain the href tags
    imagesocket_list.append(link)
    for i in imagesocket_list:
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break

        # get every page linked from the imagesocket links
        image_page = response.read()
        page = lxml.html.fromstring(image_page)

        src_links = page.xpath("//img[@id='thumb']")
        imagesocket_src = [li.get('src', None) for li in src_links]


        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('images/', imagesocket_src[0])

            savefile = basedir + save_extension[-1]
            download_url = imagesocket_src[0]
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            break
