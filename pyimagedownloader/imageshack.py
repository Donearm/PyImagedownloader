#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2014, Gianluca Fiore
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
from os.path import join
import random
import lxml.html
import logging
from pyimg import user_agent
import http_connector


# The split regexp
RImageshackSplit = '/img[0-9]{,3}/[0-9]+/'
# the 'a.imageshack.us' type url
RImageshackA = re.compile('a\.imageshack\.us/', re.IGNORECASE)
# the '/i/' type url
RImageshackI = re.compile('/i/', re.IGNORECASE)
# a partial url (without http://)
RImageshackPartial = re.compile('^[a-z0-9]\.imageshack\.(us|com)/img[0-9]{,3}/', re.IGNORECASE)
# a "desmond" url
RImageshackDesmond = re.compile('desmond\.imageshack\.(us|com)/', re.IGNORECASE)


values = {}
headers = {'User-Agent' : user_agent}
data = urlencode(values)

class ShackConnector(http_connector.Connector):
    """Modified Connector class to deal with 405 HTTP code from ImageShack"""
    def __init__(self, url):
        http_connector.Connector.__init__(self)
        self.values = {}
        self.headers = {'User-Agent' : user_agent}
        self.data = urlencode(self.values)

    def post_request(self, url, data, headers):
        self.request = urllib2.Request(url, data, headers)
        try:
            self.response = urllib2.urlopen(self.request)
            return self.response
        except urllib2.HTTPError as e:
            if e.code == 405:
                # we could be dealing with an url which is already the
                # image url let's download it right away then
                imageshack_download(RImageshackSplit, url, basedir)



class ImageshackParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = ShackConnector(self.link)
        self.logger = logging.getLogger('pyimagedownloader')

    def process_url(self, url):
        response = self.connector.reqhandler(url)
        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            self.logger.error("XMLSyntaxError at %s" % url)
            return

        return page

    def imageshack_get_image_src(self, page):
        src_links = page.xpath("//img[@id='main_image']")
        
        imageshack_src = [li.get('src', None) for li in src_links]

        return imageshack_src

    def imageshack_save_image(self, regexp, link, basedir, src=''):
        """downloader function for imageshack links. It needs a regexp for 
        re.split and of course the url of an imageshack hosted image"""

        # generate a random number; if not, the images will have the same
        # save_extension[1] and will overwrite each other   
        num = random.randrange(1, 1000)

        # there is not src at all? Then it's an embedded image
        if len(src) == 0:
            save_extension = re.split('img[0-9]+/[0-9]+/', link)
            download_url = link
            savefile = join(basedir, str(num) + str(save_extension[-1]))
        else:
            # Check if is a "type a" url 
            if RImageshackA.search(src[0]):
                save_extension = re.split('img[0-9]+/[0-9]+/', src[0])
                download_url = src[0]
                savefile = join(basedir, str(num) + str(save_extension[-1]))
            # is it a partial url (without http://) ?
            elif RImageshackPartial.search(src[0]):
                save_extension = re.split('/img[0-9]+/[0-9]+/', src[0])
                # extract the first "imgXXX" part, we'll need it to reconstruct the
                # full url
                imgxxx = re.split('/', src[0])
                download_url = 'http://' + imgxxx[1] + '.imageshack.us' + src[0]
                savefile = join(basedir, str(num) + str(save_extension[-1]))
            elif RImageshackDesmond.search(src[0]):
                save_extension = re.split('&', src[0])
                download_url = src[0]
                savefile = join(basedir, str(num) + str(re.split('=', save_extension[1])[-1]))

            else:
                # generate just the filename of the image to be locally saved
                save_extension = re.split(regexp, src[0])
                download_url = src[0]
                savefile = join(basedir, str(num) +  str(save_extension[1]))

        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

    def parse(self):
        # check first if we already have the url of the image
        if re.search(RImageshackSplit, self.link):
            self.imageshack_save_image(RImageshackSplit, self.link, self.basedir)

        self.page = self.process_url(self.link)
        
        try:
            self.imageshack_src = self.imageshack_get_image_src(self.page)
        except:
            self.logger.error("Couldn't get a src tag from %s" % self.link)
            return

        try:
            self.imageshack_save_image(RImageshackSplit, self.link, self.basedir, self.imageshack_src)
        except IndexError:
            return
