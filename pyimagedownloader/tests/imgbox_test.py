#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imgbox
import lxml.html
from os.path import join, getsize, isfile

class TestImgbox(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://imgbox.com/aaaHwL9s'
        self.image_url = 'http://o.imgbox.com/aaaHwL9s.jpg'
        self.example_ibimage_page = """<!DOCTYPE html> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"> 
<head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
  <title>imgbox - fast, simple image host</title>
  
  <meta name="description" content="Use imgbox to upload, host and share all your images. It's simple, free and blazing fast!" />
  <meta name="keywords" content="image host, image upload, image hosting, share images, free image host" />
 
  <meta name="ROBOTS" content="NOINDEX, NOFOLLOW"/>
  <meta name="GOOGLEBOT" content="NOINDEX, NOFOLLOW"/>
  <meta name="GOOGLEBOT" content="NOARCHIVE"/>

    <link rel="shortcut icon" href="/images/favicon.ico" type="image/x-icon" /> 
      <link rel="apple-touch-icon" href="/images/apple-touch-icon.png" />

 <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
 <script type="text/javascript" src="/javascripts/jgestures.min.js"></script>

  <style type="text/css">
    html, body { 
        background: url(/images/background-body.png) #262626;
        color: #fdfeff; /*#FFF*/
        padding:0px; 
        margin:0px; 
        height:100%; 
        position:relative; 
        font-family: "Helvetica Neue","HelveticaNeue",Helvetica,Arial, sans-serif;
        font-size:12px;
    }

    select, a { outline:none; }

    a{
        color:orange;
    }

    #logo img{
        border:0px;
    }
    

    #push{
        height:16px;
    }

    #wrapper{
        min-height: 100%;
        height: auto !important;
        height: 100%;
        margin: 0 auto -16px;   
    }

    #head{
        background: url(/images/background-header.png) repeat-x #1C1C1C;
        height:49px;
        line-height:47px;
        margin:auto;
        margin-bottom:16px;

    }

    #header_links{
        float:right;
    }

    

    #head div{
        padding-left:22px;
        padding-right:22px;
    }

    #head div img{
        vertical-align:middle;
    }

    #logo{
        color:#e49938;
        text-decoration:none;
        font-weight:bold;
        font-style:italic;
    }
    
    
    #rs_info{
        margin-top:6px;
        color:#9e9e9e;
        text-align:center;
        font-size:11px;
    }
    
    .cont_rs{
        margin-left:20px;
        margin-right:20px;
        padding-right:20px;
        display:absolute;
        text-align:center;
        
        
        
    }
    
    .cont_rs img{
        max-width:100%;
        background: url(/images/background-box.png) #262626;
        border:1px solid #373737;
        -moz-border-radius: 5px 5px 5px 5px;
        -webkit-border-radius: 5px 5px 5px 5px;
        border-radius:  5px 5px 5px 5px;
        behavior: url(/stylesheets/PIE.htc);
        position:relative;
        padding:9px;
    }
    
    .cont_no_rs{
        
    }
    
    
    
    #img{
        cursor:pointer;
    }
    
    #nav{
        text-align:right;
        padding-right:30px;
        padding-left:30px;
        margin-bottom:20px;
        margin-top:15px;
    }
    
    #nav a{
        border:1px solid orange;
        background-color:black;
        line-height:18px;
        font-size:14px;
        padding:4px 8px 4px 8px;
        
        color:orange;
        text-decoration:none;
        -moz-border-radius: 5px 5px 5px 5px;
        -webkit-border-radius: 5px 5px 5px 5px;
        border-radius:  5px 5px 5px 5px;
        behavior: url(/stylesheets/PIE.htc);
        position:relative;
    }
    
    h1{
        float:left;
        margin:0px;
        font-size:18px;
        line-height:18px;
    }
    
    .button_small{
        padding:0px;
        border:1px solid #424242;
        padding:5px 8px 5px 8px;
        text-align:center;
        vertical-align:middle;
        background:silver;
        background:url("/images/header-bg.png") repeat-x scroll 0 0 #242424;
        color:white;
        font-size:12px;
        text-decoration:none;
        margin:0px;
        -moz-border-radius: 5px 5px 5px 5px;
        -webkit-border-radius: 5px 5px 5px 5px;
        border-radius:  5px 5px 5px 5px;
        position:relative;
        behavior: url(/stylesheets/PIE.htc);
    }
    
    .button_small_disabled{
        padding:0px;
        border:1px solid #424242;
        padding:5px 8px 5px 8px;
        text-align:center;
        vertical-align:middle;
        background:silver;
        background:url("/images/header-bg.png") repeat-x scroll 0 0 #242424;
        color:#7f7f7f;
        font-size:12px;
        text-decoration:none;
        margin:0px;
        -moz-border-radius: 5px 5px 5px 5px;
        -webkit-border-radius: 5px 5px 5px 5px;
        border-radius:  5px 5px 5px 5px;
        position:relative;
        behavior: url(/stylesheets/PIE.htc);
    }
    
    .button_small:hover{
        color:orange;
    }
    
    #count{
        font-weight:bold;
        position:relative;
        text-align:center;
        top:-50px;
        width:100px;
        margin:auto;
        font-size:14px;
        margin-bottom:-25px;
    }
    
    #footer{
        height:16px;
        text-align:right;
        color:gray;
        margin:auto;
        padding-right:10px;
        font-size:10px;
    }
    
    #footer a{
        color:gray;
        text-decoration:none;
        margin-left:10px;
    }
    
  </style>
    

    
    
    
  
</head>

<body id="wbod">
    <div id="wrapper">
    <div id="head">
        <div>
        
            <a href="/" id="logo" style="margin-right:30px;"><img src="/images/imgbox.png" alt="imgbox"/></a>
        
                <a href="/g/mg5LEwECII" class="button_small">12-Playboy December 2011 (12-2011) Greece</a>
            
            
        
        
        <span id="header_links">
            
            <!--<a href="#" class="button_small">Share</a>-->
            <!--<a href="#" class="button_small">Download</a>-->

            <a href="javascript:rs();" class="button_small">Zoom</a>
            
                    <span class="button_small_disabled" style="margin-left:25px;">&larr; Previous</span>
            
                    <a href="/aaauW49A" class="button_small">Next &rarr;</a>
        </span>
        </div>
    </div><!--/head-->
    
    <div id="count">1 of 23</div>

    
    <div id="content">
        
        
        
            

<div id="cont" class="cont_rs">
<img alt="Aaahwl9s" class="box" id="img" onclick="rs()" src="http://o.imgbox.com/aaaHwL9s.jpg" title="Playboy_12-2011_Greece_Scanof.net_002.jpg" />
</div>

            
    </div>
    
    <div id="push"></div>
    </div><!--wrapper-->
    
    
    <div id="footer"><a href="/">&copy; 2011 imgbox - fast, simple image host</a>  <a href="/tos">Terms</a>  <a href="/help">Help</a>  <a href="/dmca">Report Abuse</a></div>

    
    
    <script type="text/javascript">
    
    var is_resized = true;
    
    function rs(){
        
        if(is_resized){
            is_resized = false;
            
            $('#cont').removeClass("cont_rs");
            $('#cont').addClass("cont_no_rs");
        }else{
            is_resized = true;
            
            $('#cont').removeClass("cont_no_rs");
            $('#cont').addClass("cont_rs");
            
        }
    }
    
    
    
    if (document.addEventListener) {
        document.addEventListener('keypress',
        function (evt) {
            // back
            // next
            if(evt.charCode==110) loadNext();
            // close
            if(evt.charCode==120) self.close();
        },
        false
        );
    }
    
    
    function loadNext(e,o){
        top.location = "http://imgbox.com/aaauW49A";
    }
    
    
    function loadPrev(e,o){
        return;
    }
    
    jQuery(document).ready(function() {
    

    jQuery('body').bind('swiperight',loadPrev);
    jQuery('body').bind('swiperightup',loadPrev);
    jQuery('body').bind('swiperightdown',loadPrev);

    
    jQuery('body').bind('swipeleft',loadNext);
    jQuery('body').bind('swipeleftup',loadNext);
    jQuery('body').bind('swipeleftdown',loadNext);

    
    });
    
    
    </script>


    <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-26381320-1']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>
    
        <script type="text/javascript">

          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', 'UA-26381320-2']);
          _gaq.push(['_trackPageview']);

          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();

        </script>

    
</body>
</html>"""
        self.ibimage = imgbox.ImgboxParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.ibimage.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imgbox_get_image_src_and_name(self):
        self.imgbox_src, self.imagename = self.ibimage.imgbox_get_image_src_and_name(lxml.html.fromstring(self.example_ibimage_page))
        self.assertIsInstance(self.imgbox_src, list)
        self.assertTrue(self.imgbox_src[0])
        self.assertIsInstance(self.imagename, list)

    def test_imgbox_save_image(self):
        urllist = []
        urllist.append(self.image_url)
        urlnamelist = []
        urlnamelist.append('testname.jpg')
        self.ibimage.imgbox_save_image(urllist, urlnamelist)
        savefile = join(self.basedir, urlnamelist[-1])
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImgbox)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
