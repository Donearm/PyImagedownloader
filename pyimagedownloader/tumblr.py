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

class TumblrParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir

    def tumblr_get_image_split(self):
        tumblr_split = re.split('/', self.link)

        return tumblr_split


    def tumblr_save_image(self, split):

        download_url = self.link
        savefile = join(self.basedir, split[-1])
        urlretrieve(download_url, savefile)

    def parse(self):
        self.tumblr_split = self.tumblr_get_image_split()

        self.tumblr_save_image(self.tumblr_split)
