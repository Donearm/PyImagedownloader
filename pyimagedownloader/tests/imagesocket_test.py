#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imagesocket
import lxml.html

class TestImagesocket(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://www.imagesocket.com/view/Cover_1_back_med_Bdc1.jpg'
        self.example_isocket_page = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>
        <title>(iS) Image Socket &raquo; View image</title>
        <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
        <meta name="description" content="We offer friendly image hosting with a simple interface, did we mention its completely free?">
        <meta name="keywords" content="image, hosting, free, photo, easy, simple, fast, quality, friendly">
        <meta name="robots" content="all">
        <meta name="revisit-after" content="10 days">

        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
        <link rel="alternate" title="(iS) Image Socket" href="/rss" type="application/rss+xml">
        <link rel="stylesheet" href="http://c57189.r89.cf2.rackcdn.com/packed.css" type="text/css" media="all">
        <!--[if lte IE 6]>
        <link rel="stylesheet" href="http://c57189.r89.cf2.rackcdn.com/ie.css type="text/css" media="screen">
        <![endif]-->
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
        <script type="text/javascript" src="http://c57196.r96.cf2.rackcdn.com/packed.js"></script>
        <script>var RecaptchaOptions = {theme : 'white'};</script>

    </head>
    <body>
        <div id="logo">
           <a href="/"><img src="/img/logo.png" alt="(iS) Image Socket: Your Free Image Host"></a>
        </div>
        <div id="navigation">
           <ul>
                <li><a href="/news/" title="Site news">News</a></li>

                                <li><a href="/random/" title="Random image">Random</a></li>
                <li><a href="/top/" title="Top 10's">Top 10</a></li>
                <li><a href="/search/" title="Search images">Search</a></li>
                <li><a href="/status/" title="Site status">Status</a></li>
                <li><a href="/feedback/" title="Site feedback">Feedback</a></li>
                                <li><a href="/login/" title="Login form">Login</a></li>

                            </ul>
        </div>
                <div id="note">
            <img onClick="Dismiss('note', 'note', '19')" src='http://www.imagesocket.com/img/close.gif' alt='Close this note'><a href="http://www.filesocket.com">Looking for file hosting? Look no further!</a>        </div>
        <script type="text/javascript">
var AdBrite_Title_Color = 'CC0000';
var AdBrite_Text_Color = '7F7F7F';
var AdBrite_Background_Color = 'FFFFFF';
var AdBrite_Border_Color = 'FFFFFF';
var AdBrite_URL_Color = '000000';
try{var AdBrite_Iframe=window.top!=window.self?2:1;var AdBrite_Referrer=document.referrer==''?document.location:document.referrer;AdBrite_Referrer=encodeURIComponent(AdBrite_Referrer);}catch(e){var AdBrite_Iframe='';var AdBrite_Referrer='';}
</script>
<span style="white-space:nowrap;"><script type="text/javascript">document.write(String.fromCharCode(60,83,67,82,73,80,84));document.write(' src="http://ads.adbrite.com/mb/text_group.php?sid=1099718&zs=3436385f3630&ifr='+AdBrite_Iframe+'&ref='+AdBrite_Referrer+'" type="text/javascript">');document.write(String.fromCharCode(60,47,83,67,82,73,80,84,62));</script>
<a target="_top" href="http://www.adbrite.com/mb/commerce/purchase_form.php?opid=1099718&afsid=55544"><img src="http://files.adbrite.com/mb/images/adbrite-your-ad-here-banner.gif" style="background-color:#FFFFFF;border:none;padding:0;margin:0;" alt="Your Ad Here" width="11" height="60" border="0" /></a></span>
<div class="frame">

    <img src="/img/working.gif" alt="Image hosted by ImageSocket">
</div>
<script type="text/javascript">
$('.frame img').attr('src', 'http://content.imagesocket.com/images/Cover_1_back_med_Bdc1.jpg').load(function() {
    // Make sure image fit and you give users option to enlarge it via color box
    if($(this).width() > 600) {
        $(this).width(600);
        $(this).height(($(this).naturalHeight/$(this).naturalWidth) * 600);
        $(this).colorbox({href:"http://content.imagesocket.com/images/Cover_1_back_med_Bdc1.jpg"});
    }
});
</script>
<div class="actions">
    <div id="favorite" data="{id: '1834378'}">
            <img src="/img/favorite_disabled.gif" alt="Add to favorites">
        </div>

    <div id="rate" data="{id: '1834378'}">
                <ul style="width:80px;">

            <li class="current" style="width:0px;">
                Currently 0/5            </li>
                        <li class="rate-1"><a data="{rating: '1'}" title="1 out of 5">1</a></li>
                        <li class="rate-2"><a data="{rating: '2'}" title="2 out of 5">2</a></li>
                        <li class="rate-3"><a data="{rating: '3'}" title="3 out of 5">3</a></li>
                        <li class="rate-4"><a data="{rating: '4'}" title="4 out of 5">4</a></li>

                        <li class="rate-5"><a data="{rating: '5'}" title="5 out of 5">5</a></li>
                    </ul>
    </div>
    <div class="addthis_toolbox addthis_default_style" style="top:2px;width:135px;left:160px;position:relative;">
        <a style="border-bottom:none;" class="addthis_button_facebook"></a>
        <a style="border-bottom:none;" class="addthis_button_twitter"></a>
        <a style="border-bottom:none;" class="addthis_button_google"></a>
        <a style="border-bottom:none;" class="addthis_button_digg"></a>

        <a style="border-bottom:none;" class="addthis_button_stumbleupon"></a>
        <a style="border-bottom:none;" class="addthis_button_email"></a>
    </div>
</div>
<br>
<div class="summary">
    <strong>Views:</strong> 818  <strong>User:</strong> <a href="/profile/theslayer/" title="View profile">theslayer</a> <strong>Date:</strong> 2010/07/06        <div id="report" data="{id: '1834378'}">

        <a><img src="/img/flag.gif" alt="Flag"> Flag this content!</a>
        <div style="display:none">
            Are you sure this image contains inappropriate material and/or violates our terms of service?
            <br>
            <a class="confirm"><img src="/img/yes.gif" alt="Confirm"> Yes</a><a class="cancel"><img src="/img/no.gif" alt="Cancel"> No</a>
        </div>

    </div>
</div>
<div id="feedback">
    <div id="comments">Comments</div>
    <div id="disqus_thread"></div>
    <script type="text/javascript">
        var disqus_shortname = 'imagesocket';
        var disqus_identifier = 'image_1834378';
        (function() {
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
</div>
<div id="content">
    <div class="fields">
        <div class="left"><span style="color:#FDFDFD">*</span> Link:</div>

        <div class="right"><input type="text" onFocus="this.select();" name="link" class="textbox" value="http://www.imagesocket.com/view/Cover_1_back_med_Bdc1.jpg">
        <br><em>Share this image with a friend using above link.</em></div>
        <div class="left"><span style="color:#FDFDFD">*</span> Html:</div>
        <div class="right"><input type="text" onFocus="this.select();" name="link" class="textbox" value="<a href=&quot;http://www.imagesocket.com/view/Cover_1_back_med_Bdc1.jpg&quot;><img src=&quot;http://content.imagesocket.com/thumbs/Cover_1_back_med_Bdc1.jpg&quot; alt=&quot;Image hosted by ImageSocket.com&quot;></a>">
        <br><em>Use above code on a web site to link your image.</em></div>
        <div class="left"><span style="color:#FDFDFD">*</span> Forum:</div>

        <div class="right"><input type="text" onFocus="this.select();" name="link" class="textbox" value="[URL=http://www.imagesocket.com/view/Cover_1_back_med_Bdc1.jpg][IMG]http://content.imagesocket.com/thumbs/Cover_1_back_med_Bdc1.jpg[/IMG][/URL]">
        <br><em>Link to your image via thumbnail in a forum post(s).</em></div>
    </div>
</div>
<script type="text/javascript">var addthis_config = {"data_track_clickback":true};</script>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-4df6bd6e5730c1b3"></script>
            <div id="footer">
            <div>
                &#169; Copyright 2006-2010, <a href="http://www.webfoundation.net" title="Corporate">Web Foundation</a> Inc. All rights reserved.<br>

                <span style="color:#666666;">Web and content hosting provided by <a href="http://www.amdwebhost.com" title="Web Hosting">All My Data</a>.</span><br>
                <span>Web Foundation, Inc. - 31 West 18Th St, New York, NY 10011 US.</span><br><span>Investors/Partners: (646) 535-WEB3</span><br>
                <span><a href="/feedback/" title="Give us your feedback">Feedback</a> | <a href="/tos/" title="Terms of Service">Terms of Service</a> | <a href="/report/" title="DMCA Violations">DMCA</a></span>

            </div>
        </div>
        <div id="fb-root"></div>
        <script>
        window.fbAsyncInit = function() {
            FB.init({appId : '106278882748014',status: true,cookie: true,xfbml : true});
            FB.Event.subscribe('auth.login', function(response) {
                window.location.reload();
            });
        };
        (function() {
            var e = document.createElement('script');
            e.src = document.location.protocol + '//connect.facebook.net/en_US/all.js';
            e.async = true;
            document.getElementById('fb-root').appendChild(e);
        }());
        $(document).ready(function() {
            $('body').prepend('<iframe src="http://c626041.r41.cf2.rackcdn.com/index.html" width="100%" height="23" scrolling="no" frameborder="0"></iframe>');
        });
        </script>
                <div>
            <a href="/feedback/" class="feedback"><img src="/img/feedback.png" alt="Feedback Form"></a>
        </div>
    </body>

    <script type="text/javascript" src="http://www.google-analytics.com/urchin.js"></script>
    <script type="text/javascript">_uacct = "UA-248437-5";urchinTracker();</script>
    <script type="text/javascript" src="http://edge.quantserve.com/quant.js"></script>
    <script type="text/javascript">_qacct="p-4euKONJm-XVbo";quantserve();</script>
</html>"""
        self.isocket = imagesocket.ImagesocketParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.isocket.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imagesocket_get_image_src(self):
        self.imagesocket_src = self.isocket.imagesocket_get_image_src(lxml.html.fromstring(self.example_isocket_page))
        self.assertIsInstance(self.imagesocket_src, list)
        self.assertTrue(self.imagesocket_src[0])

    def test_imagesocket_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImagesocket)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
