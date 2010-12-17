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


def imageupper_parse(link, basedir):
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    page = lxml.html.fromstring(response)

    src_links = page.xpath("//img[@id='img']")
    imageupper_src = [li.get('src', None) for li in src_links]

    try:
        # generate just the filename of the image to be locally saved
        save_extension = re.split('[0-9]+/[0-9]+/', imageupper_src[0])

        savefile = join(basedir, save_extension[-1])
        download_url = imageupper_src[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
    except IndexError:
        return
