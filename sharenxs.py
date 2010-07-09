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


# The regexp we'll need to find the link
rSharenxsThumb = re.compile("http://(www\.)?sharenxs\.com/thumbnails/sf/", re.IGNORECASE)
# regexp matching a http:// url
rSharenxsUrl = re.compile("http://(www\.)?sharenxs\.com", re.IGNORECASE)
# Regexp matching a full-sized sharenxs src url
rSharenxsWz = re.compile("http://images\.sharenxs\.com/", re.IGNORECASE)


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def sharenxs_parse(link):
    request = urllib2.Request(link, data, headers)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        print("An image couldn't be downloaded")
        return
    except urllib2.URLError as e:
        print("An image couldn't be downloaded")
        return

    # get every page linked from the sharenxs links
    image_page = response.read()
    page = lxml.html.fromstring(image_page)
    # find the src attribute which contains the real link of sharenxs's images
    view_links = page.xpath("//center/table/tr/td/table/tr/td[@align='center']/a[@href]")

    sharenxs_view = [li.get('href', None) for li in view_links]
    
    # list comprehension to check that just the url will be fed to request2
    sharenxs_url = [u for u in sharenxs_view if rSharenxsUrl.search(u)]

    # opening the page with the full-sized image
    request2 = urllib2.Request(sharenxs_url[0], data, headers)
    try:
        response2 = urllib2.urlopen(request2)
    except urllib2.HTTPError as e:
        print("An image couldn't be downloaded")
        return
    except urllib2.URLError as e:
        print("An image couldn't be downloaded")
        return
    page2 = lxml.html.fromstring(response2.read())

    # find the image url
    src_links = page2.xpath('//img[@src]')

    # get all src urls in page
    sharenxs_src = [s.get('src', None) for s in src_links]

    # grab and check if we already have the full-sized image uri
    sharenxs_wz = [w for w in sharenxs_src if rSharenxsWz.search(w)]

    if len(sharenxs_wz) is not 0:
        try:
            save_extension = re.split('/', str(sharenxs_wz[0]))
            savefile = basedir + str(save_extension[-1])
            download_url = str(sharenxs_wz[0])
            urlretrieve(download_url, savefile)
        except IndexError:
            return
    else:
        # in the case we don't have the full-sized uri, we use the thumbnail
        # url to generate the image's url
        sharenxs_src = [s.get('src', None) for s in src_links if rSharenxsThumb.search(s.get('src', None))]
        try:
            # get the extension for the filename
            save_extension = re.split('nxs-', sharenxs_src[0])
            savefile = basedir + str(save_extension[1])
            # pick just the src's url part we need
            sharenxs_split = re.split('thumbnails/sf/', save_extension[0])
            # and compose the full-sized image url
            download_url = 'http://images.sharenxs.com/wz/' + sharenxs_split[1] + save_extension[1]
            urlretrieve(download_url, savefile)
        except IndexError:
            return
