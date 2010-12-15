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
import http_connector
from pyimg import user_agent



values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def postimage_parse(link, basedir):
    request = urllib2.Request(link, data, headers)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        if e.code == 405:
            request = urllib2.Request(link)
            try:
                response = urllib2.urlopen(request)
            except:
                print("An image couldn't be downloaded")
                return
        else:
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
         postimage_src = [li.get('src', None) for li in alt_links]


    try:
        # generate just the filename of the image to be locally saved
        save_extension = re.split('/[a-z0-9]+/', postimage_src[0])

        savefile = join(basedir, save_extension[-1])
        download_url = postimage_src[0]

        # finally save the image on the desidered directory
        # I'm using http_connector function to make use of its opener,
        # a simple urllib2.Request doesn't set the desidered User-Agent
        # header (the first request is ok without an opener)
        downreq = http_connector.connector(download_url)
        with open(savefile, 'wb') as f:
            f.write(downreq)
    except IndexError:
        return
