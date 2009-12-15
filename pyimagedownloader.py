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
__version__ = "1.2"
__date__ = "01102009"
__email__ = "forod.g@gmail.com"

import sys
import re
import urllib2
from socket import setdefaulttimeout
from cookielib import CookieJar
from urllib import urlencode
import lxml.html
from BeautifulSoup import BeautifulSoup, SoupStrainer
from optparse import OptionParser
# importing local modules
import savesource, imageshack, imagevenue, uppix, imgshed, imagehaven, imagebam, imagetitan, bellazon, skinsbe, shareapic, storeimgs, upmyphoto, sharenxs, blogspot

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
#if len(sys.argv)!=2:
#    print 'Usage: pyimagedownloader url'
#    sys.exit(0)

# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
#rImagevenue = re.compile("href=\"?http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rImagevenue = re.compile("http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
#rImagebam = re.compile("href=\"?http://www\.imagebam\.com/image", re.IGNORECASE)
rImagebam = re.compile("http://www\.imagebam\.com/image", re.IGNORECASE)
#rImagehaven = re.compile("href=\"?http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
rImagehaven = re.compile("http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
#rImageshack = re.compile("href=\"?http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
rImageshack = re.compile("http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
rUpmyphoto = re.compile("href=\"?http://(www\.)?upmyphoto\.com", re.IGNORECASE)
rImgshed = re.compile("href=\"?http://imgshed\.com", re.IGNORECASE)
rUppix = re.compile("href=\"?http://www\.uppix\.info", re.IGNORECASE)
#rBellazon = re.compile('href=\"?http://www\.bellazon\.com/http://www\.bellazon\.com/main/index\.php\?act=', re.IGNORECASE)
rBellazon = re.compile("http://www\.bellazon\.com/", re.IGNORECASE)
rSkinsBe = re.compile("href=\"?http://image\.skins\.be", re.IGNORECASE)
rShareapic = re.compile("href=\"http://www\.shareapic\.net", re.IGNORECASE)
rStoreimgs = re.compile("href=\"?http://storeimgs\.com", re.IGNORECASE)
rImagetitan = re.compile("href=\"?http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
rBlogspot = re.compile("href=\"?http://[0-9]\.bp\.blogspot\.com", re.IGNORECASE)
rSharenxs = re.compile("href=\"?http://sharenxs\.com", re.IGNORECASE)
#rCelebutopia = re.compile("http://www\.celebutopia\.net/", re.IGNORECASE)
rUsemycomputer = re.compile("http://forum\.usemycomputer\.com/", re.IGNORECASE)
rImc = re.compile("http://www\.project-xtapes\.com/", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'



class ImageHostParser():
    """ The main parser class """

    def __init__(self, page, tag):
        #self.page = BeautifulSoup(page)
        self.page = lxml.html.fromstring(page)
        self.tag = tag
        self.which_host(tag)

    def which_host(self, tag):
        #all_tags = self.page.findAll(tag)
        all_tags = self.page.xpath('//a[@href]')
        for L in all_tags:
            #stringl = str(L)
            stringl = str(L.get('href', None))
            if rImagevenue.search(stringl):
                #imagevenue.imagevenue_parse(L)
                imagevenue.imagevenue_parse(stringl)
            elif rImagebam.search(stringl):
                #imagebam.imagebam_parse(L)
                imagebam.imagebam_parse(stringl)
            elif rImagehaven.search(stringl):
                #imagehaven.imagehaven_parse(L)
                imagehaven.imagehaven_parse(stringl)
            elif rImageshack.search(stringl):
                #imageshack.imageshack_parse(L)
                imageshack.imageshack_parse(stringl)
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
            elif rBlogspot.search(stringl):
                blogspot.blogspot_parse(L)
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

    # set a cookie handler and install the opener
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    # for some sites we need to login first....
    if rUsemycomputer.search(url):
        # We got a login user/pwd for usemycomputer, let's first login then
        umc_name = 'nirari'
        umc_pwd = 'MFdoutzen'
        #login1_page = 'http://forum.usemycomputer.com/index.php?action=login'
        login2_page = 'http://forum.usemycomputer.com/index.php?action=login2'
        values = {'user' : umc_name, 'passwrd' : umc_pwd, 'login' : 'Login'}

        # encode values
        data = urlencode(values)

        # first request to the login1 page. Not needed?
        #request1 = urllib2.Request(login1_page, data)
        #response1 = opener.open(request1)

        # second request to the login2 page
        request2 = urllib2.Request(login2_page, data)
        response1 = opener.open(request2)
    elif rImc.search(url):
        # Login credentials for Imc website
        imc_name = 'nirari'
        imc_pwd = 'Ninxtapes'
        login_page = 'http://project-xtapes.com/main/magazine/login.php'
        values = {'login' : 'Sign In', 'password' : imc_pwd, 'username' : imc_name}

        data = urlencode(values)

        # login page request
        request = urllib2.Request(login_page, data)
        response = opener.open(request)


    # Open and read the page contents
    data = urlencode(values)
    request = urllib2.Request(url, data, headers)

    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        # if the site doesn't accept a POST request, make a GET instead
        if e.code == 405:
            print("GET request")
            request = urllib2.Request(url)
            # adding the User-Agent in case it wasn't
            request.add_header('User-Agent', user_agent)
            response = urllib2.urlopen(request)
        else:
            print(e.code)
            print(e.reason)
            sys.exit(1)

    Rpage = response.read()
    return Rpage


# Generate the argument parser
def argument_parser():
    usage_message = "usage: %prog [options] url"
    cli_parser = OptionParser(usage=usage_message)
    cli_parser.add_option("-c", "--credit",
            help="optionally save the name of the poster of the images in a file",
            dest="poster")
    (options, args) = cli_parser.parse_args()
    return options.poster, args



if __name__ == "__main__":
    (poster, url) = argument_parser()
    Rpage = http_connector(url[0])
    # Parse the page for images
    parser = ImageHostParser(Rpage, 'a', )
    # Generate the directory for the source file and the images downloaded
    savesource.save_source(url[0], creditor=poster)
    sys.exit(0)
