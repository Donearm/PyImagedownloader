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
__version__ = "1.5"
__date__ = "25122010"
__email__ = "forod.g@gmail.com"

import sys
import re
import fileinput
from multiprocessing import Process, Queue
from optparse import OptionParser
from os.path import abspath, dirname
from os import rename
import lxml.html
# importing local modules
import savesource, imageshack, imagevenue, uppix, imagehaven, imagebam, \
        imagetitan, bellazon, skinsbe, shareapic, upmyphoto, \
        sharenxs, blogspot, postimage, imageupper, imagesocket, photobucket, \
        imageban, imagehostorg, turboimagehost, usemycomputer, wordpress, \
        imageboss, servimg
import http_connector
import pygui
# importing config file variables
from pyimg import basedir, numprocs



# print an advice for hosts not supported
def not_supported(host):
    msg = "Sorry but %s isn't supported or isn't working right now" % host
    print(msg)


# The regexp we'll need to find the link
rHttp = re.compile("http://", re.IGNORECASE)
rImagevenue = re.compile("http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rImagebam = re.compile("http://www\.imagebam\.com/image/", re.IGNORECASE)
rImagehaven = re.compile("http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
rImageshack = re.compile("http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
rPostimage = re.compile("http://(www\.)?postimage\.org/image/", re.IGNORECASE)
rSharenxs = re.compile("http://(www\.)?sharenxs\.com/view/\?", re.IGNORECASE)
rBlogspot = re.compile("http://[0-9]\.bp\.blogspot\.com", re.IGNORECASE)
rUpmyphoto = re.compile("http://(www\.)?upmyphoto\.com", re.IGNORECASE)
rUppix = re.compile("http://www\.uppix\.info", re.IGNORECASE)
rBellazon = re.compile("http://www\.bellazon\.com/main/index\.php\?s=[a-z0-9]+&act=attach", re.IGNORECASE)
rSkinsBe = re.compile("http://image\.skins\.be", re.IGNORECASE)
rShareapic = re.compile("http://www\.shareapic\.net/content\.php\?id", re.IGNORECASE)
rImagetitan = re.compile("http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
rImageUpper = re.compile("http://imageupper\.com/i/", re.IGNORECASE)
rImageSocket = re.compile("http://(www\.)?imagesocket\.com", re.IGNORECASE)
rPhotobucket = re.compile("http://[a-z0-9]+\.photobucket\.com", re.IGNORECASE)
rImageban = re.compile("http://[a-z0-9]+\.imageban\.ru", re.IGNORECASE)
rImagehostorg = re.compile("http://[a-z0-9]+\.imagehost\.org", re.IGNORECASE)
rTurboimagehost = re.compile("http://www\.turboimagehost\.com/p/", re.IGNORECASE)
rUsemycomputer = re.compile("http://usemycomputer\.com/show\.html\?i=\/indeximages", re.IGNORECASE)
rWordpress = re.compile("http://.*.wordpress\.com/[0-9]+/[0-9]+/.*\.[a-z]{,4}", re.IGNORECASE)
#rWordpress = re.compile("http://.*.wordpress\.com/[0-9]+/[0-9]+/.*\.[a-z]{,4}(\?w=[0-9]+\&amp\;h=[0-9]+)?", re.IGNORECASE)
rWordpressuploads = re.compile("http://.*/wp-content/uploads/.*\.[a-z]{,4}", re.IGNORECASE)
rImageboss = re.compile("http://www\.imageboss\.net", re.IGNORECASE)
rServimg = re.compile("http://www\.servimg\.com", re.IGNORECASE)
# putting them all in a dictionary
regexp_dict = {rImagevenue : imagevenue.ImagevenueParse,
        rImagebam : imagebam.ImagebamParse,
        rImagehaven : imagehaven.ImagehavenParse,
        rImageshack : imageshack.ImageshackParse,
        rPostimage : postimage.PostimageParse,
        rSharenxs : sharenxs.SharenxsParse,
        rBlogspot : blogspot.BlogspotParse,
        rUpmyphoto : upmyphoto.UpmyphotoParse,
        rUppix : uppix.UppixParse,
        rBellazon : bellazon.BellazonParse,
        rSkinsBe : skinsbe.SkinsbeParse,
        rShareapic : shareapic.ShareapicParse,
        rImagetitan : imagetitan.ImagetitanParse,
        rImageUpper : imageupper.ImageupperParse,
        rImageSocket : imagesocket.ImagesocketParse,
        rPhotobucket : photobucket.PhotobucketParse,
        rImageban : imageban.ImagebanParse,
        rImagehostorg : imagehostorg.ImagehostorgParse,
        rTurboimagehost : turboimagehost.TurboimagehostParse,
        rUsemycomputer : usemycomputer.UsemycomputerParse,
        rWordpress : wordpress.WordpressParse,
        rWordpressuploads : wordpress.WordpressParse,
        rImageboss : imageboss.ImagebossParse,
        rServimg : servimg.ServimgParse
        }



# Main parser class
class ImageHostParser():
    """ The main parser class """

    def __init__(self, page, tag, attr, basedir):
        self.page = lxml.html.fromstring(page)
        self.tag = tag
        self.attr = attr
        self.basedir = basedir
        self.numprocs = numprocs
# iterlinks() gets all links on the page but it's slower than using xpath
# (because it catches a whole lot more links)
#        self.linklist = []
#        for L in self.page.iterlinks():
#            if rHttp.search(L[2]):
#                self.linklist.append(L[2])
#        print(self.linklist)
        self.urllist = self.get_all_links(self.tag, self.attr)
        self.which_host(self.urllist, self.attr)

    def which_host(self, urllist, attr):
        """check every url in the given list against all regular expressions
        and extract the value of the chosen html attribute.
        Then use a queue and enough processes to download all matched urls"""
        # make a numeric index, a queue and enough processes as numprocs
        n = 0
        self.q = Queue()
        self.ps = [ Process(target=self.use_queue, args=()) for i in range(self.numprocs) ]

        for p in self.ps:
            # start all processes
            p.start()
        
        # piping the urllist urls into a set to purge duplicates
        finalset = set()
        for L in urllist:
            self.stringl = str(L.get(attr, None))
            finalset.add(self.stringl)


        for L in finalset:
            # iterate over the regexp dictionary items; when finding a url
            # matching, put the method, url and self.basedir in the queue
            for k, v in regexp_dict.items():
                if k.search(L):
                    parser = v(L, self.basedir)
                    self.q.put((parser.parse()))
#                    self.q.put((v, (L, self.basedir)))
                    n = n + 1
                else:
                    continue

        for i in range(self.numprocs):
            # put a STOP to end the iter builtin inside use_queue
            self.q.put("STOP")

        print("%d images were present" % n)

    def use_queue(self):
        """use up the queue by running all its elements"""
        for method in iter(self.q.get, "STOP"):
        #for method (link, b) in iter(self.q.get, "STOP"):
            # method is one of <imagehost>.<imagehost>_parse function
            # link is the matched url from finalset
            # b is always self.basedir
            try:
                method()
            except TypeError as e:
                # in case we have disabled the module (with not_supported
                # function) method will raise TypeError, which we can safely
                # ignore
                pass

    def chunks(self, l, n):
        """split an iterable in enough chunks of itself as the n given"""
        return (l[i:i+n] for i in range(0, len(l), n))

    def get_all_links(self, tag, attr):
        xpath_search = '//' + tag + '[@' + attr + ']'
        all_tags = self.page.xpath(xpath_search)
        return all_tags


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
    return options, args
#    return options.poster, options.embed, options.gui, options.savedirectory, options.filelist , args


def download_url(url, savedirectory, embed="", poster=""):
    """Main function to parse and download images"""
    
    connector = http_connector.Connector()
    r_page = connector.reqhandler(url, 1)
    if r_page == '':
        raise IOError("Url not valid or nonexistent")



    # Generate the directory for the source file and the images downloaded
    # Plus, return savedirectory as basedir + page title, so to save images
    # on a per-site basis
    source_saver = savesource.SaveSource(url, savedirectory, creditor=poster)
    savedirectory = source_saver.link_save()

#    savedirectory = savesource.save_source(url, savedirectory, creditor=poster)

    # Parse the page for images
    parser = ImageHostParser(r_page, 'a', 'href', savedirectory)
    if embed:
        # do we need to search for embedded images then?
        # Note: at the moment it downloads thumbnails too
        print("Searching for embedded images")
        print("")
        embed_links = parser.get_all_links('img', 'src')
        parser.which_host(embed_links, 'src')



def filelist_parse(parsefile):
    """parsing a file containing urls and giving back a list of them"""
    with open(abspath(parsefile), 'r') as f:
        return f.readlines()

def filelist_download(download_file):
    """download a serie of urls from a file and comment out them, in another
    file, as they are being downloaded."""
    bckp = dirname(abspath(download_file)) + '/' + 'list.bak'
    with open(abspath(download_file), 'rw') as f:
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
                        download_url(u.strip("\n"), basedir, options.embed, options.poster)
                        bckp_l.append(u)
                        url = '#' + u
                        o.write(url)
                    except:
                        # if anything goes wrong, append an error tag to the
                        # url and go on to the next one
                        bckp_l.append(u)
                        url = 'ERROR: ' + u
                        o.write(url)

    # at the end, move the backup file to the filelist's place
    rename(abspath(o.name), abspath(f.name))


def filelist_fileinput(download_file):
    """download a serie of urls from a file, commenting them as they are being
    downloaded (using fileinput)"""
    f = fileinput.input(abspath(download_file), inplace=1)
    for line in f:
        try:
            download_url(line, basedir, options.embed, options.poster)
        except:
            # print the line where it stopped
            print(line)
            # if anything goes wrong, exit without further touching the filelist
            sys.exit(0)
        l = '#' + line
        print(l.strip("\n"))

if __name__ == "__main__":
    options, url = argument_parser()

    if options.savedirectory:
        # directory given on the command line?
        basedir = abspath(options.savedirectory)

    if options.filelist:
        filelist_download(options.filelist)

        # exit now, we don't need to start the gui in this case
        sys.exit(0)

    # do we want a gui?
    if options.gui:
        pygui = pygui.Gui(basedir, options.embed, options.poster)
    else:
        # no gui then
        download_url(url, basedir, options.embed, options.poster)

    sys.exit(0)