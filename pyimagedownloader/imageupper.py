#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2013, Gianluca Fiore
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

class ImageupperParse():

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

    def imageupper_get_image_src(self, page):
        src_links = page.xpath("//img[@id='img']")
        imageupper_src = [li.get('src', None) for li in src_links]

        return imageupper_src

    def imageupper_save_image(self, src_list):
        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('([a-z][0-9]+/)?[0-9]+/[0-9]+/', src_list[0])

            savefile = join(self.basedir, save_extension[-1])
            download_url = src_list[0]
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            self.logger.error("IndexError in %s" % src_list)
            return

    def parse(self):
        self.page = self.process_url(self.link)

        self.imageupper_src = self.imageupper_get_image_src(self.page)

        self.imageupper_save_image(self.imageupper_src)
