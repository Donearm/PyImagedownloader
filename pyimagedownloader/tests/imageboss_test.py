#!/usr/bin/env python2

import unittest
import imageboss
import lxml.html
from os.path import join, getsize, isfile

class TestImageboss(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://www.imageboss.net/view/4yui83wma8beyq2ja174ne7x6k79mg-83663.JPG'
        self.image_url = 'http://www.imageboss.net/img/4yui83wma8beyq2ja174ne7x6k79mg/83663.JPG'
        self.example_iboss_page = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<HTML>
   <HEAD>
    <TITLE>Image Boss | Free Image Gallery Hosting</TITLE>
    <meta http-equiv="content-type" content="html; charset=UTF-8">
    <META name="author" content="Imageboss.net">
    <META name ="description" content="Fast, easy and free photo upload and hosting">
    <META name="keywords" content="free, image, photo, upload, image hosting, sharing, gallery, hosting, pictures">
    <meta name="robots" content="follow">

    <meta name="revisit-after" content="1 days">
    <link rel="stylesheet" href="http://www.imageboss.net/templates/stylesheet.css" type="text/css">



    <script type="text/javascript" src="http://www.imageboss.net/js/scripts.js"></script>


   </HEAD>
   <BODY>

<script type="text/javascript" src="http://syndication.exoclick.com/splash.php?cat=97&idsite=80194&idzone=137587&login=2damnhot&type=1"></script>


<p align="center">Image hosted by <a href='http://www.imageboss.net'>ImageBoss.net - Free Image Hosting</a></p>


<div id="containerImgs">


<!--JuicyAds v2.0-->
<iframe hspace=0 vspace=0 border=0 frameborder=0 marginheight=0 marginwidth=0 width=900 height=18 scrolling=no allowtransparency=true src=http://adserver.juicyads.com/adshow.php?adzone=8497></iframe>
<!--JuicyAds END-->

<div id="nextprev">





Image 3 of 10 <a href="http://www.imageboss.net/img/4yui83wma8beyq2ja174ne7x6k79mg/">Visit gallery</a>



<div id="next">
<a href="http://www.imageboss.net/view/img/4yui83wma8beyq2ja174ne7x6k79mg-39285.JPG">Next <img src="http://www.imageboss.net/images/next.png"></a>
</div>

<div id="prev">
<a href="http://www.imageboss.net/view/img/4yui83wma8beyq2ja174ne7x6k79mg-78281.JPG"><img src="http://www.imageboss.net/images/prev.png"> Previous</a>
</div>


<div id="stream">

<!--JuicyAds v2.0-->
<iframe border=0 frameborder=0 marginheight=0 marginwidth=0 width=100 height=18 scrolling=no allowtransparency=true src=http://adserver.juicyads.com/adshow.php?adzone=63669></iframe>
<!--JuicyAds END--></div>

<div style="clear:both"></div>
</div>

<!-- THE IMAGE -->
<p align="center">
<a href="#" onclick="showOnclick()">
<img id="thepic" onLoad="scaleImg();"  src="http://www.imageboss.net/img/4yui83wma8beyq2ja174ne7x6k79mg/83663.JPG" border="0">
</a>
</p>


<div id="nextprev">

<!-- Toolbox -->
<div class="addthis_toolbox addthis_default_style">
<a href="http://www.addthis.com/bookmark.php?v=250&amp;username=imageboss" class="addthis_button_compact">Share</a>
<span class="addthis_separator">|</span>

<a class="addthis_button_facebook"></a>
<a class="addthis_button_twitter"></a>
<a class="addthis_button_stumbleupon"></a>
<a class="addthis_button_myspace"></a>
<a class="addthis_button_favorites"></a>
</div>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js?pub=imageboss"></script>
<script type="text/javascript">
var addthis_config = {
  data_use_flash: false
}
</script>
<!-- Toolbox END -->





<span style="float:right;">

<a href="http://www.imageboss.net/download/img/4yui83wma8beyq2ja174ne7x6k79mg" title="Download Gallery as a Zip">Download gallery</a><a href="http://www.imageboss.net/download/img/4yui83wma8beyq2ja174ne7x6k79mg"><img class="downloadzip" src="http://www.imageboss.net/images/download.png" title="Download Gallery as a Zip" alt="Download Gallery as a Zip"></a>
</span>


<div style="clear:both"></div>
</div>

<!--JuicyAds v2.0-->
<iframe hspace=0 vspace=0 border=0 frameborder=0 marginheight=0 marginwidth=0 width=900 height=18 scrolling=no allowtransparency=true src=http://adserver.juicyads.com/adshow.php?adzone=8497></iframe>
<!--JuicyAds END-->


<div id="codesgallery">


<form name="codesgallery">
<h4>Direct Link</h4>
<input class="sharebox2" type="text" onClick="highlight(this);"
value='http://www.imageboss.net/view/img/4yui83wma8beyq2ja174ne7x6k79mg-83663.JPG'>

<h4>HTML Code</h4>
<textarea class="sharebox" name="sharehtml" rows="2"
onClick='highlight(this);'>
<a href="http://www.imageboss.net/view/img/4yui83wma8beyq2ja174ne7x6k79mg-83663.JPG" target="_blank"><img src="http://www.imageboss.net/img/4yui83wma8beyq2ja174ne7x6k79mg/thumbs/83663.JPG"></a></textarea>

<h4>BBCode</h4>
<textarea class="sharebox" name="sharebbcode" rows="2"
onClick='highlight(this);'>
[URL=http://www.imageboss.net/view/img/4yui83wma8beyq2ja174ne7x6k79mg-83663.JPG][IMG]http://www.imageboss.net/img/4yui83wma8beyq2ja174ne7x6k79mg/thumbs/83663.JPG[/IMG][/URL]</textarea>
</form>

<b><a href="http://www.imageboss.net/share/img/4yui83wma8beyq2ja174ne7x6k79mg">More sharing options</a></b>

</div>


</div>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-1230184-2");
pageTracker._trackPageview();
} catch(err) {}</script>

<div style="display: none;">
<a href="http://whos.amung.us/stats/8itd0b82nmkd/"><img src="http://whos.amung.us/widget/8itd0b82nmkd.png" width="81" height="29" alt="online"></a>
</div>
</BODY>
</HTML>"""
        self.iboss = imageboss.ImagebossParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.iboss.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imageboss_get_image_src_and_name(self):
        self.imageboss_src, self.imagename = self.iboss.imageboss_get_image_src_and_name(lxml.html.fromstring(self.example_iboss_page))
        self.assertIsInstance(self.imageboss_src, list)
        self.assertTrue(self.imageboss_src[0])
        self.assertIsInstance(self.imagename[-1], str)
        self.assertTrue(self.imagename[-1])

    def test_imageboss_save_image(self):
        urllist = [self.image_url]
        imagename = [1, 2, 'jump.jpg']
        self.iboss.imageboss_save_image(urllist, imagename)
        savefile = join(self.basedir, str(imagename[-1]))
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImageboss)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
