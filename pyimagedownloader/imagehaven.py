#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2011, Gianluca Fiore
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


def imagehaven_parse(link, basedir):
    # get every page linked from the imagehaven links
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    try:
        page = lxml.html.fromstring(response)
    except lxml.etree.XMLSyntaxError as e:
        # most of the time we can simply ignore parsing errors
        return

    # find the src attribute which contains the real link of imagehaven's images
    src_links = page.xpath("//img[@id='image']")

    imagehaven_src = [li.get('src', None) for li in src_links]

    # remove unneeded parts
    imagehaven_split = re.split('img\.php\?id=', link) 
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
