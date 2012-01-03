#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2012, Gianluca Fiore
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

class SkinsbeParse():

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

    def skinsbe_get_image_src(self, page):
        # find the src attribute which contains the real link of skinsbe's images
        src_links = page.xpath("//img[@id='wallpaper_image']")

        skinsbe_src = [li.get('src', None) for li in src_links]

        return skinsbe_src

    def skinsbe_save_image(self, src_list):
        # generate just the filename of the image to be locally saved
        save_extension = re.sub("^.*[0-9]\/", '', src_list[0])
        savefile = join(self.basedir, save_extension)

        download_url = src_list[0]
        # finally save the image in the desidered directory
        try:
            urlretrieve(download_url, savefile) 
        except :
            return

    def parse(self):
        self.page = self.process_url(self.link)

        self.skinsbe_src = self.skinsbe_get_image_src(self.page)

        self.skinsbe_save_image(self.skinsbe_src)
