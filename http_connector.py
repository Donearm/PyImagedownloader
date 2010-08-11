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
# importing config file variables
from pyimg import *


#rCelebutopia = re.compile("http://www\.celebutopia\.net/", re.IGNORECASE)
rUsemycomputer = re.compile("http://forum\.usemycomputer\.com/", re.IGNORECASE)
rImc = re.compile("http://www\.project-xtapes\.com/", re.IGNORECASE)


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

    # for some sites we need to login first....
    site_login(url, opener)

    # Encode values (if any)
    data = urlencode(values)

    # currently used headers
    #print(request.headers)

    if values:
        # if there are some values it's a POST request
        response = post_request(url, data, user_agent)
    else:
        # no values, then it's a GET request
        response = get_request(url, user_agent)


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
        login_page = 'http://project-xtapes.com/main/magazine/login.php'
        values = {'login' : 'Sign In', 'password' : imc_pwd, 'username' : imc_name}

        data = urlencode(values)

        # login page request
        request = urllib2.Request(login_page, data)
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
        else:
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

        # For some sites we need to log-in first...
        self.site_login(url, self.opener)

        # encode values, if any
        self.data = urlencode(self.values)

        # Check which kind of HTTP request we are going to do
        if self.values:
            # if there are any values it's a POST request
            response = self.post_request(url, self.data, self.useragent)
        else:
            # no values, then GET request
            response = self.get_request(url)

        #print(self.cj.make_cookies(response, request)) # show the cookies

        # read the page contents and return it
        Rpage = response.read()
        return Rpage


    def post_request(self, url, data, headers):
        request = urllib2.Request(url, data, headers)
        try:
            response = urllib2.urlopen(request)
            return response
        except urllib2.HTTPError as e:
            if e.code == 405:
                # we were wrong, the url doesn't accept a POST, make a GET then
                response = self.get_request(url, self.useragent)
            else:
                print(e.code)
                sys.exit(1)
        except urllib2.URLError as e:
            print(e.reason)
            sys.exit(1)

    def get_request(self, url):
        request = urllib2.Request(url)
        request.add_header('User-Agent', self.useragent)
        try:
            response = urllib2.urlopen(request)
            return response
        except urllib2.HTTPError as e:
            print(e.code)
            sys.exit(1)
        except urllib2.URLError as e:
            print(e.reason)
            sys.exit(1)


    def site_login(self, url, opener):
        """check if it's a site or forum for which we have login credentials. If yes, do
        the log-in and return a request for the original url after the process"""
        if self.rUsemycomputer.search(url):
            # Login to Usemycomputer forum
            self.login2_page = 'http://forum.usemycomputer.com/index.php?action=login2'
            values = {'user' : umc_name, 'passwrd' : umc_pwd, 'login' : 'Login'}
            # encode those values
            data = urlencode(values)

            # second request to the login2 page
            request2 = urllib2.Request(self.login2_page, data)
            response1 = opener(request2)
        elif self.rImc.search(url):
            # Login to IMC website
            self.login_page = 'http://project-xtapes.com/main/magazine/login.php'
            values = {'login' : 'Sign In', 'password' : imc_pwd, 'username' : imc_name}

            data = urlencode(values)

            # login page request
            request = urllib2.Request(self.login_page, data)
            response = opener.open(request)


