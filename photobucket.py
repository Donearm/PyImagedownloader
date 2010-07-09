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
import urllib2
from urllib import urlencode, urlretrieve
import lxml.html
from pyimg import *



# values for age verification
values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def photobucket_parse(link):
    try:
        # generate just the filename of the image to be locally saved
        save_extension = re.split('/', link)

        savefile = basedir + save_extension[-1]
        download_url = link
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
    except IndexError:
        return




