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



def shareapic_parse(link, basedir):
    # get every page linked from the shareapic links
    connector = http_connector.Connector()
    try:
        response = connector.reqhandler(link)

        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            return

        # find the src attribute which contains the real link of shareapic's images
        src_links = page.xpath("//img[@title='Click to zoom! ::']")
        shareapic_fullsize = []
        for li in src_links:
            fullsize_li = re.sub(r"images([0-9])", r"fullsize\1", li.get('src', None))
            #fullsize_li = re.sub(r"images([0-9])", r"fullsize\1", li['src'])
            shareapic_fullsize.append(fullsize_li) # add all the src part to a list

        download_url = shareapic_fullsize[0]
        # generate just the filename of the image to be locally saved
        save_extension = re.split('fullsize[0-9]', shareapic_fullsize[0]) 
        savefile = join(basedir, str(save_extension[1]))
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile)
    except:
        print("An image couldn't be downloaded")
        return
