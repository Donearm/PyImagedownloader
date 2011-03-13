#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2011, Gianluca Fiore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__email__ = "forod.g@gmail.com"

import re
from urllib import urlretrieve
from os.path import join
import lxml.html
import http_connector


# The regexp we'll need to find the link
RSharenxsThumb = re.compile("http://((www|cache)\.)?sharenxs\.com/thumbnails/sf/", re.IGNORECASE)
# regexp matching a http:// url
RSharenxsUrl = re.compile("http://((www|cache)\.)?sharenxs\.com", re.IGNORECASE)
# Regexp matching a full-sized sharenxs src url
RSharenxsWz = re.compile("http://((www|cache)\.)?sharenxs\.com/images/wz", re.IGNORECASE)


class SharenxsParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            return

        return page

    def sharenxs_get_image_url_and_view(self, page):
        # find the src attribute which contains the real link of sharenxs's images
        view_links = page.xpath("//center/table/tr/td/table/tr/td[@align='center']/a[@href]")

        sharenxs_view = [li.get('href', None) for li in view_links]

        # list comprehension to extract just the correct url
        sharenxs_url = [u for u in sharenxs_view if RSharenxsUrl.search(u)]

        return sharenxs_url, view_links

    def sharenxs_get_image_links_src_and_wz(self, page):
        # find the image url
        src_links = page.xpath('//img[@src]')

        # get all src urls in page
        sharenxs_src = [s.get('src', None) for s in src_links]

        # grab and check if we already have the full-sized image uri
        sharenxs_wz = [w for w in sharenxs_src if RSharenxsWz.search(w)]

        return src_links, sharenxs_src, sharenxs_wz


    def sharenxs_save_image(self, src_list):
        try:
            save_extension = re.split('/', str(src_list[0]))
            savefile = join(self.basedir, str(save_extension[-1]))
            download_url = str(src_list[0])
            try:
                urlretrieve(download_url, savefile)
                return
            except IOError:
                # it's very possible the image isn't available anymore then
                return
        except IndexError:
            return

        
    def parse(self):
        self.page = self.process_url(self.link)

        self.sharenxs_url, self.view_links = self.sharenxs_get_image_url_and_view(self.page)
        
        # check, basing on the content of sharenxs_url, whether we already are 
        # on the page with the full image or not
        if len(self.sharenxs_url) is 0:
            # full page already
            self.view_links = self.page.xpath("//center/table/tr/td[@align='center']/a[@href]/img")
            self.src_links = [li.get('src', None) for li in self.view_links]
            self.sharenxs_save_image(self.src_links)
        else:
            # opening the page with the full-sized image
            self.page = self.process_url(self.sharenxs_url[0])

            self.src_links, self.sharenxs_src, self.sharenxs_wz = self.sharenxs_get_image_links_src_and_wz(self.page)
            if len(self.sharenxs_wz) is not 0:
                try:
                    save_extension = re.split('/', str(self.sharenxs_wz[0]))
                    savefile = join(self.basedir, str(save_extension[-1]))
                    download_url = str(self.sharenxs_wz[0])
                    urlretrieve(download_url, savefile)
                except IndexError:
                    return
            else:
                # in the case we don't have the full-sized uri, we use the thumbnail
                # url to generate the image's url
                self.thumb_src = [s.get('src', None) for s in self.src_links if RSharenxsThumb.search(s.get('src', None))]
                try:
                    # get the extension for the filename
                    save_extension = re.split('nxs-', self.thumb_src[0])
                    savefile = join(self.basedir, str(save_extension[1]))
                    # pick just the src's url part we need
                    sharenxs_split = re.split('thumbnails/sf/', save_extension[0])
                    # and compose the full-sized image url
                    download_url = 'http://cache.sharenxs.com/images/wz/' + sharenxs_split[1] + save_extension[1]
                    urlretrieve(download_url, savefile)
                except IndexError:
                    return
