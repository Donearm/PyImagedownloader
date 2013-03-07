#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import servimg
import lxml.html
from os.path import join, getsize, isfile

class TestServimg(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://www.servimg.com/image_preview.php?i=496&u=10000834'
        self.image_url = 'http://i20.servimg.com/u/f20/09/00/08/34/h10.jpg'
        self.example_serv_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><title>h10 - Servimg.com - Free image hosting service</title><link rel="stylesheet" type="text/css" href="style4.css" /><link rel="stylesheet" type="text/css" href="preview.css" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><script type="text/javascript" src="js/script.js"></script><!--
<script type="text/javascript" src="http://content.rmxads.com/rmtag3.js"></script><script language="JavaScript">var rm_host = "http://optimizedby.rmxads.com";var rm_section_id = 349372;var rm_banned_pop_types = 29;var rm_pop_times = 1;var rm_pop_frequency = 300;rmShowPop();</script>--><script type="text/javascript" src="http://ad.z5x.net/st?ad_type=pop&ad_size=0x0&section=1649951&banned_pop_types=29&pop_times=2&pop_frequency=86400"></script></head><body><table style="margin:auto;"><tr><td id="preview_conteneur"><div id="title"><a href="index.php?lang=en"><img id="left" src="images/picture_mini.jpg" alt="Servimg.com - Free image hosting service" /></a><a href="index.php?lang=en"><img id="right" src="images/title.png" alt="Servimg.com - Free image hosting service" /></a><div id="title_ads"><script type='text/javascript'>//<![CDATA[
var m3_u = (location.protocol=='https:'?'https://cas.criteo.com/delivery/ajs.php':'http://cas.criteo.com/delivery/ajs.php');var m3_r = Math.floor(Math.random()*99999999999);if (!document.MAX_used) document.MAX_used = ',';document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);document.write ("?nodis=1&amp;zoneid=3451");document.write ('&amp;cb=' + m3_r);if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));document.write ("&amp;loc=" + escape(window.location));if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));if (document.context) document.write ("&context=" + escape(document.context));if (document.mmm_fo) document.write ("&amp;mmm_fo=1");document.write ("'><\/scr"+"ipt>");//]]></script></div></div><ul id="menu_preview"><li class="link_close"><a href="javascript:window.close();">Close window</a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=fr"><img src="/images/france.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=en"><img src="/images/english.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=zh"><img src="/images/china.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=ar"><img src="/images/arabic.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=de"><img src="/images/germany.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=it"><img src="/images/italy.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=pt"><img src="/images/portugal.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=ru"><img src="/images/russia.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=es"><img src="/images/spain.gif" alt="" title="" /></a></li><li><a href="image_preview.php?i=496&u=10000834&amp;lang=ro"><img src="/images/romania.gif" alt="" title="" /></a></li></ul><p id="picture" style="clear:both;"><img src="http://i20.servimg.com/u/f20/09/00/08/34/h10.jpg" alt="" /></p><form action="image_preview.php?lang=en" method="post" ><input type="hidden" name="i" value="496" /><input type="hidden" name="u" value="10000834" /><br /><p class="center" ><input type="submit" name="report" value="Report this as offensive/adult content" /></p></form><div id="profile_register_advertising"><center><script type='text/javascript'>//<![CDATA[
var m3_u = (location.protocol=='https:'?'https://cas.criteo.com/delivery/ajs.php':'http://cas.criteo.com/delivery/ajs.php');var m3_r = Math.floor(Math.random()*99999999999);if (!document.MAX_used) document.MAX_used = ',';document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);document.write ("?nodis=1&amp;zoneid=3447");document.write ('&amp;cb=' + m3_r);if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));document.write ("&amp;loc=" + escape(window.location));if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));if (document.context) document.write ("&context=" + escape(document.context));if (document.mmm_fo) document.write ("&amp;mmm_fo=1");document.write ("'><\/scr"+"ipt>");//]]></script></center></div><div style="height:1px;width: 750px;"></div></td></tr></table><div style="width: 750px;"></div><div id="footer"><p class="center"><a href="index.php?lang=en">Home page</a>&nbsp;|&nbsp;<a href="terms_service.php?lang=en">Terms of Service</a>&nbsp;|&nbsp;<a href="report.php?lang=en">Report this as offensive/adult content</a>&nbsp;|&nbsp;<a href="http://www.forumotion.com/make-forum" target="_blank" class="copyright">Make a forum</a></p><p class="center"><a href="image_preview.php?i=496&u=10000834&amp;lang=fr"><img src="/images/france.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=en"><img src="/images/english.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=zh"><img src="/images/china.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=ar"><img src="/images/arabic.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=de"><img src="/images/germany.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=it"><img src="/images/italy.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=pt"><img src="/images/portugal.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=ru"><img src="/images/russia.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=es"><img src="/images/spain.gif" alt="" title="" /></a><a href="image_preview.php?i=496&u=10000834&amp;lang=ro"><img src="/images/romania.gif" alt="" title="" /></a></p></div></div><script type="text/javascript">//<![CDATA[
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));//]]></script><script type="text/javascript">//<![CDATA[
try {var pageTracker = _gat._getTracker("UA-15108601-1");pageTracker._trackPageview();}catch(err) {}//]]></script></body></html>"""
        self.serv = servimg.ServimgParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.serv.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_servimg_get_image_src_and_name(self):
        self.servimg_src, self.imagename = self.serv.servimg_get_image_src_and_name(lxml.html.fromstring(self.example_serv_page))
        self.assertIsInstance(self.servimg_src, list)
        self.assertTrue(self.servimg_src[0])
        self.assertIsInstance(self.imagename, list)
        self.assertTrue(self.imagename[0])

    def test_servimg_save_image(self):
        urllist = [ self.image_url ]
        imagename = [ 'h10.jpg' ]
        savefile = join(self.basedir, imagename[0])
        self.serv.servimg_save_image(urllist, imagename)
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestServimg)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
