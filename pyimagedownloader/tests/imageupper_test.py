#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imageupper
import lxml.html

class TestImageupper(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://imageupper.com/i/?S0700010020221Z2735188161074'
        self.example_iupper_page = """<HTML><HEAD><TITLE>Image Upper.com - Free Image Hosting - View Image</TITLE>
<script type="text/javascript">
var resized=0;
var origW=0;
var ImgW=500;
var winW=800;
function scaleImg(what){
    what=document.getElementById(what);
    if(navigator.appName=="Netscape")
        winW=window.innerWidth;
    else if(navigator.appName.indexOf("Microsoft")!=-1 || navigator.appName.indexOf("Opera")!= -1)
        winW=document.body.offsetWidth;
    ImgW=what.width;
    if (resized==0 && ImgW>winW) {
        origW=ImgW;
        ImgW=winW-75;
        what.width=ImgW;
        resized=1;
    } else if(resized==1) {
        what.width=origW;
        resized=0;
    }
}
</script>
<style type="text/css">BODY { font-family: arial, helvetica, verdana; }.nav{font-size:12px}.desc{font-size:14px}.footer{font-size:10px}.status{font-size:14px}.base { font-size: 10pt; }.sm { font-size: 8pt; }.headline { font-size: 12pt; }.adHeadline { font: bold 14px Verdana; text-decoration: none; color: #002548; }.adText { font: normal 10px Verdana; text-decoration: none; color: #000000; }
 input.submitbtn {background-color: #FFFFF1; font-weight: bold; font-size: 9pt; color: black;}
 TABLE.tableBorderGray {BORDER-RIGHT: #CCCCCC 1px solid; BORDER-TOP: #CCCCCC 1px solid; BORDER-LEFT: #CCCCCC 1px solid; BORDER-BOTTOM: #CCCCCC 1px solid; BACKGROUND-COLOR: #fff}
 TABLE.tableBorder {BORDER-RIGHT: #B4B600 1px solid; BORDER-TOP: #B4B600 1px solid; BORDER-LEFT: #B4B600 1px solid; BORDER-BOTTOM: #B4B600 1px solid; BACKGROUND-COLOR: #fff}</style>
 
 </HEAD><BODY bgColor="#FFFFE7" leftMargin="0" text="#000000" topMargin="0" marginheight="0" marginwidth="0" LINK="#000000" ALINK="#000000" VLINK="#000000">
 <CENTER><TABLE WIDTH="750" HEIGHT="100%" class="tableBorderGray"><TR><TD WIDTH="100%" ALIGN="CENTER" BGCOLOR="#FFFFFF" VALIGN="TOP"><!-- main table-->
 
 <TABLE WIDTH="100%"><TR><TD ALIGN="CENTER" VALIGN="middle" class="nav"><A href="/"><IMG SRC="/smtext.gif" ALT="Image Upper - Free Image Hosting" ALIGN="middle" border=0></A> &nbsp;- &nbsp;<A HREF="/">Home</A> - &nbsp;<A HREF="/user/?do=myFiles">My Files</A> - &nbsp;<A HREF="/">Upload Images</A> - &nbsp;<A HREF="/tos.shtml">Terms Of Service</A></TD></TR><TR><TD class="nav" ALIGN="CENTER" VALIGN="TOP"><br><script type="text/javascript"><!--
 google_ad_client = "pub-0957851610151603";
 google_ad_slot = "7080521766";
 google_ad_width = 728;
 google_ad_height = 90;
 //-->
 </script>

 <script type="text/javascript"
 src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
 </script></TD></TR><TR><TD CLASS="base"><CENTER><P><TABLE WIDTH="95%" BORDER="0"><TR><TD ALIGN="CENTER" VALIGN="TOP" CLASS="sm"><IMG id="img" onClick="scaleImg('img');" onLoad="scaleImg('img');" SRC="http://s07.imageupper.com/1/2/Z2735188161074_22.jpg" ALT="Free celebrity, entertainment and fashion photos!"></TD></TR></TABLE><p><CENTER><TABLE WIDTH="95%" BORDER="0"><TR><TD ALIGN="RIGHT" VALIGN="TOP" BGCOLOR="#FFFFF1" class="desc"><CENTER><script type="text/javascript"><!--
 google_ad_client = "pub-0957851610151603";
 google_ad_slot = "3557370446";
 google_ad_width = 728;
 google_ad_height = 15;
 //--></script>
 <script type="text/javascript"
 src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
 </script></CENTER> <A HREF="/g/?S070001002Z2735188161074">See all Images in this Gallery >></A></TD></TR></TABLE></CENTER><P><script type="text/javascript"><!--
 google_ad_client = "pub-0957851610151603";
 google_ad_slot = "7080521766";
 google_ad_width = 728;
 google_ad_height = 90;
 //-->
 </script>
 <script type="text/javascript"
 src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
 </script><P><CENTER><TABLE WIDTH="500" CELLSPACING="0" CELLPADDING="3" BORDER="0" CLASS="tableBorder"><TR><TD>&nbsp;</TD><TD class="nav" ALIGN="CENTER"><A HREF="/code/?S070001002Z2735188161074">Get Linking Code</A> &nbsp;|&nbsp; <A HREF="/cgi/report.pl?f=S070001002Z2735188161074">Report This Image</A></TD><TD>&nbsp;</TD></TR><TR><TD ALIGN="CENTER" COLSPAN="3" CLASS="sm"><P><BR><A HREF="/" style="text-decoration:none"><b>Host your images FREE and FAST @</A> </b><A HREF="/"><IMG SRC="/smtext.gif" ALT="Image Upper - Free Image Hosting" BORDER="0" ALIGN="MIDDLE"></A><p>100% Pop-up Free Image Hosting >> <A HREF="/">Upload Now</A>!</font><p></TD></TR></TABLE></CENTER><P><p></CENTER></TD></TR></TABLE><P><BR><script type="text/javascript" language="JavaScript">var site="s31imgupper"</script><script type="text/javascript" src="http://s31.sitemeter.com/js/counter.js?site=s31imgupper"></script><noscript><a href="http://s31.sitemeter.com/stats.asp?site=s31imgupper" target="_top"><img src="http://s31.sitemeter.com/meter.asp?site=s31imgupper" alt="Site Meter" border="0"></a></noscript><script type="text/javascript" language="JavaScript1.2" src="/stats.js"></script><noscript><IMG SRC="http://paidstats.com/cgi/stats.pl?i=0&site=s31imgupper&pg=&r=nojs"></noscript>&nbsp;<FONT CLASS="footer">© 2006-2010 <A HREF="/copyright.shtml">Copyright</A> Image Upper.com. All rights reserved. &nbsp;|&nbsp; <A HREF="/tos.shtml">Terms Of Service</A><P></CENTER></TD></TR></TABLE></CENTER><!-- main table--></BODY></HTML>"""
        self.iupper = imageupper.ImageupperParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.iupper.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imageupper_get_image_src(self):
        self.imageupper_src = self.iupper.imageupper_get_image_src(lxml.html.fromstring(self.example_iupper_page))
        self.assertIsInstance(self.imageupper_src, list)
        self.assertTrue(self.imageupper_src[0])

    def test_imageupper_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImageupper)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
