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
import urllib2
from urllib import urlencode, urlretrieve
from os.path import join
import random
import lxml.html
from pyimg import user_agent
import http_connector



# The split regexp
rImageshackSplit = '/img[0-9]{,3}/[0-9]+/'
# the 'a.imageshack.us' type url
rImageshackA = re.compile('a\.imageshack\.us/', re.IGNORECASE)
# the '/i/' type url
rImageshackI = re.compile('/i/', re.IGNORECASE)
# a partial url (without http://)
rImageshackPartial = re.compile('/img[0-9]{,3}/', re.IGNORECASE)


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

class ShackConnector(http_connector.Connector):
    """Modified Connector class to deal with 405 HTTP code from ImageShack"""
    def __init__(self, url):
        http_connector.Connector.__init__(self)
        self.values = {}
        self.headers = { 'User-Agent' : user_agent }
        self.data = urlencode(self.values)

        def post_request(self, url, data, headers):
            self.request = urllib2.Request(url, data, headers)
            try:
                self.response = urllib2.urlopen(self.request)
                return self.response
            except urllib2.HTTPError as e:
                if e.code == 405:
                    # we could be dealing with an url which is already the image url
                    # let's download it right away then
                    imageshack_download(rImageshackSplit, url, basedir)




def imageshack_parse(link, basedir):
    
    # check first if it's already the full url of the image
    if re.search(rImageshackSplit, link):
        imageshack_download(rImageshackSplit, link, basedir)

    connector = ShackConnector(link)
    response = connector.reqhandler(link)

    try:
        page = lxml.html.fromstring(response)
    except lxml.etree.XMLSyntaxError as e:
        return

    # find the src attribute which contains the real link of imageshack's images
    src_links = page.xpath("//img[@id='main_image']")

    imageshack_src = [li.get('src', None) for li in src_links]

    try:
        imageshack_download('my\.php\?', link, basedir, imageshack_src[0], 1)            
    except IndexError:
        return

def imageshack_download(regexp, url, basedir, src="", htmlpage=0):
    """downloader function for imageshack links. It needs a regexp for re.split
    and of course the url of an imageshack hosted image
    htmlpage is optional and it's to be enabled only for imageshack's pages
    containing an image (and not the direct source url)
    same for src, it's optional and only for those kind of pages"""

    # generate a random number; if not, the images will have the same save_extension[1]
    # and will overwrite each other   
    num = random.randrange(1,1000)

    # Check if is a "type a" url
    if rImageshackA.search(src):
        save_extension = re.split('img[0-9]+/[0-9]+/', src)
        download_url = src
        savefile = join(basedir, str(num) + str(save_extension[-1]))
    # is it a partial url (without http://) ?
    elif rImageshackPartial.search(src):
        save_extension = re.split('/img[0-9]+/[0-9]+/', src)
        # extract the first "imgXXX" part, we'll need it to reconstruct the full url
        imgxxx = re.split('/', src)
        download_url = 'http://' + imgxxx[1] + '.imageshack.us' + src
        savefile = join(basedir, str(num) + str(save_extension[-1]))
    else:
        # generate just the filename of the image to be locally saved
        save_extension = re.split(regexp, url)
        if htmlpage == 1:
            download_url = save_extension[0] + src
            savefile = join(basedir, str(num) + str(save_extension[1]).replace('/', ''))
        else:
            download_url = url
            savefile = join(basedir, str(save_extension[1]))

    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 
