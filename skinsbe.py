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


def skinsbe_parse(link, basedir):
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    page = lxml.html.fromstring(response)


    # find the src attribute which contains the real link of skinsbe's images
    src_links = page.xpath("//img[@id='wallpaper_image']")

    skinsbe_src = [li.get('src', None) for li in src_links]

    # generate just the filename of the image to be locally saved
    save_extension = re.sub("^.*[0-9]\/", '', skinsbe_src[0])
    savefile = join(basedir, save_extension)

    download_url = skinsbe_src[0]
    # finally save the image in the desidered directory
    urlretrieve(download_url, savefile) 
