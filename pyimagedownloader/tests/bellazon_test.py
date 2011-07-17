#!/usr/bin/env python2

import unittest
import bellazon
import lxml.html

class TestBellazon(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://www.bellazon.com/http://www.bellazon.com/main/index.php?act=attach&type=post&id=1382086'
        self.example_bz_src = ['http://www.bellazon.com/main/index.php?act=attach&type=post&id=1382086&']
        self.example_bz_page = """<html>
        <head>
        <script language="javascript">
        var actualWidth = 0;

        function scaleImg(what){
              what = document.getElementById(what);
                if(actualWidth == 0) actualWidth = what.width;
                  if(actualWidth < pageWidth()){
                          what.width = actualWidth;
                              return ;
                                }
                                  if(what.width != actualWidth){
                                          what.width = actualWidth;
                                              return;
                                                }else{
                                                        what.width = pageWidth();
                                                            return;
                                                              }
        }

        function pageWidth(){
              var pageWidth = 0;
                if (navigator.appName=="Netscape") pageWidth = window.innerWidth - 50;
                  if (navigator.appName.indexOf("Microsoft")!=-1) pageWidth =  document.body.offsetWidth - 50;
                    if(pageWidth < 768) pageWidth = 768;
                      return pageWidth;
        }
        </script>
        </head>
        <body><center>
        <div align="center">
        <table border=0 cellpadding=0 cellspacing=0>
        <tr><td>
        <!-- YB: top_left (300x250) -->
        <script type="text/javascript"><!--
        yieldbuild_client = 1094;
        yieldbuild_layout = "photo_page";
        yieldbuild_loc = "top_left";
        yieldbuild_options = {};
        //--></script>
        <script type="text/javascript" src="http://hook.yieldbuild.com/s_ad.js"></script>
        </td><td>
        <!-- YB: top_right (300x250) -->
        <script type="text/javascript"><!--
        yieldbuild_client = 1094;
        yieldbuild_layout = "photo_page";
        yieldbuild_loc = "top_right";
        yieldbuild_options = {};
        //--></script>

        <script type="text/javascript" src="http://hook.yieldbuild.com/s_ad.js"></script>
        </td></tr>
        </table>
        </div>
        <img src="http://www.bellazon.com/main/index.php?act=attach&type=post&id=1382086&" id="thepic" onClick="scaleImg('thepic')" onLoad="scaleImg('thepic')">
        <div align="center">

        <!-- YB: footer_zone (728x90) -->
        <script type="text/javascript"><!--
        yieldbuild_client = 1094;
        yieldbuild_layout = "photo_page";
        yieldbuild_loc = "footer_zone";
        yieldbuild_options = {};
        //--></script>
        <script type="text/javascript" src="http://hook.yieldbuild.com/s_ad.js"></script>

        </div></center>

        <script type="text/javascript">
        var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
        document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));

        </script>
        <script type="text/javascript">
        try {
            var pageTracker = _gat._getTracker("UA-9396829-1");
            pageTracker._trackPageview();
        } catch(err) {}</script>

        </body>
        </html>"""
        self.bz = bellazon.BellazonParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.bz.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_bellazon_get_image_src(self):
        self.bellazon_src = self.bz.bellazon_get_image_src(lxml.html.fromstring(self.example_bz_page))
        self.assertIsInstance(self.bellazon_src, list)
        self.assertTrue(self.bellazon_src[0])

    def test_bellazon_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBellazon)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
