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
from os.path import join
from urllib import urlretrieve

class UsemycomputerParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir

    def usemycomputer_get_image_split_and_name(self, url):
        # no need to connect to the image's url, just rewrite the link to obtain
        # the uri of the image
        usemycomputer_split = re.split('i=', url)

        # split by '/' so to extract the image name
        imagename = re.split('/', usemycomputer_split[1])

        return usemycomputer_split, imagename

    def usemycomputer_save_image(self, split, imagename):
        # generate just the filename of the image to be locally saved
        savefile = join(self.basedir, imagename[-1])

        download_url = 'http://usemycomputer.com/' + split[1]

        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

    def parse(self):
        self.usemycomputer_split, self.imagename = self.usemycomputer_get_image_split_and_name(self.link)

        self.usemycomputer_save_image(self.usemycomputer_split, self.imagename)
