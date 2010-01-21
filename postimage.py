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

def postimage_parse(link):
    postimage_list = [] # the list that will contain the href tags
    postimage_list.append(link)
    for i in postimage_list:
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break

        # get every page linked from the postimage links
        image_page = response.read()
        page = lxml.html.fromstring(image_page)

        # find the src attribute which contains the real link of postimage's images
        # postimage has two different implementations: the first is for images resized
        # and to be seen full size with a click and the second is for small images
        # already at full size
        postimage_src = []
        postimage_alt = []
        try:
            alt_links = page.xpath("//center/a[@href]/img[@alt]")
            for li in alt_links:
                # add the alt to a list
                postimage_alt.append(li.get('alt', None))

            href_links = page.xpath("//center/a[@href]")
            for li in href_links:
                # add the href to the other list
                postimage_src.append(li.get('href', None))
        except:
            print("Haven't found anything....")
        else:
            src_links = page.xpath("//center/img")
            print("We are here")
            for li in src_links:
                # add the src to a list and the alt to another
                postimage_src.append(li.get('src', None))
                postimage_alt.append(li.get('alt', None))


        try:
            # generate just the filename of the image to be locally saved
            #save_extension = re.split('\.org/', postimage_src[0])
            save_extension = postimage_alt[0]

            #savefile = basedir + str(save_extension[1])
            savefile = basedir + save_extension
            download_url = postimage_src[0]
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            break
