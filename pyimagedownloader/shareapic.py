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


class ShareapicParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')

    def process_url(self, url):
        try:
            response = self.connector.reqhandler(url)

            try:
                page = lxml.html.fromstring(response)
            except lxml.etree.XMLSyntaxError as e:
                # most of the time we can simply ignore parsing errors
                self.logger.error("XMLSyntaxError at %s" % url)
                return

            return page
        except:
            self.logger.warning("%s couldn't be downloader" % url)
#            print("An image couldn't be downloaded")
            return

    def shareapic_get_image_src(self, page):
        # find the src attribute which contains the real link of shareapic's
        # images
        src_links = page.xpath("//div[@id='bannerad']/a/img")

        shareapic_src = []
        for L in src_links:
            fullsize = re.sub(r"images([0-9])", r"fullsize\1", L.get('src', None))
            shareapic_src.append(fullsize)

        return shareapic_src

    def shareapic_save_image(self, src_list):
        download_url = src_list[0]
        # generate just the filename of the image to be locally saved
        save_extension = re.split('fullsize[0-9]/', src_list[0])
        savefile = join(self.basedir, str(save_extension[1]))
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile)

    def parse(self):
        self.page = self.process_url(self.link)

        self.shareapic_src = self.shareapic_get_image_src(self.page)

        self.shareapic_save_image(self.shareapic_src)
