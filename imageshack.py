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
import random
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import lxml.html
from pyimg import *




# The regexp we'll need to find the link
#rSrcImageshack = re.compile('/img[0-9]+/[0-9]+/[a-zA-Z0-9]+\.[jpg|gif|png]', re.IGNORECASE)
# The split regexp
rImageshackSplit = '/img[0-9]{,3}/[0-9]+/'


values = {}
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def imageshack_parse(link):
    imageshack_list = [] # the list that will contain the href tags
    #imageshack_list.append(link['href'])
    imageshack_list.append(link)
    for i in imageshack_list:
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            if e.code == 405:
                # we could be dealing with an url which is already the image url
                # let's download it right away then
                imageshack_download(rImageshackSplit, i)
                break
            else:
                break
        except urllib2.URLError as e:
            break

        # get every page linked from the imageshack links
        image_page = response.read()
        #page_soup = BeautifulSoup(image_page)
        page = lxml.html.fromstring(image_page)

        # find the src attribute which contains the real link of imageshack's images
        #src_links = page_soup.findAll('img', src=rSrcImageshack)
        src_links = page.xpath("//img[@id='main_image']")

        imageshack_src = [li.get('src', None) for li in src_links]

        try:
            imageshack_download('/i/', i, imageshack_src[0], 1)            
        except IndexError:
            break

def imageshack_download(regexp, url, src="", htmlpage=0):
    """downloader function for imageshack links. It needs a regexp for re.split
    and of course the url of an imageshack hosted image
    htmlpage is optional and it's to be enabled only for imageshack's pages
    containing an image (and not the direct source url)
    same for src, it's optional and only for those kind of pages"""

    # generate just the filename of the image to be locally saved
    save_extension = re.split(regexp, url)
    print(save_extension)
    if htmlpage == 1:
        download_url = save_extension[0] + src
        # generate a random number; if not, the images will have the same save_extension[1]
        # and will overwrite each other   
        num = random.randrange(1,1000)
        savefile = basedir + str(num) + str(save_extension[1]).replace('/', '')
    else:
        download_url = url
        savefile = basedir + str(save_extension[1])

    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 


