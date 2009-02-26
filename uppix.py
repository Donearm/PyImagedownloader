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
from urllib import urlretrieve, urlencode
from BeautifulSoup import BeautifulSoup, SoupStrainer



# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rUppix = re.compile("href=\"?http://www\.uppix\.info", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def uppix_parse(link):
    uppix_list = [] # the list that will contain the href tags
    uppix_list.append(link['href'])
    for i in uppix_list:
        # get every page linked from the uppix links
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            break
        except urllib2.URLError, e:
            break
        image_page = response.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of uppix's images
        src_links = page_soup.findAll('img', id='dpic')
        uppix_src = []
        for li in src_links:
            uppix_src.append(li['src']) # add all the src part to a list

        # generate just the filename of the image to be locally saved
        save_extension = re.sub('S[0-9]+/', '',  uppix_src[0]) 
        uppix_sub = re.sub('Viewer[a-zA-Z]\.php\?file=', '', i)
        savefile = basedir + save_extension
        # finally save the image on the desidered directory
        urlretrieve(uppix_sub, savefile) 
