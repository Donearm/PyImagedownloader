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
    #TODO: currently this doesn't work, urlretrieve doesn't download the full image
    # but block itself with an Http error 405 "not allowed". Using POST or GET or checking
    # the Content-Length header doesn't resolve the issue.

    request = urllib2.Request(link, data, headers)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        print("An image couldn't be downloaded")
        return
    except urllib2.URLError as e:
        print("An image couldn't be downloaded")
        return

    # get every page linked from the postimage links
    image_page = response.read()
    page = lxml.html.fromstring(image_page)

    # Little trick: check if we have an img with an height; that would mean
    # the image is already fullsized. If there is no height, the image is
    # resized and we act accordingly
    height_present = page.xpath("//img[@height]")
    if height_present:
        src_links = page.xpath("//center/img")
        postimage_src = [li.get('src', None) for li in src_links]
        postimage_alt = [li.get('alt', None) for li in src_links]
    else:
        alt_links = page.xpath("//center/a[@href]/img[@alt]")
        postimage_alt = [li.get('alt', None) for li in alt_links]

        href_links = page.xpath("//center/a[@href]")
        postimage_src = [li.get('href', None) for li in href_links]


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
        return
