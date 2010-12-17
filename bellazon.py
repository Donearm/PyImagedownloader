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
import lxml.html
import http_connector



# The regexp we'll need to find the link
rBellazon = re.compile("href.*attach\&amp", re.IGNORECASE)


def bellazon_parse(link, basedir):
    if rBellazon.search(str(link)):
        connector = http_connector.Connector()
        response = connector.reqhandler(link)
