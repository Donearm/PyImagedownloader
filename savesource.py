#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
"""
"""
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__email__ = "forod.g@gmail.com"

import re
import shutil
import os
import urllib2
from urllib import urlretrieve, urlencode
from BeautifulSoup import BeautifulSoup, SoupStrainer


# The regexp we'll need to find the link
rImages = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # image files

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

values = {}
user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'
headers = { 'User-Agent' : user_agent }
data = urlencode(values)

def save_source(page):
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
    neat_title = re.sub('[\|\.\&\,\'\:\!\@\/]', '', page_title_soup.title.string)
    # and substitutes spaces with underscores
    neat_title = re.sub('\s', '_', neat_title)
    neat_title = re.sub('quot;', '', neat_title) # &quot; removing
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
    # move all the images in basedir in the output_dir
    files_in_basedir = os.listdir(basedir)
    for f in files_in_basedir:
        if rImages.search(f):
            src_name = os.path.join(basedir, f)
            dst_name = os.path.join(output_dir, f)
            shutil.move(src_name, dst_name)

