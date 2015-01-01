#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2015, Gianluca Fiore
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

import random
import string
from urllib import urlretrieve
from os.path import join, exists, splitext
import lxml.html
import logging
import http_connector


class ImagebamParse():

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.connector = http_connector.Connector()
        self.logger = logging.getLogger('pyimagedownloader')

    def process_url(self, url):
        response = self.connector.reqhandler(url)

        try:
            self.page = lxml.html.fromstring(response)
        except lxml.etree.XMLSyntaxError as e:
            # most of the time we can simply ignore parsing errors
            self.logger.error("XMLSyntaxError at %s " % url)
            return

        return self.page

    def imagebam_get_image_src_and_name(self, page):
        # find the src attribute which contains the real link of imagebam's 
        # images
        src_links = page.xpath("//img[@onclick='scale(this);']")

        imagebam_src = [li.get('src', None) for li in src_links]

        # get the image name from the Content-Disposition header
        try:
            imagename = self.connector.get_filename(imagebam_src[0], 'filename=')
        except IndexError:
            # sometimes Imagebam server go offline, skip this image
            self.logger.warning("IndexError in %s" % imagebam_src)
            return

        return imagebam_src, imagename

    def imagebam_save_image(self, src_list, imagename):

        download_url = src_list[0]
        try:
            savefile = join(self.basedir, imagename)
        except UnicodeEncodeError:
            # encode with utf8 files with non-ascii characters in their name
            savefile = join(self.basedir, imagename.encode("utf-8"))
        except UnicodeDecodeError:
            # catch bad characters and try to replace them with correct utf8 chars
            savefile = join(self.basedir, imagename.decode('utf8', 'replace'))
        except AttributeError:
            # perhaps we have used the split in getting an imagename and thus
            # we now have a list and not a string
            savefile = join(self.basedir, imagename[-1])

        # correctly rename filenames with missing or partial extension
        root, ext = splitext(savefile)
        if ext == '.':
            savefile = savefile + 'jpg'
        elif ext == '.j':
            savefile = savefile + 'pg'
        elif ext == '':
            savefile = savefile + '.jpg'
        else:
            pass

        # finally save the image in the desidered directory
        if not exists(savefile):
            try:
                urlretrieve(download_url, savefile) 
            except IOError as e:
                self.logger.warning("%s not loading" % download_url)
                # image not loading, skipping it
                return
        else:
            randstring = ''.join(random.choice(string.lowercase) for i in range(5))
            try:
                savefile = join(self.basedir, randstring + imagename)
            except UnicodeEncodeError:
                savefile = join(self.basedir, randstring + imagename.encode("uft-8"))
            except AttributeError:
                savefile = join(self.basedir, randstring + imagename[-1])
            except TypeError:
                savefile = join(self.basedir, randstring + imagename[-1])
            try:
                urlretrieve(download_url, savefile)
            except IOError as e:
                self.logger.error("Unable to save %s" % savefile)
                return

    def parse(self):
        self.page = self.process_url(self.link)

        self.imagebam_src, self.imagename = self.imagebam_get_image_src_and_name(self.page)
        self.imagebam_save_image(self.imagebam_src, self.imagename)
