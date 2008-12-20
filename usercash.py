#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
"""
"""
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__version__ = "1.0"
__date__ = "10102008"
__email__ = "forod.g@gmail.com"

import re
from urllib import FancyURLopener, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer

# +---------------------------------------------------------------------------+
# | GPL license block                                                         |
# |                                                                           |
# | This program is free software; you can redistribute it and/or modify      |
# | it under the terms of the GNU General Public License as published by      |
# | the Free Software Foundation; either version 2 of the License, or         |
# | (at your option) any later version.                                       |
# |                                                                           |
# | This program is distributed in the hope that it will be useful,           |
# | but WITHOUT ANY WARRANTY; without even the implied warranty of            |
# | MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             |
# | GNU General Public License for more details.                              |
# |                                                                           |
# | You should have received a copy of the GNU General Public License         |
# | along with this program; if not, write to the Free Software               |
# | Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA |
# +---------------------------------------------------------------------------+
# +---------------------------------------------------------------------------+
# | Release Log                                                               |
# |                                                                           |
# | 1.0 : first release. Support for imagevenue, imagebam, imageshack,        |
# |       upmyphoto, uppix and imgshed                                        |
# +---------------------------------------------------------------------------+


# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rUsercash = re.compile("href=\"?http://[0-9]+\.usercash\.com", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'

myopener = MyUrlOpener()

def usercash_parse(link):    
    usercash_list = []
    usercash_list.append(link['href'])
    for images in usercash_list:
        # get every page linked from the usercash links
        image_page = myopener.open(images)
        rimage_page = image_page.read()
        page_soup = BeautifulSoup(rimage_page)
        # find the src attribute which contains the real link of imagevenue's images
        src_links = page_soup.findAll('frame', src=rJpgSrc)
        usercashSrc = []
        for li in src_links:
            li_without_loc = re.sub('&.*', '', li['src'])
            usercashSrc.append(li_without_loc) # add all the src part to a list
            # open the imagevenue's page
            linked_image_page = myopener.open(li_without_loc)
            Rlinked_image_page = linked_image_page.read()
            linked_page_soup = BeautifulSoup(Rlinked_image_page)
            src_links2 = linked_page_soup.findAll('img', id='thepic')
            imagevenue_src = []
            for src in src_links2:
                imagevenue_src.append(src)

            linked_image_page.close()

            print imagevenue_src[0]
            imagevenue_split = re.split('img.php\?image=', li) # remove the unneeded parts
            try:
                # make up the real image url
                download_url = str(imagevenue_split[0]) + str(imagevenue_src[0])
            except IndexError:
                # if we get an IndexError just continue (it may means 
                #that the image can't be downloaded from the server 
                #or there is a host's glitch
                continue
            # generate just the filename of the image to be locally saved
            save_extension = re.split('[0-9a-zA-Z]+-[0-9]+/loc[0-9]{,4}/', imagevenue_src[0]) 
            print save_extension
            savefile = basedir + str(imagevenue_src[0])
            download_url = str(imagevenue_split[0]) + str(imagevenue_src[0])
            # finally save the image on the desidered directory
            urlretrieve(downloadUrl, savefile) 


        # Close the first page
        image_page.close()

