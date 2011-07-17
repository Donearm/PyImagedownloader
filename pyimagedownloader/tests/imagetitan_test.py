#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imagetitan
import lxml.html

class TestImagetitan(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://img1.imagetitan.com/img.php?d=1/10&n=anna10.jpg'
        self.example_ititan_page = """<html>
<head>
   <title>ImageTitan | anna10.jpg</title>
   <meta name="keywords" content="hosting, image hosting, picture hosting, photo hosting, image webhosting, photo webhosting, picture webhosting">
   <meta name="description" content="Totally free image hosting service for forums, websites, auctions, and more">
</head>
<body text=#000000 link=#3333FF vlink=3333FF alink=#FF0000 bgcolor=#DDDDDD topmargin=5>

<center><img src="http://www.imagetitan.com/images/bodytop.gif"></center>
<table align=center border=0 cellpadding=0 cellspacing=0 width=750 bgcolor=#FFFFFF>
<tr>
<td background="http://www.imagetitan.com/images/bodybg.gif"><font face="verdana, arial" size=2>

<table align=center border=0 cellpadding=0 cellspacing=0 width=730>
<tr>
<td>
<font face="verdana, arial" size=2>
<center><a href="http://www.imagetitan.com/"><img src="http://www.imagetitan.com/images/title.gif" border=0></a><br>
<a href="http://www.imagetitan.com/">Home</a> | <a href="http://www.imagetitan.com/faq.htm">FAQ</a> | <a href="http://www.imagetitan.com/terms.htm">Terms of Use</a> | <a href="http://www.imagetitan.com/contact.htm">Contact Us</a></center>
</td>

</tr>
</table>
</td>
</tr>
</table>
<center><img src="http://www.imagetitan.com/images/bodybot.gif"></center>

<p>

<table align=center border=0 cellpadding=5 cellspacing=0 width=750>
<tr>
<td align=center>
<img src="img1/1/10/anna10.jpg"></td>
</tr>
</table>

<p>

<center><img src="http://www.imagetitan.com/images/bodytop.gif"></center>
<table align=center border=0 cellpadding=0 cellspacing=0 width=750 bgcolor=#FFFFFF>
<tr>
<td align=center background="http://www.imagetitan.com/images/bodybg.gif">
<iframe src="http://www.mentalfunk.com/ads/720x90.htm" width="720" height="90" frameborder="no" scrolling="no"></iframe></center>
</td>
</tr>
</table>
<center><img src="http://www.imagetitan.com/images/bodybot.gif"></center>

<center><font size=2>Copyright &copy; 2006 ImageTitan. All Rights Reserved</center>

</body>
</html>"""
        self.ititan = imagetitan.ImagetitanParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.ititan.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imagetitan_get_image_match_group(self):
        self.imggrp, self.imgmiddle, self.imgname = self.ititan.imagetitan_get_image_match_group(lxml.html.fromstring(self.example_ititan_page))
        self.assertIsInstance(self.imggrp, re.MatchObject)
        self.assertIsInstance(self.imgmiddle, re.MatchObject)
        self.assertIsInstance(self.imgname, re.MatchObject)

    def test_imagetitan_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImagetitan)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
