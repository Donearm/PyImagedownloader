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
import lxml.html


def storeimgs_parse(link, basedir):

    # make the image url by a couple of substitution and then using a split
    # to dissect the url and add the 'i' needed before the image name
    download_url = re.sub('show', 'out', link)
    download_url = re.sub('\.html$', '', download_url)

    storeimgs_split = re.split('out.php/', download_url)

    download_url = storeimgs_split[0] + 'out.php/i' + storeimgs_split[1]

    # generate just the filename of the image to be locally saved
    save_extension = storeimgs_split[1]

    savefile = join(basedir, save_extension)
    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 
