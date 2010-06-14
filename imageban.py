#!/usr/bin/env python
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
from urllib import urlencode, urlretrieve 
import lxml.html
from pyimg import *


values = {}
headers = {'User-Agent': user_agent}
data = urlencode(values)


def imageban_parse(link):
    imageban_list = [] # the list that will contain the href tags
    imageban_list.append(link)
    for i in imageban_list:


        imageban_split = re.split('/', i) # get the image file name

        download_url = i

        # generate the save file name
        savefile = basedir + str(imageban_split[-1])

        # finally save the image in the desidered directory
        urlretrieve(download_url, savefile) 
