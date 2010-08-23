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
from urllib import urlretrieve, urlencode
from cookielib import CookieJar
from os.path import join
import lxml.html
#from BeautifulSoup import BeautifulSoup, SoupStrainer
from pyimg import user_agent




values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)


def imagehaven_parse(link, basedir):
    # get every page linked from the imagehaven links
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

    # find the src attribute which contains the real link of imagehaven's images
    src_links = page.xpath("//img[@id='image']")

    imagehaven_src = [li.get('src', None) for li in src_links]

    imagehaven_split = re.split('img\.php\?id=', link) # remove the unneeded parts
    imagehaven_split2 = re.split('\.\/', imagehaven_src[0]) 

    try:
        # make up the real image url
        download_url = str(imagehaven_split[0]) + str(imagehaven_split2[1])
    except IndexError:
        # if we get an IndexError just continue (it may means that the image
        # can't be downloaded from the server or there is a host's glitch
        pass

    # generate just the filename of the image to be locally saved
    save_extension = re.split('\./images/[0-9A-Za-z]+/[0-9A-Za-z]+/', imagehaven_src[0]) 
    savefile = join(basedir, str(save_extension[1]))
    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 
