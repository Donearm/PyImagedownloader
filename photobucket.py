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


def photobucket_parse(link, basedir):
    try:
        # generate just the filename of the image to be locally saved
        save_extension = re.split('/', link)

        savefile = join(basedir, save_extension[-1])
        download_url = link
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
    except IndexError:
        return




