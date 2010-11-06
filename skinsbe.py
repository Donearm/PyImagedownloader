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
from urllib import urlretrieve, urlencode
from os.path import join
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import user_agent
import http_connector



values = {}
headers = { 'User-Agent' : user_agent, 'show_adult': '1' }
data = urlencode(values)

def skinsbe_parse(link, basedir):
    #request = urllib2.Request(link, data, headers)
    try:
# we use the connector from http_connector because it can handle cookies
# and we'll need them to store the affirmative answer to whether to show
# adult images or not
# Without cookies the program will stop at the first adult image found
        response = http_connector.connector(link)
    #    response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        print("An image couldn't be downloaded")
        return
    except urllib2.URLError as e:
        print("An image couldn't be downloaded")
        return


    image_page = response
    #page_soup = BeautifulSoup(image_page)
    page = lxml.html.fromstring(image_page)


    # find the src attribute which contains the real link of skinsbe's images
    #src_links = page_soup.findAll('img', id='wallpaper_image')
    src_links = page.xpath("//img[@id='wallpaper_image']")

    skinsbe_src = [li.get('src', None) for li in src_links]

    # generate just the filename of the image to be locally saved
    save_extension = re.sub("^.*[0-9]\/", '', skinsbe_src[0])
    savefile = join(basedir, save_extension)

    download_url = skinsbe_src[0]
    # finally save the image in the desidered directory
    urlretrieve(download_url, savefile) 
