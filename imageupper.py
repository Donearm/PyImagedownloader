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



values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def imageupper_parse(link):
    imageupper_list = [] # the list that will contain the href tags
    imageupper_list.append(link)
    for i in imageupper_list:
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break

        # get every page linked from the imageupper links
        image_page = response.read()
        page = lxml.html.fromstring(image_page)

        src_links = page.xpath("//img[@id='img']")
        imageupper_src = [li.get('src', None) for li in src_links]



        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('[0-9]+/[0-9]+/', imageupper_src[0])

            savefile = basedir + save_extension[-1]
            download_url = imageupper_src[0]
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            break
