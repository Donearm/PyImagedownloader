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

class WordpressParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir

    def parse(self):
        # urls of this kind are already the absolute ones of the image

        # Therefore:
        # grab the filename of the image
        save_extension = re.split('/', self.link)
        
        # generate the savefile
        # the split is needed to clean image names with added 
        # '?w=width&h=height' strings
        savefile = join(self.basedir, str(save_extension[-1]).split('?w=')[0])

        download_url = self.link

        # download the image
        urlretrieve(download_url, savefile)
