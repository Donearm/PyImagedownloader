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
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import *


# The regexp we'll need to find the link
#rUpmyphoto = re.compile("http://www\.upmyphoto\.com/img", re.IGNORECASE)


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def upmyphoto_parse(link):
    upmyphoto_list = [] # the list that will contain the href tags
    #upmyphoto_list.append(link['href'])
    upmyphoto_list.append(link)
    for i in upmyphoto_list:
        # get every page linked from the upmyphoto links
        request = urllib2.Request(i, data, headers)
        try: 
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break

        image_page = response.read()
        #page_soup = BeautifulSoup(image_page)
        page = lxml.html.fromstring(image_page)

        # find the src attribute which contains the real link of upmyphoto's images
        #src_links = page_soup.findAll('img', src=rUpmyphoto)
        src_links = page.xpath("//img[@id='image']")

        upmyphoto_src = [li.get('src', None) for li in src_links]

        # generate just the filename of the image to be locally saved
        save_extension = re.split('/img/dir[0-9]+/(loc[0-9]+/)?', upmyphoto_src[0])
        savefile = basedir + str(save_extension[-1])

        download_url = upmyphoto_src[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
