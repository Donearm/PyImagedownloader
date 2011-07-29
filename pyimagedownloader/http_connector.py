#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2011, Gianluca Fiore
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
import socket
import httplib
from cookielib import CookieJar
from urllib import urlencode, quote
# importing config file variables
from pyimg import *



class Connector():
    """connect to a url, get the page and return its content"""
    def __init__(self):
        # Some variables for the connection
        self.values = {}
        self.user_agent = user_agent
        self.headers = { 'User-Agent' : self.user_agent, 'Connection' : 'Keep-Alive' }
        self.timeout = timeout
        # Set the timeout we chose in the config file
        socket.setdefaulttimeout(self.timeout)


        #set a cookie handler and install the opener
        self.cj = CookieJar()

    def threadsafe_opener(self):
        """Generate a new opener with each call, so to be thread-safe"""
        if debug == 1:
           opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj), 
                   urllib2.HTTPHandler(debuglevel=1),
                   urllib2.HTTPSHandler(debuglevel=1))
        else:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj), 
                    urllib2.HTTPHandler(),
                    urllib2.HTTPSHandler())
        return opener
#        urllib2.install_opener(opener)


    def reqhandler(self, url, login=0):
        """the attribute that actually starts the request and return the
        response string"""

        # check if the url given is a string or a list
        self.uri = self.check_string_or_list(url)

        # correctly quote not safe characters in an url
        self.uri = quote(self.uri, safe="%/:=&?~#+!$,;'@()*[]")

        # for some sites we need to login first....
        if login == 1:
            urllib2.install_opener(self.threadsafe_opener())
            self.site_login(self.uri)

        if self.values:
            # Encode values (if any)
            self.data = urlencode(self.values)
            # if there are some values it's a POST request
            self.response = self.post_request(self.uri, self.data, self.user_agent)
        else:
            # no values, then it's a GET request
            self.response = self.get_request(self.uri, self.user_agent)

        return self.response


        #print(cj.make_cookies(self.response, self.request)) # show the cookies
