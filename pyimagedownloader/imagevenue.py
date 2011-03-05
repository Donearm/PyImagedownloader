#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2011, Gianluca Fiore
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
#
# to find the page with streamate ads
RRedirects = re.compile("uploadimg\-streamate\.php", re.IGNORECASE)
# to find generical redirects
RRedirects2 = re.compile("Continue To Your Image", re.IGNORECASE)
# to find the url of the imagevenue's countdown
RRedirects3 = re.compile("tempfull-default\.php", re.IGNORECASE) 


def imagevenue_parse(link, basedir):
    """For parsing normal imagevenue's links"""

    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    # if there are ads on the page, resubmit the link to the parser
    if re.search(RRedirects, response):
        imagevenue_parse(link, basedir)
        return
    elif re.search(RRedirects2, response):
        imageveneue_parse(link)
        return

    try:
        page = lxml.html.fromstring(response)
    except lxml.etree.XMLSyntaxError as e:
        # most of the time we can simply ignore parsing errors
        return

    # find the src attribute which contains the real link of imagevenue's
    # images
    src_links = page.xpath("//img[@id='thepic']")

    imagevenue_src = [li.get('src', None) for li in src_links]

    # remove unneeded parts
    imagevenue_split = re.split('img.php\?(loc=loc[0-9]{,3}&)?image=', link)
    try:
        # make up the real image url
        download_url = str(imagevenue_split[0]) + str(imagevenue_src[0])
    except IndexError:
        # if we get an IndexError just continue (it may means that the image
        # can't be downloaded from the server or there is a host's glitch
        pass

    try:
        # generate just the filename of the image to be locally saved
        save_extension = re.split('([0-9a-zA-Z]+-[0-9]+/)?loc[0-9]{,4}/', imagevenue_src[0]) 
        savefile = join(basedir, str(save_extension[-1]))
        if savefile.endswith('.'):
            # add the extension for images without it
            savefile = savefile + 'jpg'
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 
    except IndexError:
        return


def imagevenue_embed(link):
    """For parsing the links coming from paid host images like usercash"""

    # get every page linked from the imagevenue links
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    page = lxml.html.fromstring(response)

    # find the src attribute which contains the real link of imagevenue's
    # images
    src_links = page.xpath("//img[@id='thepic']")
    imagevenue_src = []
    for li in src_links:
        imagevenue_src.append(li.get('src', None))


        # remove unneeded parts
        imagevenue_split = re.split('img.php\?image=', link)
        try:
            # make up the real image url
            download_url = str(imagevenue_split[0]) + str(imagevenue_src[0])
        except IndexError:
            # if we get an IndexError just continue (it may means that the
            # image can't be downloaded from the server or there is a host's
            # glitch
            continue

    # generate just the filename of the image to be locally saved
    save_extension = re.split('([0-9a-zA-Z]+-[0-9]+/)?loc[0-9]{,4}/', imagevenue_src[0]) 
    savefile = basedir + str(save_extension[-1])
    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 
