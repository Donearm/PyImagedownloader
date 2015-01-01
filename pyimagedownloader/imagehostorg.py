#!/usr/bin/env python2
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

class ImagehostorgParse():

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

    def imagehostorg_get_image_split_and_src(self, page):
        # find the src attribute which contains the real link of imagehostorg's 
        # images
        src_links = page.xpath("//div[@id='content']/img")

        imagehostorg_src = [li.get('src', None) for li in src_links]

        if not imagehostorg_src:
            # there is an ajax script to show the image and thus no src url
            # we use the original link to generate the image name and get the 
            # content
            imagehostorg_split = re.split('/', self.link)
            return imagehostorg_split
        else:
            # remove unneeded parts
            imagehostorg_split = re.split('/', imagehostorg_src[0])
            return imagehostorg_split, imagehostorg_src

    def imagehostorg_save_image(self, split, src_list=''):
        if not src_list:
            # if no src_list we use the original link and the split only
            download_url = re.sub('/view/', '', self.link)
            savefile = join(self.basedir, str(split[-1]))
            urlretrieve(download_url, savefile)
        else:
            download_url = src_list[0]
            savefile = join(self.basedir, str(split[-1]))
            urlretrieve(download_url, savefile)

    def parse(self):
        self.page = self.process_url(self.link)

        try:
            self.imagehostorg_split, self.imagehostorg_src = self.imagehostorg_get_image_split_and_src(self.page)
        except:
            self.logger.error("Couldn't get a split or a src string for %s" % self.link)
            return

        self.imagehostorg_save_image(self.imagehostorg_split, self.imagehostorg_src)
