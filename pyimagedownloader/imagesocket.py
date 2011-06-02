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
from urllib import urlretrieve, urlencode
from os.path import join
import lxml.html
from pyimg import user_agent
import http_connector


# values for age verification
values = { 'month': '01', 'day' : '1', 'year' : '1978', 'verifyAge' : 'Confirm'}
headers = { 'User-Agent' : user_agent }
data = urlencode(values, 1)

class ImagesocketParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()

    def give_age_verification_info(self):
        # supply the age verification informations before the first file

        # splitting the url to get only the file name
        filename = self.link.split('/')
        age_response = self.connector.post_request('http://www.imagesocket.com/warning/' + filename[-1], data, headers)


    def process_url(self, url):
        response = self.connector.reqhandler(url)
        
        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            return

        return page

    def imagesocket_get_image_src(self, page):
        src_links = page.xpath("//img[@id='thumb']")
        imagesocket_src = [li.get('src', None) for li in src_links]

        return imagesocket_src

    def imagesocket_save_image(self, src_list):
        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('images/', src_list[0])

            savefile = join(basedir, save_extension[-1])
            download_url = src_list[0]
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            return

    def parse(self):
        self.give_age_verification_info()

        self.page = self.process_url(self.link)
        if self.page is None:
            # image was not found, exit
            return

        self.imagesocket_src = self.imagesocket_get_image_src(self.page)

        self.imagesocket_save_image(self.imagesocket_src)
