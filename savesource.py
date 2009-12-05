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
__email__ = "forod.g@gmail.com"

import re
import shutil
import os
import urllib2
import string
import htmlentitydefs
from os.path import splitext
from urllib import urlretrieve, urlencode
from BeautifulSoup import BeautifulSoup


# The regexp we'll need to find the link
rImages = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # image files

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def extract_domain(url):
    """Given an url extract only the domain name (without 'www' and 'com' for example)"""
    domain = re.split('\.', url)
    return domain[1]

def strip_html_entities(text):
    """Removes HTML or XML character references and entities from a string"""
    def fix(m):
        text = m.group(0)
        if text[:2] == "&#":
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text
    return re.sub("&#?\w+;", fix, text)

def htmlentitydecode(s):
    # Thanks to http://sebsauvage.net/python/snyppets/
    # First convert alpha entities (such as &oacute;)
    def entity2char(m):
        entity = m.group(1)
        if entity in htmlentitydefs.name2codepoint:
            return unichr(htmlentitydefs.name2codepoint[entity])
        return u" " # empty space for unknown entities
    t = re.sub(u'&(%s);' % u'|'.join(htmlentitydefs.name2codepoint), entity2char, s)

    # Convert numerical entities (such as &#233;)
    t = re.sub(u'&#(\d+);', lambda x: unichr(int(x.group(1))), t)

    # Lastly convert hexadecimal entities (such as &#x00E9;)
    return re.sub(u'&#x(\w+);', lambda x: unichr(int(x.group(1), 16)), t)



def save_source(page, creditor=""):
    """ the method to save the original page link to a file """

    # get the page's title
    request = urllib2.Request(page, data, headers)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        if e.code == 405:
            request = urllib2.Request(page)
            request.add_header('User-Agent', user_agent)
            response = urllib2.urlopen(request)
        else:
            print("Some error happened")
            print(e.code)
            print(e.reason)

    page_title = response.read()
    page_title_soup = BeautifulSoup(page_title)

    # purge the title of troublesome characters
    neat_title = re.sub('quot;', '"', page_title_soup.title.string) # &quot; substitution
    neat_title = re.sub('&amp;', '&', neat_title) # &amp; substitution
    accepted_chars = frozenset(string.ascii_letters + string.digits + '(){}[]@-_+"&')
    neat_title = filter(accepted_chars.__contains__, neat_title)

    # Clean title from html entities (not quite working)
    #neat_title = strip_html_entities(neat_title)
    #neat_title = htmlentitydecode(neat_title)

    print neat_title
    output_dir = basedir + neat_title

    if os.path.isdir(output_dir):
        os.chdir(output_dir)
    else:
        os.mkdir(output_dir, 0740)
        os.chdir(output_dir)
    # save the source url in a file
    source_file = open('source.txt', "w")
    source_file.write("\n\n\n" + 'fonte:' + page + "\n")
    source_file.close()

    # check if we need to save a "credits" file too
    #
    if creditor is not None:
        # get the domain name with its apposite function
        domain_name = extract_domain(page)
        credits_file = open('credits', "w")
        credits_file.write('credits: ' + creditor + ' @' + domain_name + "\n")
        credits_file.close()

    # move all the images in basedir in the output_dir
    files_in_basedir = os.listdir(basedir)
    for f in files_in_basedir:
        if rImages.search(f):
            src_name = os.path.join(basedir, f)
            dst_name = os.path.join(output_dir, f)
            # extract the files' extension and make sure all the files have
            # it as lowercase
            dst_filename, dst_ext = splitext(dst_name)
            dst_name = dst_filename + dst_ext.lower()
            shutil.move(src_name, dst_name)

