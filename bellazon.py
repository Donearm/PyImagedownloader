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
from os.path import join
from urllib import urlretrieve, urlencode
import urllib2
import lxml.html
import http_connector
from pyimg import user_agent


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

class BellazonConnector(http_connector.Connector):
    """Modified Connector class to extract filename from Content-Disposition response header"""
    def __init__(self):
        http_connector.Connector.__init__(self)
        self.values = {}
        self.headers = { 'User-Agent' : user_agent }
        self.data = urlencode(self.values)

    def get_request(self, url):
        self.request = urllib2.Request(url)
        try:
            self.response = urllib2.urlopen(self.request)
            try:
                self.filename = self.response.headers['Content-Disposition'].split('=')[1]
                # remove single or double quotes from the filename
                if self.filename[0] == '"' or self.filename[0] == "'":
                    self.filename = self.filename[1:-1]
                return self.filename
            except:
                # no Content-Disposition header, make filename from url
                self.filename = re.split('id=', url)
                return self.filename
        except:
            pass


def bellazon_parse(link, basedir):
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    page = lxml.html.fromstring(response)

    src_links = page.xpath("//img[@id='thepic']")

    bellazon_src = [li.get('src', None) for li in src_links]

    # make a GET request to know the image filename
    bConnector = BellazonConnector()
    try:
        save_extension = bConnector.get_request(bellazon_src[0])
        download_url = bellazon_src[0]
        savefile = join(basedir, str(save_extension))
    except IndexError:
        return

    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 

