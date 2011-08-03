#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import typepad
import lxml.html
from os.path import join, getsize, isfile

class TestTypepad(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://fashioncopious.typepad.com/.a/6a00e54ef964538834015432347a94970c-popup'
        self.example_tpad_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <title>L'Express Styles May 2011 Giedre Dukauskaite by Alexandre Weinberger 1</title>
        <style type="text/css">
            html, body, p
            {
                margin: 0;
                border: 0;
                padding: 0;
                background: #000;
            }
        </style>
        <script type="text/javascript" src="/.shared/js/yui/yahoo-dom-event.js"></script>
        <script type="text/javascript">
            YAHOO.util.Event.onDOMReady( function() {
                var vw = YAHOO.util.Dom.getViewportWidth(),
                    vh = YAHOO.util.Dom.getViewportHeight();
                window.resizeBy( '800' - vw, '518' - vh );
            } );
        </script>
    </head>

    <body>
        <p><img src="http://fashioncopious.typepad.com/.a/6a00e54ef964538834015432347a94970c-800wi" alt="L'Express Styles May 2011 Giedre Dukauskaite by Alexandre Weinberger 1" /></p>
    <!-- Start Quantcast tag -->
<script type="text/javascript" src="http://edge.quantserve.com/quant.js"></script>
<script type="text/javascript">_qoptions = { tags:"typepad.core" }; _qacct="p-fcYWUmj5YbYKM"; quantserve();</script>
<noscript>
<a href="http://www.quantcast.com/p-fcYWUmj5YbYKM" target="_blank"><img src="http://pixel.quantserve.com/pixel/p-fcYWUmj5YbYKM.gif?tags=typepad.core" style="display: none" border="0" height="1" width="1" alt="Quantcast"/></a>
</noscript>
<!-- End Quantcast tag -->
<!-- Begin comScore Tag -->
<script>
document.write(unescape("%3Cscript src='" + (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js'%3E%3C/script%3E"));
</script>
<script>
COMSCORE.beacon({
  c1: 2,
  c2: "6035669",
  c3: "",
  c4: "http://fashioncopious.typepad.com/.a/6a00e54ef964538834015432347a94970c-popup",
  c5: "",
  c6: "",
  c15: ""
});

</script>
<noscript>
  <img src="http://b.scorecardresearch.com/b?c1=2&c2=6035669&c3=&c4=http%3A%2F%2Ffashioncopious.typepad.com%2F.a%2F6a00e54ef964538834015432347a94970c-popup&c5=&c6=&c15=&cv=1.3&cj=1" style="display:none" width="0" height="0" alt="" />
</noscript>
<!-- End comScore Tag -->
</body>
</html>
<!-- ph=1 -->"""
        self.tpad = typepad.TypepadParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.tpad.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_typepad_get_image_src(self):
        self.typepad_src = self.tpad.typepad_get_image_src(lxml.html.fromstring(self.example_tpad_page))
        self.assertIsInstance(self.typepad_src, list)
        self.assertTrue(self.typepad_src[0])

    def test_typepad_get_image_name(self):
        self.imagename = self.tpad.typepad_get_image_name(self.url)
        self.assertIsInstance(self.imagename, list)
        self.assertTrue(self.imagename[0])

    def test_typepad_save_image(self):
        urllist = [ self.url ]
        imagename = ['http://fashioncopious.typepad.com/', '6a00e54ef964538834015432347a94970c-popup']
        savefile = join(self.basedir, str(imagename[1]) + '.jpg')
        self.tpad.typepad_save_image(urllist, imagename)
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTypepad)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
