#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import sys
import pyimagedownloader

class TestPyImagedownloader(unittest.TestCase):
    """Unit test for pyimagedownloader (main module)"""

    def setUp(self):
        self.bellazon = 'http://www.bellazon.com/http://www.bellazon.com/main/index.php?act=attach&type=post&id=1382086'
        self.blogspot = 'http://mode.newslicious.net/2011/07/lara-stone-by-inez-vinoodh-for-vogue.html'
        self.imagebam = 'http://forum.phun.org/showthread.php?t=741256'
        self.imagebam_glry = 'http://www.imagebam.com/gallery/7jauxf1kj8s0amhtjg8gpgo55cuse0wu/'
        self.imageban = 'http://www.basketforum.it/index.php?showtopic=352&st=8800'
        self.imageboss = 'http://www.bellazon.com/main/index.php?showtopic=16155'
        self.imagehaven = 'http://forum.phun.org/showthread.php?t=632438'
        self.imagehostorg = 'http://forum.phun.org/showthread.php?t=491782'
        self.imageshack = 'http://www.bellazon.com/main/index.php?showtopic=5128'
        self.imagesocket = 'http://forum.phun.org/showthread.php?t=509325'
        self.imagetitan = 'http://forum.phun.org/showthread.php?t=66721'
        self.imageupper = 'http://forum.phun.org/showthread.php?t=494331'
        self.imagevenue = 'http://forum.phun.org/showthread.php?t=632446'
        self.imgur = 'http://www.bellazon.com/main/index.php?showtopic=53&st=2699'
        self.photobucket = 'http://www.bellazon.com/main/index.php?showtopic=16563'
        self.pixroute = 'http://forum.phun.org/showthread.php?t=614083'
        self.postimage = 'http://forums.thefashionspot.com/showpost.php?p=8759371&postcount=62'
        self.radikal = 'http://www.bellazon.com/main/index.php?showtopic=33394'
        self.servimg = 'http://www.bellazon.com/main/index.php?showtopic=37664'
        self.shareapic = 'http://www.shareapic.net/898538-Satomi-Shigemori---Sexy-Asian-Bikini-Model.html'
        self.sharenxs = 'http://forum.phun.org/showthread.php?t=741299'
        self.skinsbe = 'http://forum.skins.be/50-hq-unknown-pictures/20239-danica-thrall/'
        self.tumblr = 'http://fuckyeahsimodels.tumblr.com/post/6544001799'
        self.turboimagehost = 'http://picturecentral.wordpress.com/2011/02/08/lauren-budd-la-senza-photoshoot/'
        self.typepad = 'http://fashioncopious.typepad.com/fashioncopious/2011/05/giedre-dukauskaite-for-lexpress-styles-may-2011-by-alexandre-weinberger-editorial.html'
        self.usemycomputer = 'http://usemycomputer.com/indeximages/women/Emma.Watson/'
        self.wordpress_uploads = 'http://www.bemagazine.tv/2011/07/12/beautiful-fashion-night-foto-video/'
        self.parser = pyimagedownloader.ImageHostParser()


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPyImagedownloader)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
