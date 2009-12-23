#!/usr/bin/env python
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
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import *


# The regexp we'll need to find the link
rSharenxsThumb = re.compile("http://sharenxs\.com/thumbnails/sf/", re.IGNORECASE)


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def sharenxs_parse(link):
    sharenxs_list = [] # the list that will contain the href tags
    #sharenxs_list.append(link['href'])
    sharenxs_list.append(link)
    for i in sharenxs_list:
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break
        # get every page linked from the sharenxs links
        image_page = response.read()
        #page_soup = BeautifulSoup(image_page)
        page = lxml.html.fromstring(image_page)
        # find the src attribute which contains the real link of sharenxs's images
        #src_links = page_soup.findAll('img', src=rSharenxsThumb)
        view_links = page.xpath("//div[@align='center']/a[@href]")
        sharenxs_view = []
        for li in view_links:
            #sharenxs_view.append(li['src']) # add all the src part to a list
            sharenxs_view.append(li.get('href', None))

        # opening the page with the full-sized image
        request2 = urllib2.Request(sharenxs_view[1], data, headers)
        try:
            response2 = urllib2.urlopen(request2)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break
        page2 = lxml.html.fromstring(response2.read())

        # find the image url
        src_links = page2.xpath('//img[@src]')
        sharenxs_src = []
        for s in src_links:
            # add the src link only if it matches the regexp (and thus is what
            # we are looking for
            if rSharenxsThumb.search(s.get('src', None)):
                sharenxs_src.append(s.get('src', None))
        try:
            # get the extension for the filename
            save_extension = re.split('nxs-', sharenxs_src[0])
            savefile = basedir + str(save_extension[1])
            # pick just the src's url part we need
            sharenxs_split = re.split('thumbnails/sf/', save_extension[0])
            # and compose the full-sized image url
            download_url = 'http://images.sharenxs.com/wz/' + sharenxs_split[1] + save_extension[1]
            urlretrieve(download_url, savefile)
        except IndexError:
            break
