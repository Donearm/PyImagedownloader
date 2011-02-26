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
from urllib import urlretrieve
from os.path import join


def imageban_parse(link, basedir):
    imageban_split = re.split('/', link) # get the image file name

    download_url = link

    # generate the save file name
    savefile = join(basedir, str(imageban_split[-1]))

    # finally save the image in the desidered directory
    urlretrieve(download_url, savefile) 

