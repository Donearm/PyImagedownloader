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
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import *
#from http_connector import get_request


# The regexp we'll need to find the link
#rSrcImagebam = re.compile("http://[0-9]+\.imagebam\.com/dl\.php") # regexp for the src link



def imagebam_parse(link):
    imagebam_list = [] # the list that will contain the href tags
    #imagebam_list.append(link['href'])
    imagebam_list.append(link)
    for i in imagebam_list:
        # get every page linked from the imagebam links
        #response = get_request(i)
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break

        image_page = response.read()
        #image_page = myopener.open(i).read()
        #page_soup = BeautifulSoup(image_page)
        page = lxml.html.fromstring(image_page)

        # find the src attribute which contains the real link of imagebam's images
        #src_links = page_soup.findAll('img', src=rSrcImagebam)
        src_links = page.xpath("//img[@onclick='scale();']")

        imagebam_src = [li.get('src', None) for li in src_links]

        imagebam_split = re.split('dl\.php\?ID=', imagebam_src[0]) # remove the unneeded parts
        download_url = imagebam_src[0]
        # generate just the filename of the image to be locally saved
        # TODO: іf the image is not a jpeg how to get the correct extension?
        savefile = basedir + str(imagebam_split[1]) + ".jpg"
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

