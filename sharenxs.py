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




# The regexp we'll need to find the link
rSharenxsThumb = re.compile("http://sharenxs\.com/thumbnails/", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def sharenxs_parse(link):
    sharenxs_list = [] # the list that will contain the href tags
    sharenxs_list.append(link['href'])
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
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of sharenxs's images
        src_links = page_soup.findAll('img', src=rSharenxsThumb)
        #src_links = page_soup.findAll('link', rel='image_src')
        sharenxs_src = []
        for li in src_links:
            sharenxs_src.append(li['src']) # add all the src part to a list

        try:
            # generate just the filename of the image to be locally saved
            save_extension = re.split('tn-', sharenxs_src[0])

            savefile = basedir + str(save_extension[1])
            download_url = re.sub('thumbnails/tn-', 'images/', sharenxs_src[0])
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            break
