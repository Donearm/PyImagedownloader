#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2012, Gianluca Fiore
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
__version__ = "1.6"
__date__ = "03082011"
__email__ = "forod.g@gmail.com"

import sys
import re
import fileinput
import urllib2
import logging
from multiprocessing import Process, Queue, log_to_stderr
from os.path import abspath, dirname
from os import rename
import lxml.html
# importing local modules
import savesource, imageshack, imagevenue, imagehaven, imagebam, \
        imagetitan, bellazon, skinsbe, shareapic, \
        sharenxs, blogspot, postimage, imageupper, photobucket, \
        imageban, imagehostorg, turboimagehost, usemycomputer, wordpress, \
        imageboss, servimg, pixroute, tumblr, imgur, radikal, typepad, imgbox
import http_connector
# importing config file variables
from pyimg import basedir, numprocs, debug



# print an advice for hosts not supported
def not_supported(host):
    msg = "Sorry but %s isn't supported or isn't working right now" % host
    print(msg)


# The regexp we'll need to find the link
rHttp = re.compile("http://", re.IGNORECASE)
rImagevenue = re.compile("http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rImagebam = re.compile("http://www\.imagebam\.com/image/", re.IGNORECASE)
rImagehaven = re.compile("http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
rImageshack = re.compile("http://(img[0-9]{,3}\.)?imageshack\.us", re.IGNORECASE)
rPostimage = re.compile("http://(www\.|[a-z0-9]+)?postimage\.org/(image|[a-z0-9]+)/", re.IGNORECASE)
rSharenxs = re.compile("http://(www\.)?sharenxs\.com/(thumbnails|view/\?)", re.IGNORECASE)
rBlogspot = re.compile("http://[0-9]\.bp\.blogspot\.com", re.IGNORECASE)
rBellazon = re.compile("http://www\.bellazon\.com/main/index\.php\?s=[a-z0-9]+&act=attach", re.IGNORECASE)
rSkinsBe = re.compile("http://image\.skins\.be", re.IGNORECASE)
rShareapic = re.compile("http://www\.shareapic\.net/(content\.php\?id|View-[0-9]+-\.html)", re.IGNORECASE)
rImagetitan = re.compile("http://img[0-9]{,2}\.imagetitan\.com", re.IGNORECASE)
rImageUpper = re.compile("http://imageupper\.com/g?i/", re.IGNORECASE)
rPhotobucket = re.compile("http://[a-z0-9]+\.photobucket\.com", re.IGNORECASE)
rImageban = re.compile("http://[a-z0-9]+\.imageban\.ru", re.IGNORECASE)
rImagehostorg = re.compile("http://[a-z0-9]+\.imagehost\.org", re.IGNORECASE)
rTurboimagehost = re.compile("http://www\.turboimagehost\.com/p/", re.IGNORECASE)
rUsemycomputer = re.compile("/show\.html\?([a-z0-9=\&\;]+)?i=\/indeximages", re.IGNORECASE)
rWordpress = re.compile("http://.*.wordpress\.com/[0-9]+/[0-9]+/.*\.[a-z]{,4}", re.IGNORECASE)
#rWordpress = re.compile("http://.*.wordpress\.com/[0-9]+/[0-9]+/.*\.[a-z]{,4}(\?w=[0-9]+\&amp\;h=[0-9]+)?", re.IGNORECASE)
rWordpressuploads = re.compile("http://.*/wp-content/uploads/.*\.[a-z]{,4}", re.IGNORECASE)
rImageboss = re.compile("http://www\.imageboss\.net", re.IGNORECASE)
rServimg = re.compile("http://www\.servimg\.com", re.IGNORECASE)
rPixroute = re.compile("http://www\.pixroute\.com", re.IGNORECASE)
rTumblr = re.compile("http://[0-9]+\.media\.tumblr\.com", re.IGNORECASE)
rImgur = re.compile("http://([a-z]+\.)?imgur\.com", re.IGNORECASE)
rRadikal = re.compile("http://([a-z0-9]+\.)?radikal\.ru", re.IGNORECASE)
rTypepad = re.compile("http://([a-z0-9]+\.)?typepad\.com/\.a/", re.IGNORECASE)
rImgbox = re.compile("http://imgbox\.com", re.IGNORECASE)
# putting them all in a dictionary
regexp_dict = {rImagevenue : imagevenue.ImagevenueParse,
        rImagebam : imagebam.ImagebamParse,
        rImagehaven : imagehaven.ImagehavenParse,
        rImageshack : imageshack.ImageshackParse,
        rPostimage : postimage.PostimageParse,
        rSharenxs : sharenxs.SharenxsParse,
        rBlogspot : blogspot.BlogspotParse,
        rBellazon : bellazon.BellazonParse,
        rSkinsBe : skinsbe.SkinsbeParse,
        rShareapic : shareapic.ShareapicParse,
        rImagetitan : imagetitan.ImagetitanParse,
        rImageUpper : imageupper.ImageupperParse,
        rPhotobucket : photobucket.PhotobucketParse,
        rImageban : imageban.ImagebanParse,
        rImagehostorg : imagehostorg.ImagehostorgParse,
        rTurboimagehost : turboimagehost.TurboimagehostParse,
        rUsemycomputer : usemycomputer.UsemycomputerParse,
        rWordpress : wordpress.WordpressParse,
        rWordpressuploads : wordpress.WordpressParse,
        rImageboss : imageboss.ImagebossParse,
        rServimg : servimg.ServimgParse,
        rPixroute : pixroute.PixrouteParse,
        rTumblr : tumblr.TumblrParse,
        rImgur : imgur.ImgurParse,
        rRadikal : radikal.RadikalParse,
        rTypepad : typepad.TypepadParse,
        rImgbox : imgbox.ImgboxParse
        }



# Main parser class
class ImageHostParser():
    """ The main parser class """

    def __init__(self, page, tag, attr, basedir):
        self.page = page
        self.lxmlpage = lxml.html.fromstring(page)
        self.tag = tag
        self.attr = attr
        self.basedir = basedir
        self.numprocs = numprocs
        self.img_counter = 0
# iterlinks() gets all links on the page but it's slower than using xpath
# (because it catches a whole lot more links)
#        self.linklist = []
#        for L in self.lxmlpage.iterlinks():
#            if rHttp.search(L[2]):
#                self.linklist.append(L[2])
#        print(self.linklist)
        self.urllist = self.get_all_links(self.tag, self.attr)
        self.which_host(self.urllist, self.attr)

    def which_host(self, urllist, attr):
        """check every url in the given list against all regular expressions
        and extract the value of the chosen html attribute.
        Then use a queue and enough processes to download all matched urls"""
        # make a queue and enough processes as numprocs
        self.q = Queue()
        self.ps = [ Process(target=self.use_queue, args=()) for i in range(self.numprocs) ]

        # enable multiprocessing logging feature
        if debug:
            log_to_stderr(logging.DEBUG)


        for p in self.ps:
            # start all processes
            p.start()
        
        # piping the urllist urls into a set to purge duplicates
        finalset = set()
        for L in urllist:
            self.stringl = str(L.get(attr, None))
            # remove the anonym.to string before urls
            if self.stringl.startswith("http://anonym.to/?"):
                self.stringl = re.sub('http://anonym.to/\?', '', self.stringl)
            finalset.add(self.stringl)


        for L in finalset:
            # iterate over the regexp dictionary items; when finding a url
            # matching, put the the class name, url and self.basedir in the queue
            for k, v in regexp_dict.items():
                if k.search(L):
                    # instantiate and then pass the parse method to the queue.
                    # it downloads but doesn't make the queue do its job
#                    parser = v(L, self.basedir)
#                    self.q.put((parser.parse()))

                    # add the class name and the parameters needed for its __init__
                    # into the queue
                    self.q.put((v, (L, self.basedir)))
                    self.img_counter = self.img_counter + 1
                else:
                    continue

        for i in range(self.numprocs):
            # put a STOP to end the iter builtin inside use_queue
            self.q.put("STOP")

        print("%d images were present" % self.img_counter)

    def use_queue(self):
        """use up the queue by running all its elements"""
        for instance, (link, b) in iter(self.q.get, "STOP"):
            # instance is simply the name of the class as in regexp_dict
            # link is the matched url from finalset
            # b is always self.basedir
            
            # instantiate the class
            i = instance(link, b)
            try:
                # run the parse method
                i.parse()
            except TypeError as e:
                # in case we have disabled the module (with not_supported
                # function) trying to run it will raise TypeError, which we can 
                # safely ignore
                pass

    def chunks(self, l, n):
        """split an iterable in enough chunks of itself as the n given"""
        return (l[i:i+n] for i in range(0, len(l), n))

    def get_all_links(self, tag, attr):
        xpath_search = '//' + tag + '[@' + attr + ']'
        all_tags = self.lxmlpage.xpath(xpath_search)
        return all_tags


# Generate the argument parser
def argument_parser():
    try:
        import argparse

        cli_parser = argparse.ArgumentParser()
        cli_parser.add_argument("-c", "--credit",
                action="store",
                help="optionally save the name of the poster of the images in a file",
                dest="poster")
        cli_parser.add_argument("-e", "--embed",
                action="store_true",
                help="enable search for embedded images too",
                dest="embed")
        cli_parser.add_argument("-d", "--directory",
                action="store",
                help="the directory where to save images (overrides config file)",
                dest="savedirectory")
        cli_parser.add_argument("-g", "--gtk",
                action="store_const",
                help="start in GUI mode (GTK)",
                const='gtk',
                dest="gui")
        cli_parser.add_argument("-q", "--qt",
                action="store_const",
                help="start in GUI mode (QT)",
                const='qt',
                dest="gui")
        cli_parser.add_argument("-f", "--filelist",
                action="store",
                help="download urls from file, one per row",
                dest="filelist")
        cli_parser.add_argument(action="store",
                help="URL",
                nargs="*",
                dest="url")
        options = cli_parser.parse_args()
        return options

    except ImportError:
        # Python < 2.7 = no argparse
        import optparse

        usage_message = "usage: %prog [options] url"
        cli_parser = optparse.OptionParser(usage=usage_message)
        cli_parser.add_option("-c", "--credit",
                help="optionally save the name of the poster of the images in a file",
                dest="poster")
        cli_parser.add_option("-e", "--embed",
                action="store_true",
                help="enable search for embedded images too",
                dest="embed")
        cli_parser.add_option("-d", "--directory",
                help="the directory where to save images (overrides config file)",
                dest="savedirectory")
        cli_parser.add_option("-g", "--gtk",
                action="store_const",
                help="start in GUI mode (GTK)",
                const='gtk',
                dest="gui")
        cli_parser.add_option("-q", "--qt",
                action="store_const",
                help="start in GUI mode (QT)",
                const='qt',
                dest="gui")
        cli_parser.add_option("-f", "--filelist",
                help="download urls from file, one per row",
                dest="filelist")
        (options, args) = cli_parser.parse_args()
        return options, args


def download_url(url, savedirectory, embed="", poster=""):
    """Main function to parse and download images"""
    
    connector = http_connector.Connector()
    r_page = connector.reqhandler(url, 1)
    if r_page == '':
        raise IOError("Url not valid or nonexistent")


    # be sure to have a url as a string and not as a list for savesource.py
    url_string = connector.check_string_or_list(url)
    # Generate the directory for the source file and the images downloaded
    # Plus, return savedirectory as basedir + page title, so to save images
    # on a per-site basis
    source_saver = savesource.SaveSource(r_page, savedirectory, url_string, creditor=poster)
    savedirectory = source_saver.link_save()

    # Parse the page for images
    parser = ImageHostParser(r_page, 'a', 'href', savedirectory)
    if embed:
        # do we need to search for embedded images then?
        # Note: at the moment it downloads thumbnails too
        embed_download(parser)

def embed_download(parser):
    """Search for embedded images in a page. Requires an instance of ImageHostParser to be passed"""
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
                    except urllib2.URLError as e:
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
    # try argparse first
    try:
        options = argument_parser()
        # rename options.url to retrocompatibility with optparse previous 
        # settings
        url = options.url
    except IndexError:
        options, url = argument_parser()


    if options.savedirectory:
        # directory given on the command line?
        basedir = abspath(options.savedirectory)

    if options.filelist is not None:
        filelist_download(options.filelist)

        # exit now, we don't need to start the gui in this case
        sys.exit(0)

    # do we want a gui?
    if options.gui:
        if options.gui == 'gtk':
            import pygui
            pygui = pygui.Gui(basedir, options.embed, options.poster)
        else:
            import pygui4
            pygui = pygui4.Gui(basedir, options.embed, options.poster)
    else:
        # no gui then
        try:
            download_url(url, basedir, options.embed, options.poster)
        except KeyboardInterrupt:
            sys.exit(1)



    sys.exit(0)
