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

from os.path import join
from urllib import urlretrieve
import logging
import http_connector

class BellazonParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')

    def bellazon_save_image(self, src_url):
        try:
            save_extension = self.connector.get_filename(src_url, 'attach_id=')
            download_url = src_url
            print(save_extension)
            savefile = join(self.basedir, str(save_extension))
        except IndexError:
            self.logger.error("index error in %s")
            return

        urlretrieve(download_url, savefile)


    def parse(self):
        # Bellazon's images are just attachments to post, we already have the direct url
        self.bellazon_save_image(self.link)
