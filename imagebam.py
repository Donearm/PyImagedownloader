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

import random
import string
from urllib import urlretrieve
from os.path import join, exists
import lxml.html
import http_connector


def imagebam_parse(link, basedir):
    # get every page linked from the imagebam links
    connector = http_connector.Connector()
    response = connector.reqhandler(link)

    try:
        page = lxml.html.fromstring(response)
    except lxml.etree.XMLSyntaxError as e:
        # most of the time we can simply ignore parsing errors
        return

    # find the src attribute which contains the real link of imagebam's images
    src_links = page.xpath("//img[@onclick='scale(this);']")

    imagebam_src = [li.get('src', None) for li in src_links]

    # get the image name from the id tag
#    imagename = [li.get('id', None) for i in src_links]
    # or, better, from the Content-Disposition header
    imagename = connector.get_filename(imagebam_src[0], 'filename=')

    download_url = imagebam_src[0]

    try: 
        savefile = join(basedir, imagename)
    except UnicodeEncodeError:
        # encode with utf8 files with non-ascii characters in their name
        savefile = join(basedir, imagename.encode("utf-8"))
    except UnicodeDecodeError:
        # catch bad characters and try to replace them with correct utf8 chars
        savefile = join(basedir, imagename.decode('utf8', 'replace'))
    except AttributeError:
        # perhaps we have used the split in getting an imagename and thus
        # we now have a list and not a string
        savefile = join(basedir, imagename[-1])

    # finally save the image in the desidered directory
    if not exists(savefile):
        try:
            urlretrieve(download_url, savefile) 
        except IOError as e:
            # image not loading, skipping it
            return
    else:
        randstring = ''.join(random.choice(string.lowercase) for i in range(5))
        try:
            savefile = join(basedir, randstring + imagename)
        except UnicodeEncodeError:
            savefile = join(basedir, randstring + imagename.encode("uft-8"))
        except AttributeError:
            savefile = join(basedir, randstring + imagename[-1])
        except TypeError:
            savefile = join(basedir, randstring + imagename[-1])
        try:
            urlretrieve(download_url, savefile)
        except IOError as e:
            return


