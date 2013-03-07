#!/usr/bin/env python2

import unittest
import imagehostorg
import lxml.html
from os.path import join, getsize, isfile

class TestImagehostorg(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://h.imagehost.org/view/0790/cover'
        self.url2 = 'http://h.imagehost.org/view/0198/z_cover.jpg'
        self.image_url = 'http://h.imagehost.org/0790/cover.jpg'
        self.image_url2 = 'http://h.imagehost.org/0198/z_cover.jpg'
        self.example_ihostorg_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>cover.jpg - ImageHost.org</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="http://static.imagehost.org/imagehost.css" />
<link rel="shortcut icon" href="/favicon.ico" type="image/vnd.microsoft.icon" />
<script type="text/javascript">
/* <![CDATA[ */
var imageWidth = 525;
var imageHeight = 790;

if (typeof(window.innerWidth) == "number")
    browserWidth = window.innerWidth;
else if (document.documentElement && document.documentElement.clientWidth)
    browserWidth = document.documentElement.clientWidth;
else if (document.body && document.body.clientWidth)
    browserWidth = document.body.clientWidth;

var scaled = false;

function Scale(image)
{
    if (scaled)
    {
        image.width = imageWidth;
        image.height = imageHeight;
        image.style.cursor = "default";
        image.title = "Click to view image scaled to your browser window";
        document.getElementById("warning").style.display = "none";
        scaled = false;
    }
    else
    {
        if (imageWidth>browserWidth)
        {
            image.width = browserWidth-50;
            image.height = (browserWidth-50) * (imageHeight/imageWidth);
            image.style.cursor = "pointer";
            image.title = "Click to view image in its original size";
            document.getElementById("warning").style.display = "";
            scaled = true;
        }
    }
}
/* ]]> */
</script>

</head>
<body>

<div class="box"><!-- --></div>

<div id="warning" style="display:none">This image has been scaled to your browser window. Click on the image to view it in its original size.</div><div id="content">

<img src="http://h.imagehost.org/0790/cover.jpg" border="0" width="525" height="790" id="image" onclick="javascript:Scale(this);" alt="Hosted by ImageHost.org" />
<script type="text/javascript">
/* <![CDATA[ */
Scale(document.getElementById("image"));
/* ]]> */
</script>
</div>


<div class="box"><!-- BEGIN STANDARD TAG - 728 x 90/468 x 60 - ImageHost: Run-of-site - DO NOT MODIFY -->
<IFRAME FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=728 HEIGHT=90 SRC="http://ad.reduxmedia.com/st?ad_type=iframe&ad_size=728x90,468x60&section=692800"></IFRAME>
<!-- END TAG -->

<!-- BEGIN STANDARD TAG - popup or popunder - ImageHost - PopUnder: Run-of-site - DO NOT MODIFY -->
<SCRIPT TYPE="text/javascript" SRC="http://ad.reduxmedia.com/st?ad_type=pop&ad_size=0x0&section=699247&banned_pop_types=28&pop_times=1&pop_frequency=86400"></SCRIPT>
<!-- END TAG --></div>

<div class="box"><table class="links" cellspacing="3">

<tr><th colspan="2">cover.jpg</th></tr>
<tr><td nowrap="nowrap">Forum Thumbnail Link</td>
<td class="linkwide"><input type="text" class="wide" readonly="readonly" onclick="javascript:this.focus(); this.select();" size="50" value="[url=http://h.imagehost.org/view/0790/cover][img]http://h.imagehost.org/t/0790/cover.jpg[/img][/url]" /></td>
</tr>
<tr><td nowrap="nowrap">HTML Thumbnail Link</td>
<td class="linkwide"><input type="text" class="wide" readonly="readonly" onclick="javascript:this.focus(); this.select();" size="50" value="&lt;a target=&quot;_blank&quot; href=&quot;http://h.imagehost.org/view/0790/cover&quot;&gt;&lt;img src=&quot;http://h.imagehost.org/t/0790/cover.jpg&quot; border=&quot;0&quot; width=&quot;100&quot; height=&quot;150&quot; alt=&quot;cover.jpg (382 KB)&quot; /&gt;&lt;/a&gt;" /></td>
</tr>
<tr><td nowrap="nowrap">Forum Hotlink</td>
<td class="linkwide"><input type="text" class="wide" readonly="readonly" onclick="javascript:this.focus(); this.select();" size="50" value="[url=http://h.imagehost.org/view/0790/cover][img]http://h.imagehost.org/0790/cover.jpg[/img][/url]" /></td>
</tr>
<tr><td nowrap="nowrap">HTML Hotlink</td>
<td class="linkwide"><input type="text" class="wide" readonly="readonly" onclick="javascript:this.focus(); this.select();" size="50" value="&lt;a target=&quot;_blank&quot; href=&quot;http://h.imagehost.org/view/0790/cover&quot;&gt;&lt;img src=&quot;http://h.imagehost.org/0790/cover.jpg&quot; border=&quot;0&quot; width=&quot;525&quot; height=&quot;790&quot; alt=&quot;ImageHost.org&quot; /&gt;&lt;/a&gt;" /></td>

</tr>
<tr><td nowrap="nowrap">Text Link</td>
<td class="linkwide"><input type="text" class="wide" readonly="readonly" onclick="javascript:this.focus(); this.select();" size="50" value="http://h.imagehost.org/view/0790/cover" /></td>
</tr>
<tr><td nowrap="nowrap">Hotlink</td>
<td class="linkwide"><input type="text" class="wide" readonly="readonly" onclick="javascript:this.focus(); this.select();" size="50" value="http://h.imagehost.org/0790/cover.jpg" /></td>
</tr>
</table>
</div>

<div class="box">
<a href="http://www.imagehost.org/"><img src="http://static.imagehost.org/logosmall.gif" border="0" width="263" height="38" alt="ImageHost.org - Free Image &amp; File Hosting" /></a>

</div>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-136268-3");
pageTracker._setDomainName(".imagehost.org");
pageTracker._trackPageview();
} catch(err) {}</script>

