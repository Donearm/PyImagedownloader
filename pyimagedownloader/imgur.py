#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2011, Gianluca Fiore
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
from os.path import join
from urllib import urlretrieve
import lxml.html
import http_connector

rSrc = re.compile("http://[a-z]+\.imgur\.com/", re.IGNORECASE)

class ImgurParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            return

        return page

    def imgur_get_image_src(self, page):

        if re.match(rSrc, self.link):
            # embedded images should already match rSrc
            imgur_src = [] # a list instead of string to be compatible with
                        # imgur_save_image
            imgur_src.append(self.link)
            return imgur_src
        else:
            src_links = page.xpath('//img[@alt]')

            imgur_src = [li.get('src', None) for li in src_links]
            # we need only images matching rSrc
            imgur_src = [s for s in imgur_src if re.match(rSrc, s)]

            return imgur_src

    def imgur_save_image(self, src_list):
        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('/', src_list[0])

            savefile = join(self.basedir, save_extension[-1])
            download_url = src_list[0]
            urlretrieve(download_url, savefile)
        except IndexError:
            return

    def parse(self):
        self.page = self.process_url(self.link)

        self.imgur_src = self.imgur_get_image_src(self.page)

        self.imgur_save_image(self.imgur_src)
