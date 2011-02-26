#!/usr/bin/env python2
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
from urllib import urlretrieve
from os.path import join
import lxml.html
import http_connector


# The regexp we'll need to find the link
RSrcImagetitan = re.compile("(img[0-9]{,2})(/[0-9A-Za-z]+/[0-9]+/)(.*[jpg|png|gif|jpeg])", re.IGNORECASE)

def imagetitan_parse(link, basedir):
    # get every page linked from the imagetitan links
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    try:
        page = lxml.html.fromstring(response)
    except lxml.etree.XMLSyntaxError as e:
        # most of the time we can simply ignore parsing errors
        return

    # find the src attribute which contains the real link of imagetitan's images
    src_links = page.xpath("//img[@id='image']")

    imagetitan_src = [li.get('src', None) for li in src_links]


    imgtitanmatch = re.match(RSrcImagetitan, imagetitan_src[0])

    imgmiddle = imgtitanmatch.group(2) # the middle part of the url
    imgname = imgtitanmatch.group(3) # the name of the image 
    imggrp = imgtitanmatch.group(1) # the 'img[0-9]'

    # generate just the filename of the image to be locally saved
    savefile = join(basedir, imgname)
    # generate the url of the image
    download_url = 'http://' + imggrp + '.imagetitan.com/' + imggrp + imgmiddle + imgname
    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 

