#!/usr/bin/env python2
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
from os.path import join
import lxml.html
from pyimg import user_agent


values = {}
headers = {'User-Agent': user_agent}
data = urlencode(values)


def imagehostorg_parse(link, basedir):
    # get every page linked from the imagehostorg links
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
    page = lxml.html.fromstring(image_page)

    # find the src attribute which contains the real link of imagehostorg's images
    src_links = page.xpath("//div[@id='content']/img")

    imagehostorg_src = [li.get('src', None) for li in src_links]

    if not imagehostorg_src:
        # there is an ajax script to show the image and thus no src url
        # we use the link in imagehostorg_list to generate the image name
        # and get the content      
        imagehostorg_split = re.split('/', link)
        download_url = re.sub('view', 'secure', link)

        savefile = join(basedir, str(imagehostorg_split[-1]))

        urlretrieve(download_url, savefile)
    else:

        imagehostorg_split = re.split('/', imagehostorg_src[0]) # remove the unneeded parts
        download_url = imagehostorg_src[0]
        # generate just the filename of the image to be locally saved
        savefile = join(basedir, str(imagehostorg_split[-1]))

        # finally save the image in the desidered directory
        urlretrieve(download_url, savefile) 

