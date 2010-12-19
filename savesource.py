#!/usr/bin/env python2
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
__email__ = "forod.g@gmail.com"

import re
import shutil
import os
import string
import htmlentitydefs
from os.path import splitext, join
from urlparse import urlparse
import lxml.html
import http_connector


# The regexp we'll need to find the images in the destination directory
rImages = re.compile('\.(jpg|png|gif|jpeg)', re.IGNORECASE) # all most common image files


def extract_domain(url):
    """Given an url extract only the domain name (without 'www' and 'com' for example)"""
    u = urlparse(url)[1].split('.')
    if len(u) > 3: # for tld like co.uk or com.br
        return u[1] + '.' + u[2] + '.' + u[3]
    else:
        return u[1] + '.' + u[2]

def decode_htmlentities(s):
    # Thanks to http://github.com/sku/python-twitter-ircbot/blob/321d94e0e40d0acc92f5bf57d126b57369da70de/html%5Fdecode.py
    def substitute_entity(match):
        ent = match.group(3)
        if match.group(1) == "#":
            # decoding by number
            if match.group(2) == '':
                # number is in decimal
                return unichr(int(ent))
            elif match.group(2) == 'x':
                # number is in hex
                return unichr(int('0x'+ent, 16))
        else:
            # using a name
            cp = htmlentitydefs.name2codepoint.get(ent)
            if cp:
                return unichr(cp)
            else:
                return match.group()
    entity_re = re.compile(r'&(#?)(x?)(\w+);')
    return entity_re.subn(substitute_entity, s)[0]



def save_source(page, basedir, creditor=""):
    """ the method to save the original page link to a file """

    connector = http_connector.Connector()

    page = connector.check_string_or_list(page)

    # get the page's title
    response = connector.reqhandler(page, 1)

    page_title_parsed = lxml.html.fromstring(response)

    neat_title = page_title_parsed.find(".//title").text
    # Clean title from html entities
    neat_title = decode_htmlentities(neat_title)
    # purge the title of troublesome characters
    #neat_title = re.sub('&amp;', '&', neat_title) # &amp; substitution
    accepted_chars = frozenset(string.ascii_letters + string.digits + '(){}[]@-_+"&')
    neat_title = filter(accepted_chars.__contains__, neat_title)

    print(neat_title)

    output_dir = join(basedir, neat_title)

    if os.path.isdir(output_dir):
        os.chdir(output_dir)
    else:
        os.mkdir(output_dir, 0740)
        os.chdir(output_dir)
    # save the source url in a file
    source_file = open('source.txt', "w")
    source_file.write("\n\n\nfonte:%s\n" % page)
    source_file.close()

    # check if we need to save a "credits" file too
    #
    if creditor is not None:
        # get the domain name with its apposite function
        domain_name = extract_domain(page)
        credits_file = open('credits', "w")
        credits_file.write("credits: %s @%s \n" % (creditor, domain_name))
        credits_file.close()

    # move all the images in basedir in the output_dir
    files_in_basedir = os.listdir(basedir)
    for f in files_in_basedir:
        if rImages.search(f):
            src_name = join(basedir, f)
            dst_name = join(output_dir, f)
            # extract the files' extension and make sure all the files have
            # it as lowercase
            dst_filename, dst_ext = splitext(dst_name)
            dst_name = dst_filename + dst_ext.lower()
            if os.path.getsize(src_name) <= 1000:
                # images shorter than 1kb are not really images
                os.remove(src_name)
            else:
                shutil.move(src_name, dst_name)
