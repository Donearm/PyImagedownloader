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


def imagebam_parse(link, basedir):
    # get every page linked from the imagebam links
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    try:
        page = lxml.html.fromstring(response)
    except lxml.etree.XMLSyntaxError as e:
        # most of the time we can simply ignore parsing errors
        pass

    # find the src attribute which contains the real link of imagebam's images
    src_links = page.xpath("//img[@onclick='scale(this);']")

    imagebam_src = [li.get('src', None) for li in src_links]

    # get the image name from the id tag
#    imagename = [li.get('id', None) for i in src_links]
    # or, better, from the Content-Disposition header
    imagename = connector.get_filename(imagebam_src[0])


    download_url = imagebam_src[0]

    try: 
        savefile = join(basedir, imagename)
    except UnicodeEncodeError:
        # catch files with strange characters in name
        savefile = join(basedir, imagename.encode("utf-8"))

    # finally save the image in the desidered directory
    try:
        urlretrieve(download_url, savefile) 
    except IOError as e:
        # image not loading, skipping it
        return

