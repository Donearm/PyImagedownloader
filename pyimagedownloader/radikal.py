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

# the regexp to catch just the image we want
rSrcRadikal = re.compile('http://[a-z0-9]+\.radikal\.ru', re.IGNORECASE)

class RadikalParse():

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

    def radikal_get_image_src(self, page):
        # find the src attribute which contains the real url
        src_links = page.xpath("//img[@border]")

        radikal_src = [li.get('src', None) for li in src_links]
        # we need only image's src matching the regexp
        radikal_src = [s for s in radikal_src if re.match(rSrcRadikal, s)]

        return radikal_src

    def radikal_get_image_name(self, link):
        # generate just the filename of the image to be locally saved
        imagename = re.split('(/[a-zA-Z0-9]+)?/[a-zA-Z0-9]+/[a-zA-Z0-9]+/', link)

        return imagename

    def radikal_save_image(self, src, imagename):
        # check whether we have a src string or a list
        if isinstance(src, str):
            download_url = src
        else:
            download_url = src[0]

        if len(imagename) < 2:
            # don't try to download simple 'http://www.radikal.ru' urls
            return

        try:
            savefile = join(self.basedir, str(imagename[-1]))
            urlretrieve(download_url, savefile)
        except IndexError as e:
            self.logger.error("IndexError in %s" % imagename)
            pass

    def parse(self):
        if re.match(rSrcRadikal, self.link):
            # we already got the url of the image, get the image name and save it
            self.imagename = self.radikal_get_image_name(self.link)
            self.radikal_save_image(self.link, self.imagename)
        else:
            self.page = self.process_url(self.link)

            self.radikal_src = self.radikal_get_image_src(self.page)

            self.imagename = self.radikal_get_image_name(self.radikal_src[0])

            self.radikal_save_image(self.radikal_src, self.imagename)
