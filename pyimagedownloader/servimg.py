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

from os.path import join
from urllib import urlretrieve
import lxml.html
import logging
import http_connector


class ServimgParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        page = lxml.html.fromstring(response)

        return page

    def servimg_get_image_src_and_name(self, page):
        src_links = page.xpath("//p[@id='picture']/img")

        servimg_src = [li.get('src', None) for li in src_links]

        try:
            imagename = self.connector.get_filename(servimg_src[0], '/')
        except IndexError:
            self.logger.error("IndexError in %s" % servimg_src)
            return

        return servimg_src, imagename

    def servimg_save_image(self, src_list, imagename):
        save_extension = imagename
        download_url = src_list[0]
        savefile = join(self.basedir, str(save_extension[-1]))

        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

    def parse(self):
        self.page = self.process_url(self.link)

        self.servimg_src, self.imagename = self.servimg_get_image_src_and_name(self.page)

        self.servimg_save_image(self.servimg_src, self.imagename)
