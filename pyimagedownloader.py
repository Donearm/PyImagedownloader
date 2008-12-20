#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
"""
"""
###############################################################################



__author__ = "Gianluca Fiore"
__license__ = "GPL"
__version__ = "1.0"
__date__ = "10102008"
__email__ = "forod.g@gmail.com"

import sys
import re
import urllib2
import shutil
import os
from urllib import FancyURLopener, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer

# +---------------------------------------------------------------------------+
# | GPL license block                                                         |
# |                                                                           |
# | This program is free software; you can redistribute it and/or modify      |
# | it under the terms of the GNU General Public License as published by      |
# | the Free Software Foundation; either version 2 of the License, or         |
# | (at your option) any later version.                                       |
# |                                                                           |
# | This program is distributed in the hope that it will be useful,           |
# | but WITHOUT ANY WARRANTY; without even the implied warranty of            |
# | MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             |
# | GNU General Public License for more details.                              |
# |                                                                           |
# | You should have received a copy of the GNU General Public License         |
# | along with this program; if not, write to the Free Software               |
# | Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA |
# +---------------------------------------------------------------------------+
# +---------------------------------------------------------------------------+
# | Release Log                                                               |
# |                                                                           |
# | 1.0 : first release. Support for imagevenue, imagebam, imageshack,        |
# |       upmyphoto, uppix and imgshed                                        |
# +---------------------------------------------------------------------------+


# If no arguments were given, print a helpful message
if len(sys.argv)!=2:
    print 'Usage: pyimagedownloader url'
    sys.exit(0)

# The regexp we'll need to find the link
rJpgSrc = re.compile('.(jpg|png|gif|jpeg)', re.IGNORECASE) # generic src attributes regexp
rUsercash = re.compile("href=\"?http://[0-9]+\.usercash\.com", re.IGNORECASE)
rImagevenue = re.compile("href=\"?http://img[0-9]{,3}\.imagevenue\.com", re.IGNORECASE)
rImagebam = re.compile("href=\"?http://www\.imagebam\.com/image", re.IGNORECASE)
rImagehaven = re.compile("href=\"?http://(img|adult|[a-z])[0-9]{,3}\.imagehaven\.net", re.IGNORECASE)
rImageshack = re.compile("href=\"?http://img[0-9]{,3}\.imageshack\.us", re.IGNORECASE)
rUpmyphoto = re.compile("href=\"?http://www\.upmyphoto\.com", re.IGNORECASE)
rImgshed = re.compile("href=\"?http://imgshed\.com", re.IGNORECASE)
rUppix = re.compile("href=\"?http://www\.uppix\.info", re.IGNORECASE)
#rBellazon = re.compile('href=\"?http://www\.bellazon\.com/http://www\.bellazon\.com/main/index\.php\?act=', re.IGNORECASE)
rBellazon = re.compile("http://www\.bellazon\.com/", re.IGNORECASE)
rSkinsBe = re.compile("href=\"?http://image\.skins\.be", re.IGNORECASE)

# Our base directory
basedir = '/mnt/documents/Maidens/Uploads/'

# Create a class from urllib because it's better to substitute the default 
# User-Agent with something more common (google won't get angry and so on)
class MyUrlOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610 GranParadiso/3.0.1'


