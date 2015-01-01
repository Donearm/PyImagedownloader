#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2015, Gianluca Fiore
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
__date__ = "03082011"
__email__ = "forod.g@gmail.com"

import sys
import re
import urllib2
import socket
import httplib
import logging
from time import sleep
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
        self.headers = {'User-Agent' : self.user_agent, 'Connection' : 'Keep-Alive'}
        self.timeout = timeout
        #set a cookie handler and install the opener
        self.cj = CookieJar()
        self.opener = self.threadsafe_opener()
        self.logger = logging.getLogger('pyimagedownloader')
        # Set the timeout we chose in the config file
        socket.setdefaulttimeout(self.timeout)

    def threadsafe_opener(self):
        """Generate a new opener with each call, so to be thread-safe"""
        if debug == 1:
            self.logger.setLevel(logging.DEBUG)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj), 
                   urllib2.HTTPHandler(debuglevel=1),
                   urllib2.HTTPSHandler(debuglevel=1),
                   urllib2.HTTPRedirectHandler)
        else:

            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj), 
                    urllib2.HTTPHandler(),
                    urllib2.HTTPSHandler(),
                    urllib2.HTTPRedirectHandler)
        urllib2.install_opener(opener)
        return opener

    def reqhandler(self, url, login=0):
        """the attribute that actually starts the request and return the
        response string"""

        # check if the url given is a string or a list
        self.uri = self.check_string_or_list(url)

        # correctly quote not safe characters in an url
        self.uri = quote(self.uri, safe="%/:=&?~#+!$,;'@()*[]")

        # for some sites we need to login first....
        if login == 1:
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

        login_page = ''
        values = {}

        # Regexps needed
        self.RUsemycomputer = re.compile("http://forum\.usemycomputer\.com/", re.IGNORECASE)
        self.RImc = re.compile("http://(www\.)?(project\-xtapes|imcmagazine)\.com/", re.IGNORECASE)
        self.RCelebrityForum = re.compile("http://(celebrityforum\.)?freeforumzone\.leonardo\.it", re.IGNORECASE)
        self.ROrfaosdoexclusivo = re.compile("http[s]?://www\.orfaosdoexclusivo\.com", re.IGNORECASE)

        # check if url matches one of the sites and prepare the request to log in it
        if self.RUsemycomputer.search(url):
            login_page = 'http://forum.usemycomputer.com/index.php?action=login2'
            values = {'user' : umc_name, 'passwrd' : umc_pwd, 'login' : 'Login'}
        elif self.RImc.search(url):
            login_page = 'http://www.imcmagazine.com/login.php'
            values = {'login' : 'Sign In', 'password' : imc_pwd, 'username' : imc_name}
        elif self.RCelebrityForum.search(url):
#            login_page = 'http://auth.leonardo.it/sso/login'
            login_page = 'http://celebrityforum.freeforumzone.leonardo.it/loginc.aspx?c=3207&f=3207&pbu=%252fforum.aspx%253fc%253d3207%2526f%253d3207'

            values = {'__VIEWSTATE': '/wEPDwUJNDY0NDIzNDMwD2QWAmYPZBYEAgEPZBYIAgEPFgIeB1Zpc2libGVoZAIEDxYCHgdjb250ZW50BUxDZWxlYnJpdHkgRm9ydW0gLSAxMDAlIHNleHkgZSBtYWRlIGluIEl0YWx5IC0gSWwgZm9ydW0gZGVsbGUgY2VsZWJyaXQmIzIyNDsuZAIFDxYCHwEFK0NlbGVicml0eSBGb3J1bSAtIDEwMCUgc2V4eSBlIG1hZGUgaW4gSXRhbHlkAggPFgIfAQUaSWwgZm9ydW0gZGVsbGUgY2VsZWJyaXTDoC5kAgkPZBYIAgUPFgIfAGcWAgIBDxYCHgtjZWxsc3BhY2luZwUBMRYCZg9kFgRmDxYCHgVjbGFzcwUJY3RibGxvZ28xZAIBD2QWAmYPZBYEZg9kFgJmDxYCHgV3aWR0aAUBMWQCAQ9kFgQCAQ8WAh8EBQExZAICDxYEHgdjb2xzcGFuBQExHwQFBDEwMCVkAg8PZBYCAgEPZBYEAgoPFgQeBGhyZWYFHC9yZWdjLmFzcHg/Yz0zMjA3JmFtcDtmPTMyMDceCWlubmVyaHRtbAUkQ2xpY2sgaGVyZSB0byBSZWdpc3RlciBhIG5ldyBhY2NvdW50ZAILDxYEHwYFIS9wYXNzd29yZGMuYXNweD9jPTMyMDcmYW1wO2Y9MzIwNx8HBRlMb3N0IFBhc3N3b3JkPyBDbGljayBoZXJlZAIRD2QWAgICDxYCHgRUZXh0BdUDPCEtLSBiZWdpbiBhZCB0YWcgIC0gdGlsZSA9IDIgLS0+DQo8c2NyaXB0IGxhbmd1YWdlPSJKYXZhU2NyaXB0IiB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPi8vPCEtLQ0KaWYodHlwZW9mKHZfcmFuZG9tbnVtYmVyKT09InVuZGVmaW5lZCIpe3ZhciB2X3JhbmRvbW51bWJlcj1NYXRoLmZsb29yKE1hdGgucmFuZG9tKCkqMTAwMDAwMDAwMDApfQ0KaWYodHlwZW9mKHZfdGlsZSk9PSJ1bmRlZmluZWQiKXt2YXIgdl90aWxlPTF9ZWxzZXt2X3RpbGUrK30NCmRvY3VtZW50LndyaXRlKCc8Jysnc2NyJysnaXB0IHNyYz0iaHR0cDovL2FkLml0LmRvdWJsZWNsaWNrLm5ldC9hZGovZmZ6b25lL2NpbmVtYTt0aWxlPScrdl90aWxlKyc7c3o9MzAweDI1MDtvcmQ9Jyt2X3JhbmRvbW51bWJlcisnPyIgdHlwZT0idGV4dC9qYXZhc2NyaXB0Ij48XC8nKydzY3InKydpcHQ+Jyk7DQovLy0tPjwvc2NyaXB0Pg0KPCEtLSBFbmQgYWQgdGFnIC0tPmQCGQ9kFgICAQ9kFgJmDxBkZBQrAQBkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBSdjdGwwMCRDUEgxJExvZ2luQ29udHJvbCRMb2dpblBlcm1hbmVudGUFI2N0bDAwJENQSDEkTG9naW5Db250cm9sJExvZ2luU2ljdXJvBSVjdGwwMCRDUEgxJExvZ2luQ29udHJvbCRMb2dpbk5hc2Nvc3Rv+omcpM+HLM4mDkZ1qLfzOnIz+CpGg5ri5iQOrMVnTHk=',
                    'ctl00$CPH1$LabPBUrl': '%2fforum.aspx%3fc%3d3207%26f%3d3207', 'ctl00$CPH1$LoginControl$TUsername': cf_name,
                    'ctl00$CPH1$LoginControl$TPassword': cf_pwd, 'ctl00$CPH1$LoginControl$ButLogin': 'Log In'}
