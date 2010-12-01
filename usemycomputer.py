#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008, Gianluca Fiore
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
from urllib import urlretrieve


def usemycomputer_parse(link, basedir):

    # no need to connect to the image's url, just rewrite the link to obtain
    # the uri of the image
    usemycomputer_split = re.split('show\.html\?i=\/', link)

    # split by '/' so to extract the image name
    imgname = re.split('/', usemycomputer_split[1])

    # generate just the filename of the image to be locally saved
    savefile = join(basedir, imgname[-1])

    download_url = usemycomputer_split[0] + usemycomputer_split[1]

    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 
