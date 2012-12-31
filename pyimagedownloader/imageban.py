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
from urllib import urlretrieve
from os.path import join

class ImagebanParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir

    def parse(self):
        # get the image file name
        imageban_split = re.split('/', self.link)

        download_url = self.link

        # generate the save file name
        savefile = join(self.basedir, str(imageban_split[-1]))

        # finally save the image in the desidered directory
        urlretrieve(download_url, savefile)

