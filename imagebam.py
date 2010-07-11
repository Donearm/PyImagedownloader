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
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import user_agent
#from http_connector import get_request


# The regexp we'll need to find the link
#rSrcImagebam = re.compile("http://[0-9]+\.imagebam\.com/dl\.php") # regexp for the src link

values = {}
headers = {'User-Agent': user_agent}
data = urlencode(values)


def imagebam_parse(link, basedir):
    # get every page linked from the imagebam links
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
    #page_soup = BeautifulSoup(image_page)
    page = lxml.html.fromstring(image_page)

    # find the src attribute which contains the real link of imagebam's images
    #src_links = page_soup.findAll('img', src=rSrcImagebam)
    src_links = page.xpath("//img[@onclick='scale(this);']")

    imagebam_src = [li.get('src', None) for li in src_links]

    # get the image name from the id tag
    imagename = [li.get('id', None) for i in src_links]

    imagebam_split = re.split('dl\.php\?ID=', imagebam_src[0]) # remove the unneeded parts
    download_url = imagebam_src[0]
    # generate just the filename of the image to be locally saved
    # not needed anymore since getting the name from the id tag
    #savefile = basedir + str(imagebam_split[1]) + ".jpg"
    savefile = join(basedir, str(imagename[0]))

    # finally save the image in the desidered directory
    urlretrieve(download_url, savefile) 

