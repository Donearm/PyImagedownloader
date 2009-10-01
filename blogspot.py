#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
"""
"""
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__email__ = "forod.g@gmail.com"

import re
import urllib2
from urllib import urlencode, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer


# Regexp needed for the src links
rSrcBlogspot = re.compile('http://[0-9]\.bp\.blogspot\.com/.*\.(jpg|jpeg|gif|png)', re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def blogspot_parse(link):
    blogspot_list = [] # the list that will contain the href tags
    blogspot_list.append(link['href'])
    for i in blogspot_list:
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break
        # get every page linked from the blogspot links
        image_page = response.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of blogspot's images
        src_links = page_soup.findAll('img', src=rSrcBlogspot)
        blogspot_src = []
        for li in src_links:
            blogspot_src.append(li['src']) # add all the src part to a list

        # generate just the filename of the image to be locally saved
        save_extension = re.split('(/[0-9A-Za-z_-]+/)*', blogspot_src[0])

        savefile = basedir + str(save_extension[-1])

        download_url = blogspot_src[0]
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
