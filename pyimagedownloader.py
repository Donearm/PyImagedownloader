#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
"""
"""
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__version__ = "1.1"
__date__ = "19052009"
__email__ = "forod.g@gmail.com"

import sys
import re
import urllib2
from socket import setdefaulttimeout
from cookielib import CookieJar
from urllib import urlencode
from BeautifulSoup import BeautifulSoup, SoupStrainer
# importing local modules
import savesource, imageshack, imagevenue, usercash, uppix, imgshed, imagehaven, imagebam, imagetitan, bellazon, skinsbe, shareapic, storeimgs, upmyphoto, sharenxs

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
# | 1.1 : Added shareapic and usercash support. Some bugfixes.
# | 1.0 : first release. Support for imagevenue, imagebam, imageshack,        |
# |       upmyphoto, uppix and imgshed                                        |
# +---------------------------------------------------------------------------+


# If no arguments were given, print a helpful message
if len(sys.argv)!=2:
    print 'Usage: pyimagedownloader url'
    sys.exit(0)

# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rUsercash = re.compile("href=\"?http://[0-9]+\.usercash\.com", re.IGNORECASE)
rImagevenue = re.compile("href=\"?http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rImagebam = re.compile("href=\"?http://www\.imagebam\.com/image", re.IGNORECASE)
rImagehaven = re.compile("href=\"?http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
rImageshack = re.compile("href=\"?http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
rUpmyphoto = re.compile("href=\"?http://(www\.)?upmyphoto\.com", re.IGNORECASE)
rImgshed = re.compile("href=\"?http://imgshed\.com", re.IGNORECASE)
rUppix = re.compile("href=\"?http://www\.uppix\.info", re.IGNORECASE)
#rBellazon = re.compile('href=\"?http://www\.bellazon\.com/http://www\.bellazon\.com/main/index\.php\?act=', re.IGNORECASE)
rBellazon = re.compile("http://www\.bellazon\.com/", re.IGNORECASE)
rSkinsBe = re.compile("href=\"?http://image\.skins\.be", re.IGNORECASE)
rShareapic = re.compile("href=\"http://www\.shareapic\.net", re.IGNORECASE)
rStoreimgs = re.compile("href=\"?http://storeimgs\.com", re.IGNORECASE)
rImagetitan = re.compile("href=\"?http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
rSharenxs = re.compile("href=\"?http://sharenxs\.com", re.IGNORECASE)
rCelebutopia = re.compile("http://www\.celebutopia\.net/", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'



class ImageHostParser():
    """ The main parser class """

    def __init__(self, page, tag):
        self.page = BeautifulSoup(page)
        self.tag = tag
        self.which_host(tag)

    def which_host(self, tag):
        all_tags = self.page.findAll(tag)
        for L in all_tags:
            stringl = str(L)
            if rUsercash.search(stringl):
                usercash.usercash_parse(L)
            elif rImagevenue.search(stringl):
                imagevenue.imagevenue_parse(L)
            elif rImagebam.search(stringl):
                imagebam.imagebam_parse(L)
            elif rImagehaven.search(stringl):
                imagehaven.imagehaven_parse(L)
            elif rImageshack.search(stringl):
                imageshack.imageshack_parse(L)
            elif rUpmyphoto.search(stringl):
                upmyphoto.upmyphoto_parse(L)
            elif rImgshed.search(stringl):
                imgshed.imgshed_parse(L)
            elif rUppix.search(stringl):
                uppix.uppix_parse(L)
            elif rBellazon.search(stringl):
                print(stringl)
                bellazon.bellazon_parse(L)
            elif rSkinsBe.search(stringl):
                skinsbe.skinsbe_parse(L)
            elif rShareapic.search(stringl):
                shareapic.shareapic_parse(L)
            elif rStoreimgs.search(stringl):
                storeimgs.storeimgs_parse(L)
            elif rImagetitan.search(stringl):
                imagetitan.imagetitan_parse(L)
            elif rSharenxs.search(stringl):
                sharenxs.sharenxs_parse(L)
            else:
                continue


def http_connector(url):
    """connect to a url and get the page"""

    # Some variables for the connection
    values = {}
    user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009021410 Firefox/3.0.6'
    headers = { 'User-Agent' : user_agent }
    # Change the timeout
    timeout = 60
    setdefaulttimeout(timeout)

    if rCelebutopia.search(url):
        # for Celebutopia links we need a cookie handler
        cj = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

    # Open and read the page contents
    data = urlencode(values)
    request = urllib2.Request(url, data, headers)

    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        # if the site doesn't accept a POST request, make a GET instead
        if e.code == 405:
            print("GET request")
            request = urllib2.Request(sys.argv[1])
            # adding the User-Agent in case it wasn't
            request.add_header('User-Agent', user_agent)
            response = urllib2.urlopen(request)
        else:
            print(e.code)
            print(e.reason)
            sys.exit(1)

    Rpage = response.read()
    return Rpage






Rpage = http_connector(sys.argv[1])
# Parse the page for images
parser = ImageHostParser(Rpage, 'a', )
# Generate the directory for the source file and the images downloaded
savesource.save_source(sys.argv[1])
sys.exit(0)
