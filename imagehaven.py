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
from urllib import urlretrieve, urlencode
from cookielib import CookieJar
import lxml.html
#from BeautifulSoup import BeautifulSoup, SoupStrainer
from pyimg import *



# The regexp we'll need to find the link
rSponsoredContent = re.compile("streamate\.com", re.IGNORECASE)
rSrcImagehaven = re.compile("\./images") # regexp for the src link



values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)


def imagehaven_parse(link):
    imagehaven_list = [] # the list that will contain the href tags
    #imagehaven_list.append(link['href'])
    imagehaven_list.append(link)
    for i in imagehaven_list:
        # get every page linked from the imagehaven links
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break
        image_page = response.read()

        if re.search(rSponsoredContent, image_page):
            # if there are ads on the page, resubmit the link to the parser
            imagehaven_parse(link)
            break

        #page_soup = BeautifulSoup(image_page)
        page = lxml.html.fromstring(image_page)

        # find the src attribute which contains the real link of imagehaven's images
        #src_links = page_soup.findAll('img', src=rSrcImagehaven)
        src_links = page.xpath("//img[@id='image']")
        imagehaven_src = []
        for li in src_links:
            #imagehaven_src.append(li['src']) # add all the src part to a list
            imagehaven_src.append(li.get('src', None))

        imagehaven_split = re.split('img\.php\?id=', i) # remove the unneeded parts
        imagehaven_split2 = re.split('\.\/', imagehaven_src[0]) 

        try:
            # make up the real image url
            download_url = str(imagehaven_split[0]) + str(imagehaven_split2[1])
        except IndexError:
            # if we get an IndexError just continue (it may means that the image
            # can't be downloaded from the server or there is a host's glitch
            continue

        # generate just the filename of the image to be locally saved
        save_extension = re.split('\./images/[0-9A-Za-z]+/[0-9A-Za-z]+/', imagehaven_src[0]) 
        savefile = basedir + str(save_extension[1])
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
