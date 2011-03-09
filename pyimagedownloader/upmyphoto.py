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

class UpmyphotoParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()

    def process_url(self, url):
        response = connector.reqhandler(url)

        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            return

        return page

    def upmyphoto_get_image_src(self, page):
        # find the src attribute which contains the real link of upmyphoto's images
        src_links = page.xpath("//img[@id='image']")

        upmyphoto_src = [li.get('src', None) for li in src_links]

        return upmyphoto_src
        
    def upmyphoto_save_image(self, src_list):
        # generate just the filename of the image to be locally saved
        # if this fails, it's possible that the image has been deleted
        try:
            save_extension = re.split('/img/dir[0-9]+/(loc[0-9]+/)?', src_list[0])
        except IndexError as e:
            return
        savefile = join(self.basedir, str(save_extension[-1]))
        download_url = src_list[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

    def parse(self):
        self.page = self.process_url(self.link)
        
        self.upmyphoto_src = self.upmyphoto_get_image_src(self.page)

        self.upmyphoto_save_image(self.upmyphoto_src)
