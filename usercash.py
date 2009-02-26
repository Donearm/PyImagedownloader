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
from imagevenue import imagevenue_embed

# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rUsercash = re.compile("href=\"?http://[0-9]+\.usercash\.com", re.IGNORECASE)
rImagevenue = re.compile("http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def usercash_parse(link):    
    usercash_list = []
    usercash_list.append(link['href'])
    for images in usercash_list:
        # get every page linked from the usercash links
        request = urllib2.Request(images, data, headers)
        response = urllib2.urlopen(request)
        image_page = response.read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of imagevenue's images
        src_links = page_soup.findAll('frame', src=rJpgSrc)

        # give imagevenue_embed the correct link
        correct_link = re.sub("^.*http", 'http', str(src_links))
        correct_link = re.sub("&amp;ref=.*$", '', correct_link)

        if rImagevenue.search(correct_link):
            imagevenue_embed(correct_link)


