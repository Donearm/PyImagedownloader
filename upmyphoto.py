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


# The regexp we'll need to find the link
#rUpmyphoto = re.compile("http://www\.upmyphoto\.com/img", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2b4) Gecko/20091202 Firefox/3.6b4'
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
        upmyphoto_src = []
        for li in src_links:
            #upmyphoto_src.append(li['src']) # add all the src part to a list
            upmyphoto_src.append(li.get('src', None))


        # generate just the filename of the image to be locally saved
        save_extension = re.split('/img/', upmyphoto_src[0])
        savefile = basedir + str(save_extension[1])

        download_url = upmyphoto_src[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
