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
from os.path import join
import lxml.html
from pyimg import user_agent



values = {}
headers = {'User-Agent': user_agent}
data = urlencode(values)


def turboimagehost_parse(link, basedir):
    # get every page linked from the turboimagehost links
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

    # find the src attribute which contains the real link of turboimagehost's images
    src_links = page.xpath("//img[@id='imageid']")

    turboimagehost_src = [li.get('src', None) for li in src_links]


    # get just the filename
    turboimagehost_split = re.split('[0-9A-Za-z]+/', turboimagehost_src[0])

    download_url = turboimagehost_src[0]

    try: 
        # generate just the filename of the image to be locally saved
        savefile = join(basedir, str(turboimagehost_split[-1]))
    except UnicodeEncodeError:
        # catch files with strange characters in name
        savefile = join(basedir, str(turboimagehost_split[-1].encode("utf-8")))

    # finally save the image in the desidered directory
    urlretrieve(download_url, savefile) 

