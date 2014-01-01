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

from os.path import join
from urllib import urlretrieve
import lxml.html
import logging
import http_connector


class ImagebossParse():

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

    def imageboss_get_image_src_and_name(self, page):
        src_links = page.xpath("//img[@id='thepic']")

        imageboss_src = [li.get('src', None) for li in src_links]
        
        imagename = self.connector.get_filename(imageboss_src[0], '[a-z0-9]+/')

        return imageboss_src, imagename

    def imageboss_save_image(self, src_list, imagename):

        try:
            save_extension = imagename
            download_url = src_list[0]
            savefile = join(self.basedir, str(save_extension[-1]))
        except IndexError:
            self.logger.error("IndexError in %s" % src_list)
            return

        urlretrieve(download_url, savefile)

    def parse(self):
        self.page = self.process_url(self.link)

        self.imageboss_src, self.imagename = self.imageboss_get_image_src_and_name(self.page)

        self.imageboss_save_image(self.imageboss_src, self.imagename)
