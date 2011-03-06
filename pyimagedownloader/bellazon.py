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

from os.path import join
from urllib import urlretrieve
import lxml.html
import http_connector

class BellazonParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.page = ''
        self.connector = http_connector.Connector()

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            self.page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            return

        return self.page

    def bellazon_get_image_src(self, page):
        src_links = page.xpath("//img[@id='thepic']")

        bellazon_src = [li.get('src', None) for li in src_links]

        return bellazon_src

    def bellazon_save_image(self, src_list):
        try:
            save_extension = self.connector.get_filename(src_list[0], 'id=')
            download_url = src_list[0]
            savefile = join(self.basedir, str(save_extension))
        except IndexError:
            return

        urlretrieve(download_url, savefile)

    def bellazon_parse(self):
        self.page = self.process_url(self.link)

        self.bellazon_src = self.bellazon_get_image_src(self.page)

        self.bellazon_save_image(self.bellazon_src)



def bellazon_parse(link, basedir):
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    try:
        page = lxml.html.fromstring(response)
    except lxml.etree.XMLSyntaxError as e:
        # most of the time we can simply ignore parsing errors
        return

    src_links = page.xpath("//img[@id='thepic']")

    bellazon_src = [li.get('src', None) for li in src_links]

    try:
        save_extension = connector.get_filename(bellazon_src[0], 'id=')
        download_url = bellazon_src[0]
        savefile = join(basedir, str(save_extension))
    except IndexError:
        return

    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 

