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

class UppixParse():

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

    def uppix_get_image_src(self, page):
        # find the src attribute which contains the real link of uppix's images
        src_links = page.xpath("//img[@id='dpic']")

        uppix_src = [li.get('src', None) for li in src_links]

        return uppix_src

    def uppix_save_image(self, src_list):
        # generate just the filename of the image to be locally saved
        save_extension = re.sub('S[0-9]+/', '',  src_list[0]) 
        uppix_sub = re.sub('Viewer[a-zA-Z]\.php\?file=', '', self.link)
        savefile = join(self.basedir, save_extension)
        # finally save the image on the desidered directory
        urlretrieve(uppix_sub, savefile) 

    def parse(self):
        self.page = self.process_url(self.link)

        self.uppix_src = self.uppix_get_image_src(self.page)

        self.uppix_save_image(self.uppix_src)