<!-- Start Quantcast tag -->
<script type="text/javascript" src="http://edge.quantserve.com/quant.js"></script>
<script type="text/javascript">_qacct="p-65fDiBy2lVMDM";quantserve();</script>
<noscript>
<a href="http://www.quantcast.com/p-65fDiBy2lVMDM" target="_blank"><img src="http://pixel.quantserve.com/pixel/p-65fDiBy2lVMDM.gif" style="display: none" border="0" height="1" width="1" alt="Quantcast"/></a>
</noscript>
<!-- End Quantcast tag -->
</body>
</html>"""
        self.ihost = imagehostorg.ImagehostorgParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.ihost.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imagehostorg_get_image_split_and_src(self):
        self.imagehostorg_split, self.imagehostorg_src = self.ihost.imagehostorg_get_image_split_and_src(lxml.html.fromstring(self.example_ihostorg_page))
        self.assertIsInstance(self.imagehostorg_split, list)
        self.assertTrue(self.imagehostorg_split[0])
        if self.imagehostorg_src:
            self.assertIsInstance(self.imagehostorg_src, list)
            self.assertTrue(self.imagehostorg_src[0])

    def test_imagehostorg_save_image(self):
        urllist = [self.image_url]
        split = ['http://', 'h.imagehost.org', '/view/', '/0790/', 'cover.jpg']
        savefile = join(self.basedir, str(split[-1]))
        self.ihost.imagehostorg_save_image(split, src_list=urllist)
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)

    def test_imagehostorg_save_image_without_src_list(self):
        urllist = [self.image_url2]
        split2 = ['http://', 'h.imagehost.org', '/view/', '/0198/', 'z_cover.jpg']
        savefile2 = join(self.basedir, str(split2[-1]))
        self.ihost.imagehostorg_save_image(split2)
        self.assertTrue(isfile(savefile2))
        self.assertTrue(getsize(savefile2) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImagehostorg)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
