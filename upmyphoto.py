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


def upmyphoto_parse(link, basedir):
    # get every page linked from the upmyphoto links
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    page = lxml.html.fromstring(response)

    # find the src attribute which contains the real link of upmyphoto's images
    src_links = page.xpath("//img[@id='image']")

    upmyphoto_src = [li.get('src', None) for li in src_links]

    # generate just the filename of the image to be locally saved
    # if this fails, it's possible that the image has been deleted
    try:
        save_extension = re.split('/img/dir[0-9]+/(loc[0-9]+/)?', upmyphoto_src[0])
    except IndexError as e:
        return
    savefile = join(basedir, str(save_extension[-1]))

    download_url = upmyphoto_src[0]
    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 
