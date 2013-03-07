#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imagetitan
import lxml.html
from os.path import join, getsize, isfile

class TestImagetitan(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://img2.imagetitan.com/img.php?image=38_1966.jpg'
        self.image_url = 'http://img2.imagetitan.com/img2/IVljS3wDcTG4k66/38/38_1966.jpg'
        self.example_ititan_page = """<html>
<head>
   <title>ImageTitan | 1966.jpg</title>
   <meta name="keywords" content="hosting, image hosting, picture hosting, photo hosting, image webhosting, photo webhosting, picture webhosting">
   <meta name="description" content="Totally free image hosting service for forums, websites, auctions, and more">
</head>
<script language="javascript">
var saveWidth = 0;

function scaleImg(what)
{
   what = document.getElementById(what);
   if( navigator.appName=="Netscape" )
   {
      winW = window.innerWidth;
   }
   if( navigator.appName.indexOf("Microsoft") != -1 )
   {
      winW = document.body.offsetWidth;
   }
   if( what.width > (720) || saveWidth > (720) )
   {
      if( what.width == (720) )
      {
         what.width=saveWidth;
      }
      else
      {
         saveWidth = what.width;
         what.style.cursor = "pointer";
         what.width=(720);
         note.style.display="";
      }
   }
}
</script>
<body text=#000000 link=#3333FF vlink=3333FF alink=#FF0000 bgcolor=#DDDDDD topmargin=5>

<center>
<div id="note" style="display:none;"><font size=1 face="verdana">This image has been scaled down to fit your screen. Click image for original size</font><p></div>

<img id="image" onLoad="scaleImg('image')" onClick="scaleImg('image')" src="img2/IVljS3wDcTG4k66/38/38_1966.jpg"></center>

<p>

<center>
<br><font size=2 face="verdana, arial">
<a href="http://www.imagetitan.com/linkcode.php?host=img2&t=1&image=38_1966.jpg">Get Linking Code</a> | <a href="http://www.imagetitan.com/">Upload Images</a> | <a href="http://www.imagetitan.com/report.php?host=img2&image=38_1966.jpg">Report Problem</a>
<br><font size=1>Free image hosting by <a href="http://www.imagetitan.com/">ImageTitan</a></font>

</font>
</center>

</body>
</html>"""
        self.ititan = imagetitan.ImagetitanParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.ititan.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imagetitan_get_image_match_group(self):
        self.imggrp, self.imgmiddle, self.imgname = self.ititan.imagetitan_get_image_match_group(lxml.html.fromstring(self.example_ititan_page))
        # re.MatchObject simply return True if they matched
        self.assertTrue(self.imggrp)
        self.assertTrue(self.imgmiddle)
        self.assertTrue(self.imgname)

    def test_imagetitan_save_image(self):
        imggrp = 'img2'
        imgmiddle = '/IVljS3wDcTG4k66/38/'
        imgname = '38_1966.jpg'
        savefile = join(self.basedir, imgname)
        self.ititan.imagetitan_save_image(imggrp, imgmiddle, imgname)
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImagetitan)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
