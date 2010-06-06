#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008, Gianluca Fiore
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,          
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            
#   GNU General Public License for more details.                           
#                                                                         
#   You should have received a copy of the GNU General Public License        
#   along with this program; if not, write to the Free Software              
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#############################################################################

__author__ = "Gianluca Fiore"
__license__ = "GPL"
__version__ = "1.3"
__date__ = "28052010"
__email__ = "forod.g@gmail.com"

import sys
import re
import urllib2
from socket import setdefaulttimeout
from cookielib import CookieJar
from urllib import urlencode
from optparse import OptionParser
import lxml.html
#from BeautifulSoup import BeautifulSoup, SoupStrainer
# importing local modules
import savesource, imageshack, imagevenue, uppix, imagehaven, imagebam, imagetitan, bellazon, skinsbe, shareapic, storeimgs, upmyphoto, sharenxs, blogspot, postimage, imageupper, imagesocket, photobucket
from http_connector import *
# importing config file variables
from pyimg import *


# The regexp we'll need to find the link
#rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
#rImagevenue = re.compile("href=\"?http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rImagevenue = re.compile("http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
#rImagebam = re.compile("href=\"?http://www\.imagebam\.com/image", re.IGNORECASE)
rImagebam = re.compile("http://www\.imagebam\.com/image", re.IGNORECASE)
#rImagehaven = re.compile("href=\"?http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
rImagehaven = re.compile("http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
#rImageshack = re.compile("href=\"?http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
rImageshack = re.compile("http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
#rUpmyphoto = re.compile("href=\"?http://(www\.)?upmyphoto\.com", re.IGNORECASE)
rUpmyphoto = re.compile("http://(www\.)?upmyphoto\.com", re.IGNORECASE)
#rImgshed = re.compile("href=\"?http://imgshed\.com", re.IGNORECASE)
#rUppix = re.compile("href=\"?http://www\.uppix\.info", re.IGNORECASE)
rUppix = re.compile("http://www\.uppix\.info", re.IGNORECASE)
#rBellazon = re.compile('href=\"?http://www\.bellazon\.com/http://www\.bellazon\.com/main/index\.php\?act=', re.IGNORECASE)
rBellazon = re.compile("http://www\.bellazon\.com/", re.IGNORECASE)
#rSkinsBe = re.compile("href=\"?http://image\.skins\.be", re.IGNORECASE)
rSkinsBe = re.compile("http://image\.skins\.be", re.IGNORECASE)
#rShareapic = re.compile("href=\"http://www\.shareapic\.net/content\.php\?id", re.IGNORECASE)
rShareapic = re.compile("http://www\.shareapic\.net/content\.php\?id", re.IGNORECASE)
#rStoreimgs = re.compile("href=\"?http://storeimgs\.com", re.IGNORECASE)
rStoreimgs = re.compile("http://storeimgs\.com", re.IGNORECASE)
#rImagetitan = re.compile("href=\"?http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
rImagetitan = re.compile("http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
#rSharenxs = re.compile("href=\"?http://sharenxs\.com", re.IGNORECASE)
rSharenxs = re.compile("http://(www\.)?sharenxs\.com/view/\?", re.IGNORECASE)
#rBlogspot = re.compile("href=\"?http://[0-9]\.bp\.blogspot\.com", re.IGNORECASE)
rBlogspot = re.compile("http://[0-9]\.bp\.blogspot\.com", re.IGNORECASE)
rPostimage = re.compile("http://www\.postimage\.org/image\.php", re.IGNORECASE)
rImageUpper = re.compile("http://imageupper\.com/i/", re.IGNORECASE)
rImageSocket = re.compile("http://imagesocket\.com", re.IGNORECASE)
rPhotobucket = re.compile("http://[a-z0-9]+\.photobucket\.com", re.IGNORECASE)


class ImageHostParser():
    """ The main parser class """

    def __init__(self, page, tag, attr):
        #self.page = BeautifulSoup(page)
        self.page = lxml.html.fromstring(page)
        self.tag = tag
        self.attr = attr
        self.which_host(tag, attr)

    def which_host(self, tag, attr):
        #all_tags = self.page.findAll(tag)
        xpath_search = '//' + tag + '[@' + attr + ']'
        all_tags = self.page.xpath(xpath_search)
        n = 0
        for L in all_tags:
            #stringl = str(L)
            stringl = str(L.get(attr, None))
            if rImagevenue.search(stringl):
                imagevenue.imagevenue_parse(stringl)
                n = n + 1
            elif rImagebam.search(stringl):
                imagebam.imagebam_parse(stringl)
                n = n + 1
            elif rImagehaven.search(stringl):
                imagehaven.imagehaven_parse(stringl)
                n = n + 1
            elif rImageshack.search(stringl):
                imageshack.imageshack_parse(stringl)
                n = n + 1
            elif rUpmyphoto.search(stringl):
                upmyphoto.upmyphoto_parse(stringl)
                n = n + 1
            elif rUppix.search(stringl):
                uppix.uppix_parse(stringl)
                n = n + 1
            elif rBellazon.search(stringl):
                not_supported('Bellazon')
                #bellazon.bellazon_parse(L)
                n = n + 1
            elif rSkinsBe.search(stringl):
                skinsbe.skinsbe_parse(stringl)
                n = n + 1
            elif rShareapic.search(stringl):
                shareapic.shareapic_parse(stringl)
                n = n + 1
            elif rStoreimgs.search(stringl):
                storeimgs.storeimgs_parse(stringl)
                n = n + 1
            elif rImagetitan.search(stringl):
                imagetitan.imagetitan_parse(stringl)
                n = n + 1
            elif rSharenxs.search(stringl):
                sharenxs.sharenxs_parse(stringl)
                n = n + 1
            elif rBlogspot.search(stringl):
                blogspot.blogspot_parse(stringl)
                n = n + 1
            elif rPostimage.search(stringl):
                not_supported('Postimage')
                #postimage.postimage_parse(stringl)
                n = n + 1
            elif rImageUpper.search(stringl):
                imageupper.imageupper_parse(stringl)
                n = n + 1
            elif rImageSocket.search(stringl):
                imagesocket.imagesocket_parse(stringl)
                n = n + 1
            elif rPhotobucket.search(stringl):
                photobucket.photobucket_parse(stringl)
                n = n + 1
            else:
                continue
        print("%d images were present" % n)



# Generate the argument parser
def argument_parser():
    usage_message = "usage: %prog [options] url"
    cli_parser = OptionParser(usage=usage_message)
    cli_parser.add_option("-c", "--credit",
            help="optionally save the name of the poster of the images in a file",
            dest="poster")
    cli_parser.add_option("-e", "--embed",
            action="store_true",
            help="enable search for embedded images too",
            dest="embed")
    (options, args) = cli_parser.parse_args()
    return options.poster, options.embed, args

# print an advice for hosts not supported
def not_supported(host):
    msg = "Sorry but %s isn't supported or isn't working right now" % host
    print(msg)


if __name__ == "__main__":
    (poster, embed, url) = argument_parser()
    Rpage = http_connector(url[0])
    # Parse the page for images
    parser = ImageHostParser(Rpage, 'a', 'href')
    if embed:
        # do we need to search for embedded images then?
        # Note: at the moment it downloads thumbnails too
        print("Searching for embedded images")
        print("")
        parser.which_host('img', 'src')
    # Generate the directory for the source file and the images downloaded
    savesource.save_source(url[0], creditor=poster)
    sys.exit(0)
