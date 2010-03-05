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
__date__ = "16122009"
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
import savesource, imageshack, imagevenue, uppix, imagehaven, imagebam, imagetitan, bellazon, skinsbe, shareapic, storeimgs, upmyphoto, sharenxs, blogspot, postimage
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
#rCelebutopia = re.compile("http://www\.celebutopia\.net/", re.IGNORECASE)
rUsemycomputer = re.compile("http://forum\.usemycomputer\.com/", re.IGNORECASE)
rImc = re.compile("http://www\.project-xtapes\.com/", re.IGNORECASE)


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
                #upmyphoto.upmyphoto_parse(L)
                upmyphoto.upmyphoto_parse(stringl)
            elif rUppix.search(stringl):
                #uppix.uppix_parse(L)
                uppix.uppix_parse(stringl)
            elif rBellazon.search(stringl):
                bellazon.bellazon_parse(L)
            elif rSkinsBe.search(stringl):
                #skinsbe.skinsbe_parse(L)
                skinsbe.skinsbe_parse(stringl)
            elif rShareapic.search(stringl):
                #shareapic.shareapic_parse(L)
                shareapic.shareapic_parse(stringl)
            elif rStoreimgs.search(stringl):
                #storeimgs.storeimgs_parse(L)
                storeimgs.storeimgs_parse(stringl)
            elif rImagetitan.search(stringl):
                #imagetitan.imagetitan_parse(L)
                imagetitan.imagetitan_parse(stringl)
            elif rSharenxs.search(stringl):
                #sharenxs.sharenxs_parse(L)
                sharenxs.sharenxs_parse(stringl)
            elif rBlogspot.search(stringl):
                #blogspot.blogspot_parse(L)
                blogspot.blogspot_parse(stringl)
            elif rPostimage.search(stringl):
                postimage.postimage_parse(stringl)
            else:
                continue

def site_login(url, opener):
    """check if it's a site or forum we have login credentials for and log-in"""
    if rUsemycomputer.search(url):
        # We got a login user/pwd for usemycomputer, let's first login then
        login2_page = 'http://forum.usemycomputer.com/index.php?action=login2'
        values = {'user' : umc_name, 'passwrd' : umc_pwd, 'login' : 'Login'}

        # encode values
        data = urlencode(values)

        # second request to the login2 page
        request2 = urllib2.Request(login2_page, data)
        response1 = opener.open(request2)
    elif rImc.search(url):
        # Loging to IMC website
        login_page = 'http://project-xtapes.com/main/magazine/login.php'
        values = {'login' : 'Sign In', 'password' : imc_pwd, 'username' : imc_name}

        data = urlencode(values)

        # login page request
        request = urllib2.Request(login_page, data)
        response = opener.open(request)



def http_connector(url):
    """connect to a url, get the page and return it"""

    # Some variables for the connection
    values = {}
    headers = { 'User-Agent' : user_agent }
    # Set the timeout we chose in the config file
    setdefaulttimeout(timeout)

    # Do we need to debug?
    debug = 0

    # set a cookie handler and install the opener
    cj = CookieJar()
    if debug == 1:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler(debuglevel=1))
    else:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    # for some sites we need to login first....
    site_login(url, opener)

    # Encode values (if any)
    data = urlencode(values)

    # currently used headers
    #print(request.headers)

    if values:
        # if there are some values it's a POST request
        request = urllib2.Request(url, data, headers)
        try:
            response = urllib2.urlopen(request)
            # various infos on the response
            #print(response.info())
            #print(response.geturl())
            #print(response.getcode())
        except urllib2.HTTPError as e:
            # if the site doesn't accept a POST request, make a GET instead
            if e.code == 405:
                response = get_request(url, user_agent)
            else:
                print(e.code)
                sys.exit(1)
        except urllib2.URLError as e:
            print(e.reason)
    else:
        # no values, then it's a GET request
        response = get_request(url, user_agent)


    #print(cj.make_cookies(response, request)) # show the cookies
    Rpage = response.read()
    return Rpage

def get_request(url, ua=user_agent):
    print("GET request")
    request = urllib2.Request(url)
    request.add_header('User-Agent', ua)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        print(e.code)
        sys.exit(1)
    except urllib2.URLError as e:
        print(e.reason)
        sys.exit(1)

    return response


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
