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

rThumbs = re.compile("_thumb\.", re.IGNORECASE)

class ImageepParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir

    def imageep_save_image(self, link):
        # with imageep.com we don't need to parse the page; therefore
        # generate just the filename of the image to be locally saved
        save_extension = re.split('viewer\.php\?file=', link)
        try:
            download_url = save_extension[0] + 'images/' + save_extension[-1]
            savefile = join(self.basedir, save_extension[-1])

            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IOError:
            # perhaps an embedded url? Just download it then

            # exclude thumbnails
            if re.search(rThumbs, link):
                return
            else:
                try:
                    save_extension = re.split('images/', link)

                    download_url = link
                    savefile = join(self.basedir, save_extension[-1])

                    urlretrieve(download_url, savefile)
                except IOError:
                    return

    def parse(self):
        self.imageep_save_image(self.link)
