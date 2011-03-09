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
from urllib import urlretrieve
from os.path import join
import lxml.html
import http_connector

class ImagehavenParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            self.page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            return

        return self.page

    def imagehaven_get_image_splits_and_name(self, page):
        # find the src attribute which contains the real url
        src_links = page.xpath("//img[@id='image']")

        imagehaven_src = [li.get('src', None) for li in src_links]

        # remove unneeded parts
        imagehaven_split = re.split('img\.php\?id=', self.link)
        imagehaven_split2 = re.split('\.\/', imagehaven_src[0])

        # generate just the filename of the image to be locally saved
        imagename = re.split('\./images/[0-9A-Za-z]+/[0-9A-Za-z]+/', imagehaven_src[0])

        return imagehaven_split, imagehaven_split2, imagename

    def imaghaven_save_image(self, split1, split2, imagename):
        try:
            # make up the real image url
            download_url = str(split1[0]) + str(split2[1])
            savefile = join(self.basedir, str(imagename[1]))
        except IndexError:
            # if we get an IndexError just continue (it may means that the image
            # can't be downloaded from the server or there is a host's glitch
            pass

        urlretrieve(download_url, savefile)

    def parse(self):
        self.page = self.process_url(self.link)

        self.imagehaven_split1, self.imagehaven_split2, self.imagename = self.imagehaven_get_image_splits_and_name(self.page)

        self.imagehaven_save_image(self.imagehaven_split1, self.imagehaven_split2, self.imagename)
