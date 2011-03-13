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
import http_connector


class BlogspotParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir

    def parse(self):
        # No need for blogspot to call lxml again, the link is
        # already the direct urls to the full image
        save_extension = re.split('/s1600/', self.link)
        savefile = join(self.basedir, str(save_extension[-1]))
        download_url = self.link
        urlretrieve(download_url, savefile)
