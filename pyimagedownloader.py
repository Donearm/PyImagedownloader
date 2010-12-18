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
__version__ = "1.4"
__date__ = "17122010"
__email__ = "forod.g@gmail.com"

import sys
import re
import fileinput
from optparse import OptionParser
from os.path import abspath, dirname
from os import rename
import lxml.html
# importing local modules
import savesource, imageshack, imagevenue, uppix, imagehaven, imagebam, \
        imagetitan, bellazon, skinsbe, shareapic, storeimgs, upmyphoto, \
        sharenxs, blogspot, postimage, imageupper, imagesocket, photobucket, \
        imageban, imagehostorg, turboimagehost, usemycomputer, wordpress
import http_connector
import pygui
# importing config file variables
from pyimg import basedir





# The regexp we'll need to find the link
rHttp = re.compile("http://", re.IGNORECASE)
rImagevenue = re.compile("http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rImagebam = re.compile("http://www\.imagebam\.com/image/", re.IGNORECASE)
rImagehaven = re.compile("http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
rImageshack = re.compile("http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
rUpmyphoto = re.compile("http://(www\.)?upmyphoto\.com", re.IGNORECASE)
rUppix = re.compile("http://www\.uppix\.info", re.IGNORECASE)
rBellazon = re.compile("http://www\.bellazon\.com/", re.IGNORECASE)
rSkinsBe = re.compile("http://image\.skins\.be", re.IGNORECASE)
rShareapic = re.compile("http://www\.shareapic\.net/content\.php\?id", re.IGNORECASE)
rStoreimgs = re.compile("http://storeimgs\.com", re.IGNORECASE)
rImagetitan = re.compile("http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
rSharenxs = re.compile("http://(www\.)?sharenxs\.com/view/\?", re.IGNORECASE)
rBlogspot = re.compile("http://[0-9]\.bp\.blogspot\.com", re.IGNORECASE)
rPostimage = re.compile("http://(www\.)?postimage\.org/image/", re.IGNORECASE)
rImageUpper = re.compile("http://imageupper\.com/i/", re.IGNORECASE)
rImageSocket = re.compile("http://(www\.)?imagesocket\.com", re.IGNORECASE)
rPhotobucket = re.compile("http://[a-z0-9]+\.photobucket\.com", re.IGNORECASE)
rImageban = re.compile("http://[a-z0-9]+\.imageban\.ru", re.IGNORECASE)
rImagehostorg = re.compile("http://[a-z0-9]+\.imagehost\.org", re.IGNORECASE)
rTurboimagehost = re.compile("http://www\.turboimagehost\.com", re.IGNORECASE)
rUsemycomputer = re.compile("http://usemycomputer\.com/show\.html\?i=\/indeximages", re.IGNORECASE)
rWordpress = re.compile("http://.*.wordpress\.com/[0-9]+/[0-9]+/.*\.[a-z]{,4}", re.IGNORECASE)
rWordpressuploads = re.compile("http://.*/wp-content/uploads/.*\.[a-z]{,4}", re.IGNORECASE)





# Main parser class
class ImageHostParser():
    """ The main parser class """

    def __init__(self, page, tag, attr):
        self.page = lxml.html.fromstring(page)
        self.tag = tag
        self.attr = attr
# iterlinks() gets all links on the page but it's slower than using xpath
# (because it catches a whole lot more links)
#        self.linklist = []
#        for L in self.page.iterlinks():
#            if rHttp.search(L[2]):
#                self.linklist.append(L[2])
#        print(self.linklist)
        self.which_host(tag, attr)

    def which_host(self, tag, attr):
        xpath_search = '//' + tag + '[@' + attr + ']'
        all_tags = self.page.xpath(xpath_search)
        n = 0
        for L in all_tags:
            stringl = str(L.get(attr, None))
            if rImagevenue.search(stringl):
                imagevenue.imagevenue_parse(stringl, basedir)
                n = n + 1
            elif rImagebam.search(stringl):
                imagebam.imagebam_parse(stringl, basedir)
                n = n + 1
            elif rImagehaven.search(stringl):
                imagehaven.imagehaven_parse(stringl, basedir)
                n = n + 1
            elif rImageshack.search(stringl):
                imageshack.imageshack_parse(stringl, basedir)
                n = n + 1
            elif rUpmyphoto.search(stringl):
                upmyphoto.upmyphoto_parse(stringl, basedir)
                n = n + 1
            elif rUppix.search(stringl):
                uppix.uppix_parse(stringl, basedir)
                n = n + 1
            elif rBellazon.search(stringl):
                not_supported('Bellazon')
                #bellazon.bellazon_parse(L, basedir)
                n = n + 1
            elif rSkinsBe.search(stringl):
                skinsbe.skinsbe_parse(stringl, basedir)
                n = n + 1
            elif rShareapic.search(stringl):
                shareapic.shareapic_parse(stringl, basedir)
                n = n + 1
            elif rStoreimgs.search(stringl):
                storeimgs.storeimgs_parse(stringl, basedir)
                n = n + 1
            elif rImagetitan.search(stringl):
                imagetitan.imagetitan_parse(stringl, basedir)
                n = n + 1
            elif rSharenxs.search(stringl):
                sharenxs.sharenxs_parse(stringl, basedir)
                n = n + 1
            elif rBlogspot.search(stringl):
                blogspot.blogspot_parse(stringl, basedir)
                n = n + 1
            elif rPostimage.search(stringl):
                #not_supported('Postimage')
                postimage.postimage_parse(stringl, basedir)
                n = n + 1
            elif rImageUpper.search(stringl):
                imageupper.imageupper_parse(stringl, basedir)
                n = n + 1
            elif rImageSocket.search(stringl):
                imagesocket.imagesocket_parse(stringl, basedir)
                n = n + 1
            elif rPhotobucket.search(stringl):
                photobucket.photobucket_parse(stringl, basedir)
                n = n + 1
            elif rImageban.search(stringl):
                imageban.imageban_parse(stringl, basedir)
                n = n + 1
            elif rImagehostorg.search(stringl):
                imagehostorg.imagehostorg_parse(stringl, basedir)
                n = n + 1
            elif rTurboimagehost.search(stringl):
                turboimagehost.turboimagehost_parse(stringl, basedir)
                n = n + 1
            elif rUsemycomputer.search(stringl):
                usemycomputer.usemycomputer_parse(stringl, basedir)
                n = n + 1
            elif rWordpress.search(stringl) or rWordpressuploads.search(stringl):
                wordpress.wordpress_parse(stringl, basedir)
                n = n + 1
            else:
                continue
        print("%d images were present" % n)



# Generate the argument parser
def argument_parser():
    usage_message = "usage: %prog [options] url"
    cli_parser = OptionParser(usage=usage_message)
    cli_parser.add_option("-c", "--credit",
            help="optionally save the name of the poster of the images in a file",
            dest="poster")
    cli_parser.add_option("-e", "--embed",
            action="store_true",
            help="enable search for embedded images too",
            dest="embed")
    cli_parser.add_option("-d", "--directory",
            help="the directory where to save images",
            dest="savedirectory")
    cli_parser.add_option("-g", "--gui",
            action="store_true",
            help="start in gui mode",
            dest="gui")
    cli_parser.add_option("-f", "--filelist",
            help="a file containing the urls to be downloaded, one per row",
            dest="filelist")
    (options, args) = cli_parser.parse_args()
    return options.poster, options.embed, options.gui, options.savedirectory, options.filelist , args

# print an advice for hosts not supported
def not_supported(host):
    msg = "Sorry but %s isn't supported or isn't working right now" % host
    print(msg)


def download_url(url, savedirectory, embed="", poster=""):
    """Main function to parse and download images"""
    
    connector = http_connector.Connector()
    Rpage = connector.reqhandler(url, 1)


    # Parse the page for images
    parser = ImageHostParser(Rpage, 'a', 'href')
    if embed:
        # do we need to search for embedded images then?
        # Note: at the moment it downloads thumbnails too
        print("Searching for embedded images")
        print("")
        parser.which_host('img', 'src')

    # Generate the directory for the source file and the images downloaded
    savesource.save_source(url, savedirectory, creditor=poster)

def filelist_parse(file):
    """parsing a file containing urls and giving back a list of them"""
    file = open(abspath(file), 'r')
    return file.readlines()

def filelist_download(file):
    """download a serie of urls from a file and comment out them, in another file, as
    they are being downloaded."""
    bckp = dirname(abspath(file)) + '/' + 'list.bak'
    with open(abspath(file), 'rw') as f:
        # save every line in the filelist
        whole_f = f.readlines()
        # initiate a list for the downloaded and commented urls
        bckp_l = []
        with open(bckp, 'w') as o:
            for u in whole_f:
                if u.startswith('#'):
                    # a previously downloaded url? Just save it
                    bckp_l.append(u)
                    o.write(u)
                else:
                    try:
                        download_url(u.strip("\n"), basedir, embed, poster)
                    except:
                        # if anything goes wrong, add the not downloaded urls to the filelist,
                        # uncommented, and exit
                        downloaded_l = [i for i in whole_f if i not in bckp_l]
                        for i in downloaded_l:
                            o.write(i)
                        sys.exit(0)
                    bckp_l.append(u)
                    url = '#' + u
                    o.write(url)
    # at the end, move the backup file to the filelist's place
    rename(abspath(o.name), abspath(f.name))


def filelist_fileinput(file):
    """download a serie of urls from a file, commenting them as they are being
    downloaded (using fileinput)"""
    f = fileinput.input(abspath(file), inplace=1)
    for line in f:
        try:
            download_url(line, basedir, embed, poster)
        except:
            # print the line where it stopped
            print(line)
            # if anything goes wrong, exit without further touching the filelist
            sys.exit(0)
        l = '#' + line
        print(l.strip("\n"))

if __name__ == "__main__":
    (poster, embed, gui, savedirectory, filelist, url) = argument_parser()

    if savedirectory:
        # directory given on the command line?
        basedir = abspath(savedirectory)

    if filelist:
        filelist_download(filelist)

        # exit now, we don't need to start the gui in this case
        sys.exit(0)

    # do we want a gui?
    if gui:
        pygui = pygui.Gui(basedir, embed, poster)
    else:
        # no gui then
        download_url(url, basedir, embed, poster)

    sys.exit(0)
