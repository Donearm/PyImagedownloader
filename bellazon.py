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
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import *
#from http_connector import get_request
import http_connector



# The regexp we'll need to find the link
#rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rBellazon = re.compile("href.*attach\&amp", re.IGNORECASE)




def bellazon_parse(link):
    bellazon_list = []
    #bellazon_list.append(page.findAll('a', title=rJpgSrc))
    #bellazon_href = []
    #for li in bellazon_href:
    #    bellazon_href.append(li['href'])
    #    print li
    if rBellazon.search(str(link)):
        bellazon_list.append(link['href'])

        connector = HttpConnector()
        response = connector.get_request(link, headers)
