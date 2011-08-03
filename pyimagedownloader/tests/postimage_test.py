#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import postimage
import lxml.html
from os.path import join, getsize, isfile

class TestPostimage(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://postimage.org/image/2a2npxl6s/'
        self.image_url = 'http://s3.postimage.org/5tolfqo49/Clip_20io.jpg'
        self.example_pimage_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>View image: Clip 20io</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<link rel="stylesheet" type="text/css" href="/style.min.css" />
</head>
<body>
<center>
<br /><br />
<img src='http://s3.postimage.org/njqa0s1o8/Clip_20io.jpg' alt='Clip 20io' width='661px' height='894px' /><br /><br /><br />
<div id="footer">
<ul>
<li><a href="http://www.postimage.org/">free image hosting</a> | </li>

<li><a href="http://www.postimage.org/search.php">image search</a> | </li>
<li><a href="#codes" onclick="toggle('codes');">show codes</a> | </li>
<li><a href="http://www.postimage.org/contact.php?url=aHR0cDovL3Bvc3RpbWFnZS5vcmcvaW1hZ2UvMmEybnB4bDZzLw==">report abuse or request deletion</a></li></ul>
<br />
<div id="codes">
<a name="codes"></a>

<table border="0" cellpadding="0" cellspacing="4" class="bbcode">
<tr>
    <td><textarea onmouseover='this.focus()' onfocus='this.select()' id="code_1" wrap="off" scrolling="no">http://postimage.org/image/2a2npxl6s/</textarea></td>

    <td style="width:170px;"><span id="result_1">Direct Link</span></td>
    <td><div id="clip_container_1" style="position:relative" onmousedown="clip_i=1"><div id="clip_button_1" class="my_clip_button">copy to clipboard</div></div></td>
</tr>
<tr>
    <td colspan="3" style="padding-top:15px">&nbsp;</td>
</tr>
<tr>
    <td><textarea onmouseover='this.focus()' onfocus='this.select()' id="code_2" wrap="off" scrolling="no">[url=http://postimage.org/image/2a2npxl6s/][img]http://s3.postimage.org/2a2npxl6s/Clip_20io.jpg[/img][/url]</textarea></td>
    <td><span id="result_2">Thumbnail for Forums (1)</span></td>

    <td><div id="clip_container_2" style="position:relative" onmousedown="clip_i=2"><div id="clip_button_2" class="my_clip_button">copy to clipboard</div></div></td>
</tr>
<tr>
    <td><textarea onmouseover='this.focus()' onfocus='this.select()' id="code_3" wrap="off" scrolling="no">[url=http://postimage.org/image/2a2npxl6s/][img=http://s3.postimage.org/2a2npxl6s/Clip_20io.jpg][/url]</textarea></td>
    <td><span id="result_3">Thumbnail for Forums (2)</span></td>
    <td><div id="clip_container_3" style="position:relative" onmousedown="clip_i=3"><div id="clip_button_3" class="my_clip_button">copy to clipboard</div></div></td>
</tr>
<tr>
    <td><textarea onmouseover='this.focus()' onfocus='this.select()' id="code_4" wrap="off" scrolling="no">&lt;a href='http://postimage.org/image/2a2npxl6s/' target='_blank'&gt;&lt;img src='http://s3.postimage.org/2a2npxl6s/Clip_20io.jpg' border='0' alt=&quot;Clip 20io&quot; /&gt;&lt;/a&gt;</textarea></td>

    <td><span id="result_4">Thumbnail for Website</span></td>
    <td><div id="clip_container_4" style="position:relative" onmousedown="clip_i=4"><div id="clip_button_4" class="my_clip_button">copy to clipboard</div></div></td>
</tr>
<tr>
    <td colspan="3" style="padding-top:15px">&nbsp;</td>
</tr>
<tr>
    <td><textarea onmouseover='this.focus()' onfocus='this.select()' id="code_5" wrap="off" scrolling="no">[url=http://www.postimage.org/][img]http://s3.postimage.org/r3c7ql4id/Clip_20io.jpg[/img][/url]
[url=http://www.postimage.org/]image hosting[/url]</textarea></td>
    <td><span id="result_5">Hotlink for Forums (1)</span></td>

    <td><div id="clip_container_5" style="position:relative" onmousedown="clip_i=5"><div id="clip_button_5" class="my_clip_button">copy to clipboard</div></div></td>
</tr>
<tr>
    <td><textarea onmouseover='this.focus()' onfocus='this.select()' id="code_6" wrap="off" scrolling="no">[url=http://www.postimage.org/][img=http://s3.postimage.org/r3c7ql4id/Clip_20io.jpg][/url]
[url=http://www.postimage.org/]image hosting[/url]</textarea></td>
    <td><span id="result_6">Hotlink for Forums (2)</span></td>
    <td><div id="clip_container_6" style="position:relative" onmousedown="clip_i=6"><div id="clip_button_6" class="my_clip_button">copy to clipboard</div></div></td>
</tr>
<tr>
    <td><textarea onmouseover='this.focus()' onfocus='this.select()' id="code_7" wrap="off" scrolling="no">&lt;a href='http://www.postimage.org/' target='_blank'&gt;&lt;img src='http://s3.postimage.org/r3c7ql4id/Clip_20io.jpg' border='0' alt=&quot;Clip 20io&quot; /&gt;&lt;/a&gt;&lt;br /&gt;&lt;a target='_blank' href='http://www.postimage.org/'&gt;image hosting&lt;/a&gt;&lt;br /&gt;&lt;br /&gt;

</textarea></td>
    <td><span id="result_7">Hotlink for Website</span></td>
    <td><div id="clip_container_7" style="position:relative" onmousedown="clip_i=7"><div id="clip_button_7" class="my_clip_button">copy to clipboard</div></div></td>
</tr>
<tr>
    <td colspan="3" style="padding-top:10px">&nbsp;</td>
</tr>
<tr>
    <td>&nbsp;</td>
    <td style="width:170px;">Social Networks</td>

    <td>
        <a rel="nofollow" target="_blank" href='http://del.icio.us/post?url=http://postimage.org/image/2a2npxl6s/' title="Submit to Delicious"><span class="smallsocial smalldelicious"></span></a>
        <a rel="nofollow" target="_blank" href='https://www.google.com/bookmarks/mark?op=edit&bkmk=http://postimage.org/image/2a2npxl6s/&annotation=' title="Submit to Google Bookmark"><span class="smallsocial smallgooglebook"></span></a>
        <a rel="nofollow" target="_blank" href='http://digg.com/submit?phase=2&url=http://postimage.org/image/2a2npxl6s/' title="Submit to Digg"><span class="smallsocial smalldigg"></span></a>
        <a rel="nofollow" target="_blank" href='http://www.google.com/buzz/post?url=http://postimage.org/image/2a2npxl6s/' title="Submit to Google Buzz"><span class="smallsocial smallbuzz"></span></a>
        <a rel="nofollow" target="_blank" href='http://www.stumbleupon.com/submit?url=http://postimage.org/image/2a2npxl6s/' title="Submit to StumbleUpon"><span class="smallsocial smallstumbleupon"></span></a>
        <a rel="nofollow" target="_blank" href='http://www.reddit.com/submit?url=http://postimage.org/image/2a2npxl6s/' title="Submit to Reddit"><span class="smallsocial smallreddit"></span></a>
        <a rel="nofollow" target="_blank" href='http://twitter.com/home/?status=http://postimage.org/image/2a2npxl6s/' title="Submit to Twitter"><span class="smallsocial smalltwitter"></span></a>
        <a rel="nofollow" target="_blank" href='http://www.facebook.com/sharer.php?u=http://postimage.org/image/2a2npxl6s/' title="Submit to Facebook"><span class="smallsocial smallfacebook"></span></a>

    </td>
</tr>
</table>
</div>
<p>Powered by PostImage.org</p>
</div>
</center>
<script type="text/javascript" src="/view.group.js"></script>
<script type="text/javascript">new Image().src = "//counter.yadro.ru/hit?r" + escape(document.referrer) + ((typeof(screen)=="undefined")?"" : ";s"+screen.width+"*"+screen.height+"*" + (screen.colorDepth?screen.colorDepth:screen.pixelDepth)) + ";u"+escape(document.URL) + ";h"+escape(document.title.substring(0,80)) + ";" +Math.random();</script>
</body>
</html>"""
        self.pimage = postimage.PostimageParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.pimage.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_postimage_get_image_src(self):
        self.postimage_src = self.pimage.postimage_get_image_src(lxml.html.fromstring(self.example_pimage_page))
        self.assertIsInstance(self.postimage_src, list)
        self.assertTrue(self.postimage_src[0])

    def test_postimage_save_image(self):
        # TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPostimage)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
