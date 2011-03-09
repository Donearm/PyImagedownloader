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
import lxml.html
import http_connector


class PostimageParse():

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

    def postimage_get_image_src(self, page):
        # Little trick: check if we have an img with an height; that would mean
        # the image is already fullsized. If there is no height, the image is
        # resized and we act accordingly
        height_present = page.xpath("//img[@height]")
        if height_present:
            src_links = page.xpath("//center/img")
            postimage_src = [li.get('src', None) for li in src_links]
            postimage_alt = [li.get('alt', None) for li in src_links]
        else:
            alt_links = page.xpath("//center/a[@href]/img[@alt]")
            postimage_alt = [li.get('alt', None) for li in alt_links]
            postimage_src = [li.get('src', None) for li in alt_links]

        return postimage_src

    def postimage_save_image(self, src_list):
        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('/[a-z0-9]+/', src_list[0])

            savefile = join(self.basedir, save_extension[-1])
            download_url = src_list[0]

            # finally save the image on the desidered directory
            # I'm using http_connector function to make use of its opener,
            # a simple urllib2.Request doesn't set the desidered User-Agent
            # header (the first request is ok without an opener)
            downreq = self.connector.reqhandler(download_url)
            with open(savefile, 'wb') as f:
                f.write(downreq)
        except IndexError:
            return

    def parse(self):
        self.page = self.process_url(self.link)

        self.postimage_src = self.postimage_get_image_src(self.page)

        self.postimage_save_image(self.postimage_src)
