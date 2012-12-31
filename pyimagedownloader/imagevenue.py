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
#
# to find the page with streamate ads
RRedirects = re.compile("uploadimg\-streamate\.php", re.IGNORECASE)
# to find generical redirects
RRedirects2 = re.compile("Continue To Your Image", re.IGNORECASE)
# to find the url of the imagevenue's countdown
RRedirects3 = re.compile("tempfull-default\.php", re.IGNORECASE) 

class ImagevenueParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')
        # once we had 2 different functions for imagevenue's images coming from 
        # paid hosts like usercash; now it's not needed anymore so 
        # imagevenue_embed is just another name for parse()
        self.imagevenue_embed = self.parse()

    def process_url(self, url):
        response = self.connector.reqhandler(url)
        # if there are ads on the page, resubmit the link to the parser
        if re.search(RRedirects, response):
            self.parse(self.link, self.basedir)
            return
        elif re.search(RRedirects2, response):
            self.parse(self.link)
            return

        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            self.logger.error("XMLSyntaxError at %s" % url)
            return

        return page

    def imagevenue_get_image_src_and_split(self, page):
        # find the src attribute which contains the real link of imagevenue's
        # images
        src_links = page.xpath("//img[@id='thepic']")

        imagevenue_src = [li.get('src', None) for li in src_links]

        # remove unneeded parts
        imagevenue_split = re.split('img.php\?(loc=loc[0-9]{,3}&)?image=', self.link)

        return imagevenue_src, imagevenue_split

    def imagevenue_save_image(self, src_list, split):
        try:
            # make up the real image url
            download_url = str(split[0]) + str(src_list[0])
        except IndexError:
            # if we get an IndexError just continue (it may means that the image
            # can't be downloaded from the server or there is a host's glitch
            self.logger.warning("IndexError in %s or %s" % (split, src_list))
            pass

        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('([0-9a-zA-Z]+-[0-9]+/)?loc[0-9]{,4}/', src_list[0])
            savefile = join(self.basedir, str(save_extension[-1]))

            if savefile.endswith('.'):
                # add the extension for images without it
                savefile = savefile + 'jpg'
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            self.logger.error("IndexError in %s" % src_list)
            return

    def parse(self):
        self.page = self.process_url(self.link)

        self.imagevenue_src, self.imagevenue_split = self.imagevenue_get_image_src_and_split(self.page)

        self.imagevenue_save_image(self.imagevenue_src, self.imagevenue_split)
