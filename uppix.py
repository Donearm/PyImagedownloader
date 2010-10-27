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
from urllib import urlretrieve, urlencode
from os.path import join
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import user_agent


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def uppix_parse(link, basedir):
    # get every page linked from the uppix links
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

    # find the src attribute which contains the real link of uppix's images
    #src_links = page_soup.findAll('img', id='dpic')
    src_links = page.xpath("//img[@id='dpic']")

    uppix_src = [li.get('src', None) for li in src_links]

    # generate just the filename of the image to be locally saved
    save_extension = re.sub('S[0-9]+/', '',  uppix_src[0]) 
    uppix_sub = re.sub('Viewer[a-zA-Z]\.php\?file=', '', link)
    savefile = join(basedir, save_extension)
    # finally save the image on the desidered directory
    urlretrieve(uppix_sub, savefile) 
