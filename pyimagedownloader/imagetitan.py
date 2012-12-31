#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2013, Gianluca Fiore
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
import logging
import http_connector


# The regexp we'll need to find the link
RSrcImagetitan = re.compile("(img[0-9]{,2})(/[0-9A-Za-z]+/[0-9]+/)(.*[jpg|png|gif|jpeg])", re.IGNORECASE)

class ImagetitanParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            self.logger.error("XMLSyntaxError at %s" % url)
            return

        return page

    def imagetitan_get_image_match_group(self, page):
        # find the src attribute which contains the real link of imagetitan's images
        src_links = page.xpath("//td[@align='center']/img")
        if len(src_links) == 0:
            # newer images have a different html layout
            src_links = page.xpath("//img[@id='image']")

        imagetitan_src = [li.get('src', None) for li in src_links]

        # get the match group
        imgtitanmatch = re.match(RSrcImagetitan, imagetitan_src[0])

        imggrp = imgtitanmatch.group(1) # the 'img[0-9]' part of the url
        imgmiddle = imgtitanmatch.group(2) # the middle part
        imgname = imgtitanmatch.group(3) # the name of the image 

        return imggrp, imgmiddle, imgname

    def imagetitan_save_image(self, imggrp, imgmiddle, imgname):
        # generate just the filename of the image to be locally saved
        savefile = join(self.basedir, imgname)
        # generate the url of the image
        download_url = 'http://' + imggrp + '.imagetitan.com/' + imggrp + imgmiddle + imgname
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

    def parse(self):
        self.page = self.process_url(self.link)

        self.imggrp, self.imgmiddle, self.imgname = self.imagetitan_get_image_match_group(self.page)

        self.imagetitan_save_image(self.imggrp, self.imgmiddle, self.imgname)