#         self.Rpage = self.response.read()
#         return self.Rpage


    def site_login(self, url):
        """check if it's a site or forum we have login credentials for and
        log-in"""

        # Regexps needed
        self.RUsemycomputer = re.compile("http://forum\.usemycomputer\.com/", re.IGNORECASE)
        self.RImc = re.compile("http://www\.(project\-xtapes|imcmagazine)\.com/", re.IGNORECASE)
        self.RCelebrityForum = re.compile("http://(celebrityforum\.)?freeforumzone\.leonardo\.it", re.IGNORECASE)
        self.ROrfaosdoexclusivo = re.compile("http[s]?://www\.orfaosdoexclusivo\.com", re.IGNORECASE)

        if self.RUsemycomputer.search(url):
            # We got a login user/pwd for usemycomputer, let's first login then
            login2_page = 'http://forum.usemycomputer.com/index.php?action=login2'
            values = {'user' : umc_name, 'passwrd' : umc_pwd, 'login' : 'Login'}

            # encode values
            data = urlencode(values)

            # second request to the login2 page
            opener = self.threadsafe_opener()
            urllib2.install_opener(opener)
            request2 = urllib2.Request(login2_page, data)
            response1 = opener.open(request2)
        elif self.RImc.search(url):
            # Loging to IMC website
            login_page = 'http://www.imcmagazine.com/login.php'
            values = {'login' : 'Sign In', 'password' : imc_pwd, 'username' : imc_name}

            data = urlencode(values)

            # login page request
            opener = self.threadsafe_opener()
            urllib2.install_opener(opener)
            request = urllib2.Request(login_page, data)
            response = opener.open(request)
        elif self.RCelebrityForum.search(url):
            login_page = 'http://celebrityforum.freeforumzone.leonardo.it/loginc.aspx'
            auth_page = 'http://auth.leonardo.it/sso/login'


            values = {'SSO_cik': 'G9clW564v319FjXGuTXXOVzSKDrUTFAXfI8M0uDx2EoxYiBekWLO7M6fMu99MlpQ',
                    'SSO_USERNAME': cf_name, 'SSO_PASSWORD': cf_pwd, 'SSO_p': 'c',
                    'SSO_CHANNEL': '3', 'SSO_PAUTH': '0', 'SSO_USE_ENC': '0',
                    'SSO_PAYLOAD': '1', 'SSO_SECURE_LOGIN': '1', 'FFZ_LOGIN_RQ': '1',
                    'FFZ_SLOGIN': '1', 'FFZ_HLOGIN': '0', 'SSO_REDIRECT_PATH': login_page}
            
            data = urlencode(values)

            opener = self.threadsafe_opener()
            urllib2.install_opener(opener)
            request = urllib2.Request(auth_page, data)
            response = opener.open(request)
        elif self.ROrfaosdoexclusivo.search(url):
            login_page = 'https://www.orfaosdoexclusivo.com/forum/index.php?app=core&module=global&section=login&do=process'
            values = {'username': orfaos_name, 'password': orfaos_pwd}

            data = urlencode(values)

            opener = self.threadsafe_opener()
            urllib2.install_opener(opener)
            request = urllib2.Request(login_page, data)
            response = opener.open(request)

    def post_request(self, url, data, headers, referer=''):
        request = urllib2.Request(url, data, headers)
        opener = self.threadsafe_opener()
        urllib2.install_opener(opener)
        request.add_header('Accept', '*/*')
        if referer:
            request.add_header('Referer', referer)
        attempts = 0
        while attempts < 10:
            try:
                response = opener.open(request, data)
                # various infos on the response
                #print(response.info())
                #print(response.geturl())
                #print(response.getcode())
                return response.read()
            except httplib.InvalidURL as e:
                # url is not valid!
                response = ''
                return response
            except httplib.IncompleteRead as e:
                attempts += 1
            except httplib.BadStatusLine as e:
                # server replies with an unknown HTTP status code
                attempts +=1
            except urllib2.HTTPError as e:
                attempts += 1
                response = ''
                if e.code == 405:
                    # we were wrong, the url doesn't accept a POST, make a GET
                    # then
                    response = self.get_request(url, self.user_agent)
                elif e.code == 404:
                    # url non-existing, just go on
                    print("%s couldn't be found, skipping it..." % url)
                    return response
                else:
                    print(e.code)
            except urllib2.URLError as e:
                attempts += 1
                print(e.reason)
            except socket.error as e:
                attempts += 1
                print(e)

        print("An image couldn't be downloaded.")
        response = ''
        return response


    def get_request(self, url, ua, referer=''):
        request = urllib2.Request(url)
        opener = self.threadsafe_opener()
        urllib2.install_opener(opener)
        request.add_header('User-Agent', ua)
        request.add_header('Accept', '*/*')
        if referer:
            request.add_header('Referer', referer)
        attempts = 0
        while attempts < 10:
            try:
                response = opener.open(request, None)
#                print(request.header_items())
#                print(request.unredirected_hdrs)
                return response.read()
            except httplib.InvalidURL as e:
                # url is not valid!
                response = ''
                return response
            except httplib.IncompleteRead as e:
                attempts += 1
                self.get_request(url, ua)
            except httplib.BadStatusLine as e:
                # server replies with an unknown HTTP status code
                attempts +=1
            except urllib2.HTTPError as e:
                attempts += 1
                response = ''
                if e.code == 404:
                    # url non-existing, just go on
                    print("%s couldn't be found, skipping it..." % url)
                    return response
                else:
                    print(e.code)
            except urllib2.URLError as e:
                attempts += 1
                print(e.reason)
            except socket.error as e:
                attempts += 1
                print(e)

        print("An image couldn't be downloaded.")
        response = ''
        return response


    def get_filename(self, url, split=''):
        request = urllib2.Request(url)
        opener = self.threadsafe_opener()
        urllib2.install_opener(opener)
        request.add_header('User-Agent', self.user_agent)
        try:
            response = opener.open(request)
            try:
                self.filename = response.headers['Content-Disposition'].split('=')[1]
                # remove single or double quotes from the filename
                if self.filename[0] == '"' or self.filename[0] == "'":
                    self.filename = self.filename[1:-1]
                return self.filename
            except:
                # no Content-Disposition header, make filename from url
                # if a split string has been given
                if split:
                    self.filename = re.split(split, url)
                    return self.filename
                else:
                    return
        except:
            # it's possible that the url is currently not available,
            # use the url and the split string then
            self.filename = re.split(split, url)
            return self.filename


    def check_string_or_list(self, url):
        """check if the url given is a string or a list and always returns a
        correct url"""
        if isinstance(url, str):
            uri = url
            return uri
        elif isinstance(url, list):
            uri = url[0]
            return uri
        else:
            # something else has been passed, exiting
            sys.exit(1)
