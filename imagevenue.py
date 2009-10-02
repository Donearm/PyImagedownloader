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
from urllib import urlretrieve, urlencode
from BeautifulSoup import BeautifulSoup, SoupStrainer
from cookielib import CookieJar


# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rImagevenue = re.compile("href=\"?http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rScript = re.compile("<scr'\+'ipt[^>]*>(.*?)</scr'\+'ipt>", re.IGNORECASE) # identify malformed script tags
rRedirects = re.compile("uploadimg\-streamate\.php", re.IGNORECASE) # to find the page with streamate ads
rRedirects2 = re.compile("Continue To Your Image", re.IGNORECASE) # to find generical redirects
rRedirects3 = re.compile("tempfull-default\.php", re.IGNORECASE) # to find the url of the imagevenue's countdown

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def imagevenue_parse(link):
    """For parsing normal imagevenue's links"""
    
    imagevenue_list = [] # the list that will contain the href tags
    imagevenue_list.append(link['href'])
    for i in imagevenue_list:
        request = urllib2.Request(i, data, headers)
        try:
            response = urllib2.urlopen(request)
            # search if the image link goes to a "Continue to image" page. If so substitute the url part with the real image one and request the page again
            redirect = re.search(rRedirects3, response.geturl())
            if redirect:
                realurl = rRedirects3.sub('img.php', response.geturl())
                try:
                    response = urllib2.urlopen(realurl)
                except urllib2.URLError as e:
                    if e.code == 404:
                        break
        except urllib2.URLError as e:
            if e.code == 404:
                break
        # get every page linked from the imagevenue links, removing those
        # damned '<scr'+'ipt>' tags
        image_page = rScript.sub('', response.read())


        # if there are ads on the page, resubmit the link to the parser
        if re.search(rRedirects, image_page):
            imagevenue_parse(link)
            break
        elif re.search(rRedirects2, image_page):
            imageveneue_parse(link)
            break

        page_soup = BeautifulSoup(image_page)

        # find the src attribute which contains the real link of imagevenue's images
        src_links = page_soup.findAll('img', id='thepic')
        imagevenue_src = []
        for li in src_links:
            imagevenue_src.append(li['src']) # add all the src part to a list


        imagevenue_split = re.split('img.php\?image=', i) # remove the unneeded parts
        try:
            # make up the real image url
            download_url = str(imagevenue_split[0]) + str(imagevenue_src[0])
        except IndexError:
            # if we get an IndexError just continue (it may means that the image
            # can't be downloaded from the server or there is a host's glitch
            continue
        # generate just the filename of the image to be locally saved
        save_extension = re.split('[0-9a-zA-Z]+-[0-9]+/loc[0-9]{,4}/', imagevenue_src[0]) 
        try:
            savefile = basedir + str(save_extension[1])
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 
        except IndexError:
            break


def imagevenue_embed(link):
    """For parsing the links coming from paid host images like usercash"""

    # get every page linked from the imagevenue links
    request = urllib2.Request(link, data, headers)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        return
    except urllib2.URLError as e:
        return
    image_page = response.read()
    page_soup = BeautifulSoup(image_page)
    # find the src attribute which contains the real link of imagevenue's images
    src_links = page_soup.findAll('img', id='thepic')
    imagevenue_src = []
    for li in src_links:
        imagevenue_src.append(li['src']) # add all the src part to a list


        imagevenue_split = re.split('img.php\?image=', link) # remove the unneeded parts
        try:
            # make up the real image url
            download_url = str(imagevenue_split[0]) + str(imagevenue_src[0])
        except IndexError:
            # if we get an IndexError just continue (it may means that the image
            # can't be downloaded from the server or there is a host's glitch
            continue
    # generate just the filename of the image to be locally saved
    save_extension = re.split('[0-9a-zA-Z]+-[0-9]+/loc[0-9]{,4}/', imagevenue_src[0]) 
    savefile = basedir + str(save_extension[1])
    # finally save the image on the desidered directory
    urlretrieve(download_url, savefile) 
