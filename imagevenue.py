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
from urllib import FancyURLopener, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer




# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rImagevenue = re.compile("href=\"?http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

# Instanciate the UrlOpener
myopener = MyUrlOpener()

def imagevenue_parse(link):
    """For parsing normal imagevenue's links"""
    
    imagevenue_list = [] # the list that will contain the href tags
    imagevenue_list.append(link['href'])
    for i in imagevenue_list:
        # get every page linked from the imagevenue links
        image_page = myopener.open(i)
        Rimage_page = image_page.read()
        page_soup = BeautifulSoup(Rimage_page)
        # find the src attribute which contains the real link of imagevenue's images
        src_links = page_soup.findAll('img', id='thepic')
        imagevenue_src = []
        for li in src_links:
            imagevenue_src.append(li['src']) # add all the src part to a list

        # Close the page
        image_page.close()

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
        savefile = basedir + str(save_extension[1])
        # finally save the image on the desidered directory
        urlretrieve(download_url, savefile) 

def imagevenue_embed(link):
    """For parsing the links coming from paid host images like usercash"""

    # get every page linked from the imagevenue links
    image_page = myopener.open(link)
    Rimage_page = image_page.read()
    page_soup = BeautifulSoup(Rimage_page)
    # find the src attribute which contains the real link of imagevenue's images
    src_links = page_soup.findAll('img', id='thepic')
    imagevenue_src = []
    for li in src_links:
        imagevenue_src.append(li['src']) # add all the src part to a list

        # Close the page
        image_page.close()

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
