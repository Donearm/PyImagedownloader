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
from cookielib import CookieJar
from socket import setdefaulttimeout
from urllib import urlencode
from BeautifulSoup import BeautifulSoup, SoupStrainer



# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
#rBellazon = re.compile('href=\"?http://www\.bellazon\.com/http://www\.bellazon\.com/main/index\.php\?act=attach', re.IGNORECASE)
#rBellazon = re.compile("http://www\.bellazon\.com/", re.IGNORECASE)
rBellazon = re.compile("href.*attach\&amp", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Some variables for the connection
values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009021410 Firefox/3.0.6'
headers = { 'User-Agent' : user_agent }
# Change the timeout
timeout = 60
setdefaulttimeout(timeout)
# prepare the cookies handler
cj = CookieJar()



def bellazon_parse(link):
    bellazon_list = []
    #bellazon_list.append(page.findAll('a', title=rJpgSrc))
    #bellazon_href = []
    #for li in bellazon_href:
    #    bellazon_href.append(li['href'])
    #    print li
    if rBellazon.search(str(link)):
        bellazon_list.append(link['href'])
        print(link)

        # Open and read the page contents
        data = urlencode(values)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        request = urllib2.Request(link, data, headers)

        try:
            respone = urllib2.urlopen(request)
        except HTTPError as e:
            print(e.code)
            print(e.reason)
