#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2015, Gianluca Fiore
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
import logging
import http_connector

class TurboimagehostParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            self.logger.error("XMLSyntaxError at %s" % url)
            return

        return page

    def turboimagehost_get_image_src(self, page):
        # find the src attribute which contains the real link of turboimagehost's 
        # images
        src_links = page.xpath("//img[@id='imageid']")

        turboimagehost_src = [li.get('src', None) for li in src_links]

        return turboimagehost_src

    def turboimagehost_save_image(self, src_list):
        # get just the filename
        turboimagehost_split = re.split('[0-9A-Za-z]+/', src_list[0])

        download_url = src_list[0]

        try: 
            # generate just the filename of the image to be locally saved
            savefile = join(self.basedir, str(turboimagehost_split[-1]))
        except UnicodeEncodeError:
            # catch files with strange characters in name
            savefile = join(self.basedir, str(turboimagehost_split[-1].encode("utf-8")))

        # finally save the image in the desidered directory
        urlretrieve(download_url, savefile) 

    def parse(self):
        self.page = self.process_url(self.link)

        self.turboimagehost_src = self.turboimagehost_get_image_src(self.page)

        self.turboimagehost_save_image(self.turboimagehost_src)
