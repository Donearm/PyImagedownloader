#!/usr/bin/env python2
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
# importing config file variables
from pyimg import *


#rCelebutopia = re.compile("http://www\.celebutopia\.net/", re.IGNORECASE)
rUsemycomputer = re.compile("http://forum\.usemycomputer\.com/", re.IGNORECASE)
rImc = re.compile("http://www\.imcmagazine\.com/", re.IGNORECASE)
rCelebrityForum = re.compile("http://celebrityforum\.freeforumzone\.leonardo\.it", re.IGNORECASE)


def check_string_or_list(url):
    """check if the url given is a string or a list and always returns a correct url"""
    if isinstance(url, str):
        uri = url
        return uri
    elif isinstance(url, list):
        uri = url[0]
        return uri
    else:
        # something else has been passed, exiting
        sys.exit(1)


def connector(url, moveon=0):
    """connect to a url, get the page and return it"""

    # Some variables for the connection
    values = {}
    headers = { 'User-Agent' : user_agent }
    # Set the timeout we chose in the config file
    setdefaulttimeout(timeout)

    # set a cookie handler and install the opener
    cj = CookieJar()
    if debug == 1:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler(debuglevel=1))
    else:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    # check if the url given is a string or a list
    uri = check_string_or_list(url)

    # for some sites we need to login first....
    site_login(uri, opener)

    # Encode values (if any)
    data = urlencode(values)

    # currently used headers
    #print(request.headers)

    if values:
        # if there are some values it's a POST request
        response = post_request(uri, data, user_agent)
    else:
        # no values, then it's a GET request
        response = get_request(uri, user_agent)


    #print(cj.make_cookies(response, request)) # show the cookies
    Rpage = response.read()
    return Rpage


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
        login_page = 'http://www.imcmagazine.com/login.php'
        values = {'login' : 'Sign In', 'password' : imc_pwd, 'username' : imc_name}

        data = urlencode(values)

        # login page request
        request = urllib2.Request(login_page, data)
        response = opener.open(request)
    elif rCelebrityForum.search(url):
        login_page = 'http://celebrityforum.freeforumzone.leonardo.it/loginc.aspx'
        auth_page = 'http://auth.leonardo.it/sso/login'


        values = {'SSO_cik': 'G9clW564v319FjXGuTXXOVzSKDrUTFAXfI8M0uDx2EoxYiBekWLO7M6fMu99MlpQ',
                'SSO_USERNAME': cf_name, 'SSO_PASSWORD': cf_pwd, 'SSO_p': 'c',
                'SSO_CHANNEL': '3', 'SSO_PAUTH': '0', 'SSO_USE_ENC': '0',
                'SSO_PAYLOAD': '1', 'SSO_SECURE_LOGIN': '1', 'FFZ_LOGIN_RQ': '1',
                'FFZ_SLOGIN': '1', 'FFZ_HLOGIN': '0', 'SSO_REDIRECT_PATH': login_page}
        
        data = urlencode(values)

        request = urllib2.Request(auth_page, data)
        response = opener.open(request)

def post_request(url, data, headers):
    request = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(request)
        # various infos on the response
        #print(response.info())
        #print(response.geturl())
        #print(response.getcode())
        return response
    except urllib2.HTTPError as e:
        if e.code == 405:
            # we were wrong, the url doesn't accept a POST, make a GET then
            response = get_request(url, user_agent)
        elif e.code == 404:
            # url non-existing, just go on
            print("%s couldn't be found, skipping it..." % url)
            response = ''
            return response
        else:
            print(e.code)
            sys.exit(1)
    except urllib2.URLError as e:
        print(e.reason)


def get_request(url, ua=user_agent):
    request = urllib2.Request(url)
    request.add_header('User-Agent', ua)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        if e.code == 404:
            # url non-existing, just go on
            print("%s couldn't be found, skipping it..." % url)
            response = ''
            return response
        else:
            print(e.code)
            sys.exit(1)
    except urllib2.URLError as e:
        print(e.reason)
        sys.exit(1)

    return response

