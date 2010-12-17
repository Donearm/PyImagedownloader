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
from urllib import urlretrieve
from os.path import join
import lxml.html
import http_connector


# The regexp we'll need to find the link
rSharenxsThumb = re.compile("http://((www|cache)\.)?sharenxs\.com/thumbnails/sf/", re.IGNORECASE)
# regexp matching a http:// url
rSharenxsUrl = re.compile("http://((www|cache)\.)?sharenxs\.com", re.IGNORECASE)
# Regexp matching a full-sized sharenxs src url
rSharenxsWz = re.compile("http://((www|cache)\.)?sharenxs\.com/images/wz", re.IGNORECASE)

def sharenxs_parse(link, basedir):
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    page = lxml.html.fromstring(response)
    # find the src attribute which contains the real link of sharenxs's images
    view_links = page.xpath("//center/table/tr/td/table/tr/td[@align='center']/a[@href]")

    sharenxs_view = [li.get('href', None) for li in view_links]
    
    # list comprehension to check that just the url will be fed to request2
    sharenxs_url = [u for u in sharenxs_view if rSharenxsUrl.search(u)]

    if len(sharenxs_url) is 0:
        # perhaps we are already on the page with the full image
        view_links = page.xpath("//center/table/tr/td[@align='center']/a[@href]/img")
        src_link = [li.get('src', None) for li in view_links]
        try:
            save_extension = re.split('/', str(src_link[0]))
            savefile = join(basedir, str(save_extension[-1]))
            download_url = str(src_link[0])
            urlretrieve(download_url, savefile)
            return
        except IndexError:
            return

    # opening the page with the full-sized image
    response2 = connector.reqhandler(sharenxs_url[0])

    page2 = lxml.html.fromstring(response2)

    # find the image url
    src_links = page2.xpath('//img[@src]')

    # get all src urls in page
    sharenxs_src = [s.get('src', None) for s in src_links]

    # grab and check if we already have the full-sized image uri
    sharenxs_wz = [w for w in sharenxs_src if rSharenxsWz.search(w)]

    if len(sharenxs_wz) is not 0:
        try:
            save_extension = re.split('/', str(sharenxs_wz[0]))
            savefile = join(basedir, str(save_extension[-1]))
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
            savefile = join(basedir, str(save_extension[1]))
            # pick just the src's url part we need
            sharenxs_split = re.split('thumbnails/sf/', save_extension[0])
            # and compose the full-sized image url
            download_url = 'http://cache.sharenxs.com/images/wz/' + sharenxs_split[1] + save_extension[1]
            urlretrieve(download_url, savefile)
        except IndexError:
            return
