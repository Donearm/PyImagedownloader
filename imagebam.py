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
import random
from os.path import splitext
import lxml.html
from pyimg import user_agent


values = {}
headers = {'User-Agent': user_agent}
data = urlencode(values)


def imagebam_parse(link, basedir):
    # get every page linked from the imagebam links
    request = urllib2.Request(link, data, headers)
    try:
         response = urllib2.urlopen(request, None, 8)
#         response = http_connector.connector(request)
    except socket.error as e:
        # timing out...
        print("An image couldn't be downloaded")
        return
    except urllib2.HTTPError as e:
        print("An image couldn't be downloaded")
        return
    except urllib2.URLError as e:
        print("An image couldn't be downloaded")
        return

    image_page = response.read()
    page = lxml.html.fromstring(image_page)

    # find the src attribute which contains the real link of imagebam's images
    src_links = page.xpath("//img[@onclick='scale(this);']")

    imagebam_src = [li.get('src', None) for li in src_links]

    # get the image name from the id tag
    imagename = [li.get('id', None) for i in src_links]

    try:
        imagebam_split = re.split('dl\.php\?ID=', imagebam_src[0]) # remove the unneeded parts
    except IndexError:
        # if the splitting fails it's possible that that image has problems and can't
        # really be downloaded, skip it.
        print("An image couldn't be downloaded")
        return

    download_url = imagebam_src[0]

    # generate a random number for the imagename
    num = random.randrange(1,1000)

    # check if the imagename has an extension (jpg by default)
    # if not, add it after having inserted the random number too
    basename, extension = splitext(imagename[0])
    if not extension:
        imagename[0] = str(imagename[0]) + str(num) + '.jpg'
    else:
        imagename[0] = str(basename) + str(num) + str(extension)

    try: 
        savefile = join(basedir, str(imagename[0]))
    except UnicodeEncodeError:
        # catch files with strange characters in name
        savefile = join(basedir, str(imagename[0].encode("utf-8")))

    # finally save the image in the desidered directory
    try:
        urlretrieve(download_url, savefile) 
    except IOError as e:
        # image not loading, skipping it
        return

