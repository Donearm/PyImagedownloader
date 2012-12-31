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
from os.path import join
import random
import lxml.html
import logging
import http_connector


class PostimageParse():

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

    def postimage_get_image_src(self, page):
        # some images on postimage are embedded, check for <a><img> first
        src_links = page.xpath("//center/a[@href]/img[@alt]")
        if len(src_links) == 0:
            self.logger.debug("(%s) first xpath query didn't find anything" % self.link)
            src_links = page.xpath("//center/img[@alt]")

        postimage_src = [li.get('src', None) for li in src_links]
        postimage_alt = [li.get('alt', None) for li in src_links]

        return postimage_src

    def postimage_save_image(self, src_list):
        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('/[a-z0-9]+/', src_list[0])

            randnumber = random.randint(1, 999)
            savefile = join(self.basedir, str(randnumber) + '-' + save_extension[-1])
            download_url = src_list[0]


            # finally save the image on the desidered directory
            # I'm using http_connector function to make use of its opener,
            # a simple urllib2.Request doesn't set the desidered User-Agent
            # header (the first request is ok without an opener)
            downreq = self.connector.reqhandler(download_url)
            with open(savefile, 'wb') as f:
                f.write(downreq)
        except IndexError as e:
            self.logger.error("IndexError in %s" % src_list)
            return

    def parse(self):
        self.page = self.process_url(self.link)

        self.postimage_src = self.postimage_get_image_src(self.page)

        self.postimage_save_image(self.postimage_src)
