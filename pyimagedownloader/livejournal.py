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


class LivejournalParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir

    def livejournal_get_image_name(self, link):
        # generate just the filename of the image to be locally saved
        imagename = re.split('pic/', link)

        return imagename

    def livejournal_save_image(self, src, imagename):
        download_url = src.strip('/')
        try:
            savefile = join(self.basedir, str(imagename[-1].strip('/')) + '.jpg')
            urlretrieve(download_url, savefile)
        except IndexError:
            pass


    def parse(self):
        self.imagename = self.livejournal_get_image_name(self.link)

        self.livejournal_save_image(self.link, self.imagename)
