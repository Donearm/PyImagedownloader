#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2014, Gianluca Fiore
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

class ImagehavenParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            self.page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            self.logger.error("XMLSyntaxError at %s" % url)
            return

        return self.page

    def imagehaven_get_image_split_and_src(self, page):
        # find the src attribute which contains the real url
        try:
            src_links = page.xpath("//img[@id='image']")
        except AttributeError as e:
            self.logger.error("Didn't find src tag with xpath query at %s" % self.link)
            # NoneType object? Exit
            return

        imagehaven_src = [li.get('src', None) for li in src_links]

        # remove unneeded parts
        imagehaven_split = re.split('img\.php\?id=', self.link)

        return imagehaven_split, imagehaven_src

    def imagehaven_save_image(self, split, srclist):
        try:
            # make up the real image url
            download_url = str(split[0]) + re.sub('\./images', 'images', srclist[0])
            savefile = join(self.basedir, split[-1])
            urlretrieve(download_url, savefile)
        except IndexError:
            # if we get an IndexError just continue (it may means that the image
            # can't be downloaded from the server or there is a host's glitch
            self.logger.debug("Skipping an IndexError on %s" % srclist[0])
            pass

    def parse(self):
        self.page = self.process_url(self.link)

        self.imagehaven_split, self.imagehaven_src = self.imagehaven_get_image_split_and_src(self.page)

        self.imagehaven_save_image(self.imagehaven_split, self.imagehaven_src)
