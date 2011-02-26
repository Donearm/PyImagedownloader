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


def wordpress_parse(link, basedir):
    # urls of this kind are already the absolute ones of the image
    # Therefore:

    # grab the filename of the image
    save_extension = re.split('/[0-9]{,2}/', link)
    
    # generate the savefile
    # the split is needed to clean image names with added '?w=width&h=height' 
    # strings
    savefile = join(basedir, str(save_extension[-1]).split('?w=')[0])

    download_url = link

    # download the image
    urlretrieve(download_url, savefile)