class ImageHostParser():
    """ The main parser class """

    def __init__(self, page, tag):
        self.page = BeautifulSoup(page)
        self.tag = tag
        self.which_host(tag)

    def which_host(self, tag):
        all_tags = self.page.findAll(tag)
        for L in all_tags:
            stringl = str(L)
            if rUsercash.search(stringl):
                self.usercash_parse(L)
            elif rImagevenue.search(stringl):
                self.imagevenue_parse(L)
            elif rImagebam.search(stringl):
                self.imagebam_parse(L)
            elif rImagehaven.search(stringl):
                self.imagehaven_parse(L)
            elif rImageshack.search(stringl):
                self.imageshack_parse(L)
            elif rUpmyphoto.search(stringl):
                self.upmyphoto_parse(L)
            elif rImgshed.search(stringl):
                self.imgshed_parse(L)
            elif rUppix.search(stringl):
                self.uppix_parse(L)
            #elif rBellazon.search(stringl):
            #    self.bellazon_parse(L, page)
            elif rSkinsBe.search(stringl):
                print "We found a link!"
                self.skinsbe_parse(L)
            else:
                continue

    def usercash_parse(self, link):    
        usercash_list = []
        usercash_list.append(link['href'])
        for images in usercash_list:
            # get every page linked from the usercash links
            image_page = myopener.open(images)
            rimage_page = image_page.read()
            page_soup = BeautifulSoup(rimage_page)
            # find the src attribute which contains the real link of imagevenue's images
            src_links = page_soup.findAll('frame', src=rJpgSrc)
            usercashSrc = []
            for li in src_links:
                li_without_loc = re.sub('&.*', '', li['src'])
                usercashSrc.append(li_without_loc) # add all the src part to a list
                # open the imagevenue's page
                linked_image_page = myopener.open(li_without_loc)
                Rlinked_image_page = linked_image_page.read()
                linked_page_soup = BeautifulSoup(Rlinked_image_page)
                src_links2 = linked_page_soup.findAll('img', src=rJpgSrc)
                imagevenue_src = []
                for src in src_links2:
                    print src
                    imagevenue_src.append(src)
                print li_without_loc
                print imagevenue_src[0]
                # TODO:
                # usercash doesn't works


                savefile = basedir + str(saveExtension[1])
                # finally save the image on the desidered directory
                urlretrieve(downloadUrl, savefile) 


            # Close the first page
            image_page.close()


    def imagevenue_parse(self, link):
        imagevenue_list = [] # the list that will contain the href tags
        imagevenue_list.append(link['href'])
        for i in imagevenue_list:
            # get every page linked from the imagevenue links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of imagevenue's images
            src_links = page_soup.findAll('img', id='thepic')
            imagevenue_src = []
            for li in src_links:
                imagevenue_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            imagevenue_split = re.split('img.php\?image=', i) # remove the unneeded parts
            try:
                # make up the real image url
                download_url = str(imagevenue_split[0]) + str(imagevenue_src[0])
            except IndexError:
                # if we get an IndexError just continue (it may means that the image
                # can't be downloaded from the server or there is a host's glitch
                continue
            # generate just the filename of the image to be locally saved
            save_extension = re.split('[0-9a-zA-Z]+-[0-9]+/loc[0-9]{,4}/', imagevenue_src[0]) 
            savefile = basedir + str(save_extension[1])
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 


    def imagebam_parse(self, link):
        rSrcImagebam = re.compile("http://[0-9]+\.imagebam\.com/dl\.php") # regexp for the src link
        imagebam_list = [] # the list that will contain the href tags
        imagebam_list.append(link['href'])
        for i in imagebam_list:
            # get every page linked from the imagebam links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of imagebam's images
            src_links = page_soup.findAll('img', src=rSrcImagebam)
            imagebam_src = []
            for li in src_links:
                imagebam_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            imagebam_split = re.split('dl\.php\?ID=', imagebam_src[0]) # remove the unneeded parts
            download_url = imagebam_src[0]
            # generate just the filename of the image to be locally saved
            # TODO: іf the image is not a jpeg how to get the correct extension?
            savefile = basedir + str(imagebam_split[1]) + ".jpg"
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 

    def imagehaven_parse(self, link):
        rSrcImagehaven = re.compile("\./images") # regexp for the src link
        imagehaven_list = [] # the list that will contain the href tags
        imagehaven_list.append(link['href'])
        for i in imagehaven_list:
            # get every page linked from the imagehaven links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of imagehaven's images
            src_links = page_soup.findAll('img', src=rSrcImagehaven)
            imagehaven_src = []
            for li in src_links:
                imagehaven_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            imagehaven_split = re.split('img\.php\?id=', i) # remove the unneeded parts
            imagehaven_split2 = re.split('\.\/', imagehaven_src[0]) 
            try:
                # make up the real image url
                download_url = str(imagehaven_split[0]) + str(imagehaven_split2[1])
            except IndexError:
                # if we get an IndexError just continue (it may means that the image
                # can't be downloaded from the server or there is a host's glitch
                continue
            # generate just the filename of the image to be locally saved
            save_extension = re.split('\./images/[0-9A-Za-z]+/[0-9A-Za-z]+/', imagehaven_src[0]) 
            savefile = basedir + str(save_extension[1])
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 


    def imageshack_parse(self, link):
        rSrcImageshack = re.compile('http://img([0-9]{,3})\.imageshack\.us/img[0-9]+/[0-9]+/[0-9a-z]+\.jpg')
        imageshack_list = [] # the list that will contain the href tags
        imageshack_list.append(link['href'])
        for i in imageshack_list:
            # get every page linked from the imageshack links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of imageshack's images
            src_links = page_soup.findAll('img', src=rSrcImageshack)
            imageshack_src = []
            for li in src_links:
                imageshack_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            # generate just the filename of the image to be locally saved
            save_extension = re.split('img[0-9]{,3}/[0-9]+/', imageshack_src[0]) 
            savefile = basedir + str(save_extension[1])
            download_url = imageshack_src[0]
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 

    def uppix_parse(self, link):
        uppix_list = [] # the list that will contain the href tags
        uppix_list.append(link['href'])
        for i in uppix_list:
            # get every page linked from the uppix links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of uppix's images
            src_links = page_soup.findAll('img', id='dpic')
            uppix_src = []
            for li in src_links:
                uppix_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            # generate just the filename of the image to be locally saved
            save_extension = re.sub('S[0-9]+/', '',  uppix_src[0]) 
            uppix_sub = re.sub('Viewer[a-zA-Z]\.php\?file=', '', i)
            savefile = basedir + save_extension
            # finally save the image on the desidered directory
            urlretrieve(uppix_sub, savefile) 

    def upmyphoto_parse(self, link):
        upmyphoto_list = [] # the list that will contain the href tags
        upmyphoto_list.append(link['href'])
        for i in upmyphoto_list:
            # get every page linked from the upmyphoto links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of upmyphoto's images
            src_links = page_soup.findAll('img', src=rUpmyphoto)
            upmyphoto_src = []
            for li in src_links:
                upmyphoto_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            # generate just the filename of the image to be locally saved
            save_extension = re.split('img/dir[0-9]+/loc[0-9]+/',  upmyphoto_src[0]) 
            savefile = basedir + str(save_extension[1])
            download_url = upmyphoto_src[0]
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 

    def imgshed_parse(self, link):
        imgshed_list = [] # the list that will contain the href tags
        imgshed_list.append(link['href'])
        for i in imgshed_list:
            # get every page linked from the imgshed links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of imgshed's images
            src_links = page_soup.findAll('img', id='theimage')
            imgshed_src = []
            for li in src_links:
                imgshed_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            # generate just the filename of the image to be locally saved
            save_extension = re.sub('^\./files/', '', imgshed_src[0]) 
            download_url = 'http://imgshed.com/files/' + save_extension

            savefile = basedir + save_extension
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 

    def bellazon_parse(self, link, page):
        bellazon_list = []
        bellazon_list.append(self.page.findAll('a', title=rJpgSrc))
        #href_links = self.page.findAll('a', href=rBellazon)
        #bellazon_href = []
        #for li in bellazon_href:
        #    bellazon_href.append(li['href'])
        #    print li
        for li in bellazon_list:
            print li

    def skinsbe_parse(self, link):
        skinsbe_list = [] # the list that will contain the href tags
        skinsbe_list.append(link['href'])
        for i in skinsbe_list:
            print i
            # get every page linked from the skinsbe links
            image_page = myopener.open(i)
            Rimage_page = image_page.read()
            page_soup = BeautifulSoup(Rimage_page)
            # find the src attribute which contains the real link of skinsbe's images
            src_links = page_soup.findAll('img', id='theimage')
            skinsbe_src = []
            for li in src_links:
                print li
                skinsbe_src.append(li['src']) # add all the src part to a list

            # Close the page
            image_page.close()

            # generate just the filename of the image to be locally saved
            save_extension = re.sub('^\./files/', '', skinsbe_src[0]) 
            download_url = 'http://skinsbe.com/files/' + save_extension

            savefile = basedir + save_extension
            # finally save the image on the desidered directory
            urlretrieve(download_url, savefile) 

    def save_source(self, page):
        """ the method to save the original page link to a file """

        # get the page's title
        page_title = myopener.open(page)
        Rpage_title = page_title.read()
        page_title_soup = BeautifulSoup(Rpage_title)
        # purge the title of troublesome characters
        #neatTitle = re.sub('[\s\|\.\;\,\&\?\!\'\/\\]', '', page_title_soup.title.string)
        #neat_title = re.sub('\W', '', page_title_soup.title.string)
        neat_title = re.sub('[\s\|\.\&\,\'\:\!\@]', '', page_title_soup.title.string)
        print neat_title
        output_dir = basedir + neat_title
        os.mkdir(output_dir, 0740)
        os.chdir(output_dir)
        # save the source url in a file
        source_file = open('source.txt', "w")
        source_file.write('fonte:' + page + "\n\n\n")
        source_file.close()
        # move all the images in basedir in the output_dir
        files_in_basedir = os.listdir(basedir)
        for f in files_in_basedir:
            if rJpgSrc.search(f):
                src_name = os.path.join(basedir, f)
                dst_name = os.path.join(output_dir, f)
                shutil.move(src_name, dst_name)




# Instanciate the UrlOpener
myopener = MyUrlOpener()

# Open and read the page contents
page = myopener.open(sys.argv[1])
Rpage = page.read()
page.close()

# Parse the page for images
parser = ImageHostParser(Rpage, 'a', )
# Generate the directory for the source file and the images downloaded
parser.save_source(sys.argv[1])
sys.exit(0)
