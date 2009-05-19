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
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rImagetitan = re.compile("href=\"?http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
rSrcImagetitan = re.compile("(img[0-9]{,2})(/[0-9A-Za-z]+/[0-9]+/)(.*[jpg|png|gif|jpeg])", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)


def imagetitan_parse(link):
    imagetitan_list = [] # the list that will contain the href tags
    imagetitan_list.append(link['href'])
    print("We are here!")
    for i in imagetitan_list:
        # get every page linked from the imagetitan links
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            break
        except urllib2.URLError as e:
            break
        image_page = response.read()
        #image_page = myopener.open(i).read()
        page_soup = BeautifulSoup(image_page)
        # find the src attribute which contains the real link of imagetitan's images
        src_links = page_soup.findAll('img', src=rSrcImagetitan)
        imagetitan_src = []
        for li in src_links:
            imagetitan_src.append(li['src']) # add all the src part to a list


        imgtitanmatch = re.match(rSrcImagetitan, imagetitan_src[0])

        imgmiddle = imgtitanmatch.group(2) # the middle part of the url
        imgname = imgtitanmatch.group(3) # the name of the image 
        imggrp = imgtitanmatch.group(1) # the 'img[0-9]'

        # generate just the filename of the image to be locally saved
        savefile = basedir + imgname
        # generate the url of the image
        download_url = 'http://' + imggrp + '.imagetitan.com/' + imggrp + imgmiddle + imgname
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