#            values = {'SSO_cik': 'G9clW564v319FjXGuTXXOVzSKDrUTFAXfI8M0uDx2EoxYiBekWLO7M6fMu99MlpQ',
#                    'SSO_USERNAME': cf_name, 'SSO_PASSWORD': cf_pwd, 'SSO_p': 'c',
#                    'SSO_CHANNEL': '3', 'SSO_PAUTH': '0', 'SSO_USE_ENC': '0',
#                    'SSO_PAYLOAD': '1', 'SSO_SECURE_LOGIN': '1', 'FFZ_LOGIN_RQ': '1',
#                    'FFZ_SLOGIN': '1', 'FFZ_HLOGIN': '0', 'SSO_REDIRECT_PATH': login_page}
        elif self.ROrfaosdoexclusivo.search(url):
            login_page = 'https://www.orfaosdoexclusivo.com/forum/index.php?app=core&module=global&section=login&do=process'
            values = {'username': orfaos_name, 'password': orfaos_pwd}
        else:
            self.logger.error("%s didn't match any know login-provided site" % url)
            return

        # encode values
        data = urlencode(values)

        request = urllib2.Request(login_page, data)

        try:
            response = self.opener.open(request)
        except urllib2.HTTPError as e:
            if e.code == 408:
                # request timed-out, wait a sec and retry
                sleep(1)
                response = self.opener.open(request)

    def post_request(self, url, data, headers, referer=''):
        request = urllib2.Request(url, data, headers)
        request.add_header('Accept', '*/*')
        if referer:
            request.add_header('Referer', referer)
        attempts = 0
        while attempts < 10:
            try:
                response = self.opener.open(request, data)
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
                    self.logger.warning("%s couldn't be found, skipping it..." % url)
#                    print("%s couldn't be found, skipping it..." % url)
                    return response
                else:
                    print(e.code)
            except urllib2.URLError as e:
                attempts += 1
                print(e.reason)
            except socket.error as e:
                attempts += 1
                print(e)

        self.logger.error("10 tries weren't enough to download %s ..." % url)
#        print("An image couldn't be downloaded.")
        response = ''
        return response

    def get_request(self, url, ua, referer=''):
        request = urllib2.Request(url)
        request.add_header('User-Agent', ua)
        request.add_header('Accept', '*/*')
        if referer:
            request.add_header('Referer', referer)
        attempts = 0
        while attempts < 10:
            try:
                response = self.opener.open(request, None)
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
                    self.logger.warning("%s couldn't be found, skipping it..." % url)
#                    print("%s couldn't be found, skipping it..." % url)
                    return response
                else:
                    print(e.code)
            except urllib2.URLError as e:
                attempts += 1
                print(e.reason)
            except socket.error as e:
                attempts += 1
                print(e)

        self.logger.error("10 tries weren't enough to download %s ..." % url)
#        print("An image couldn't be downloaded.")
        response = ''
        return response

    def get_filename(self, url, split=''):
        request = urllib2.Request(url)
        request.add_header('User-Agent', self.user_agent)
        try:
            response = self.opener.open(request)
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
