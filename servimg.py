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

from os.path import join
from urllib import urlretrieve
import lxml.html
import http_connector


def servimg_parse(link, basedir):
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    page = lxml.html.fromstring(response)

    src_links = page.xpath("//p[@id='picture']/img")

    servimg_src = [li.get('src', None) for li in src_links]

    try:
        save_extension = connector.get_filename(servimg_src[0], '/')
        download_url = servimg_src[0]
        savefile = join(basedir, str(save_extension[-1]))
    except IndexError:
        return

    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 

