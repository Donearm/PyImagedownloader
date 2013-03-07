#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imgchili
import lxml.html
from os.path import join, getsize, isfile

class TestImgchili(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://imgchili.com/show/2765/2765317_9.jpg'
        self.image_url = 'http://i1.imgchili.com/2765/2765317_9.jpg'
        self.example_chiliimage_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Language" content="en-us" />
    <meta http-equiv="imagetoolbar" content="no" />
    
    <title>imgChili &raquo; 2765317_9.jpg</title>
   
    <meta name="version" content="imgChili" />

    <meta name="description" content="imgChili is the free image hosting solution for everyone. With imgChili you can upload your images and photos, categorize them, share them with friends, and you can even make money out of this!" />

    <meta name="keywords" content="image hosting, image hosting service, multiple image hosting, unlimited bandwidth, free image hosting" />
            
    <base href="http://imgchili.com/" />

    <link rel="shortcut icon" href="./theme/images/favicoc.ico" />
    <link href="theme/style.css" rel="stylesheet" type="text/css" media="screen" />
        <script type="text/javascript"> 
    var a = "<a class=\"removeAds2\" href=\"premium\" target=\"_blank\">Remove ads [x]<\/a><iframe src='http://www.streamate.com/landing/2/?AFNO=1-0-630365-341541&UHNSMTY=303' style='width:1028px;height:900px;border:0px;'></iframe>";
    var x = "";
    </script>
    
    <script type="text/javascript" src="source/includes/scripts/jquery.js"></script>

    <script type="text/javascript" src="source/includes/scripts/genjscript.js"></script>
    <script type="text/javascript" src="source/includes/scripts/phpjs_00029.js"></script>

    <script type="text/javascript" src="source/includes/scripts/jquery.jdMenu.js"></script>
    <script type="text/javascript" src="source/includes/scripts/jquery.bgiframe.js"></script>
    <script type="text/javascript" src="source/includes/scripts/jquery.positionBy.js"></script>
    <script type="text/javascript" src="source/includes/scripts/jquery.dimensions.js"></script>

    <script type="text/javascript" src="/js/maxlines.js"></script>
    <!-- <# JSHOOK_GCHART #> -->

<!--[if lt IE 7]>
    <script src="/js/pngfix.js" type="text/javascript"></script>
    <script>DD_belatedPNG.fix('.pngfix');</script>
<![endif]-->
        <script type="text/javascript">
            function loginMenu(){
                if (document.getElementById('loginMenu').style.display == 'none'){
                    document.getElementById('loginMenu').style.display = 'block';
                    $("#loginTab").attr("class","button6");


                }else{
                    document.getElementById('loginMenu').style.display = 'none';
                    $("#loginTab").attr("class","button3");
                }
            }



        </script>
<script type="text/javascript">
    <!--
        if (top.location!= self.location) {
            top.location = self.location.href
        }
    //-->
</script>

<script language="vbscript" type="text/vbs">

set_ie_alert()

Function vb_alert(msg_str)
MsgBox msg_str,vbOKOnly+vbInformation+vbApplicationModal,alert_title
End Function

</script>
</head>
<body>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-23829964-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
<!-- Place this tag in your head or just before your close body tag -->
<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
<script type="text/javascript" src="//platform.twitter.com/widgets.js"></script>

<div id="ad" style="font-size:17px;padding:5px;display:none;"></div>
<div id="all">

<div class="members_bar">

                    <div class="guest_links">

                <a onmouseover="loginMenu();" id="loginTab" class="button3" href="#">Log In</a>&nbsp;

<a href="signup" class="button3" >Register</a>
                <div id="loginMenu" class="button5" style="display: none;">
                    <form action="users.php?act=login-d" method="post">

                        <p><label>Username:&nbsp;</label><input name="username" class="textfield" type="text" /></p>

                        <p><label>Password:&nbsp;</label><input name="password" class="textfield" type="password" /></p>

                        <br /><br /><p><a href="javascript:void(0);" onclick="toggle_lightbox('users.php?act=lost_password', 'lost_password_lightbox');">Reset Password</a> &nbsp; <input type="submit" value="Log In" class="button1" /></p>

                    </form>

                </div>
            </div>
            </div>

    <div class="logo_cell">  
    <a href="./" style="float: left;" class="logo"></a>        <div style=""><img src="./theme/images/blank.gif" height="0" width="0" alt="blank" /></div>  



        <ul id="navlink">
            <li><a href="./blog" class="navlink">News</a></li>

                                    <li><a href="/premium" class="navlink">Premium</a></li>
                    <li><a href="./affiliate" class="navlink">Affiliate</a></li>
            <li><a href="./tools" class="navlink">Tools</a></li>                                                            
                                                                </ul>
</div> 

                <div class="page_cell">  
    <div id="page_body" class="page_body"><script type="text/javascript">
    // <![CDATA[
var scaled = false;

function scaleonload(){
    e = document.getElementById('show_image');
    scale(e);
}

function scale(e){

    if(scaled){
        e.width=originalWidth;
        e.height=originalHeight;
        scaled=false;
    }else{
        if(e.width>908){
            originalWidth = e.width;
            originalHeight = e.height;
            e.style.cursor = "url(/theme/magnify.cur), default";
            e.width=908;
            e.height = Math.ceil(908*(originalHeight/originalWidth));
            scaled=true;
        }
    }
}

// ]]>

</script>
            <center>
    

<div class="sidebar2">
    <div>
        <a class="removeAds" href="premium">Remove ads [x]</a>
    </div>
<a href="http://www.3dtoontube.com/?t=3dimgchili" target="_blank"><img src="http://imgchili.com/media/tube/728x90h.jpg" alt="3dtoontube" /></a>
</div>
</center>
            
<script src="/js/showa.js" type="text/javascript"></script>




    <center><br />  <img id="show_image" onload="scale(this);" onclick="scale(this);"  src="http://i1.imgchili.com/2765/2765317_9.jpg" alt="2765317_9.jpg" /></center>

    

<div>
    <table cellpadding="4" cellspacing="1" border="0" style="width: 100%;">
        <tr>
            <td colspan="2" class="tdrow2">
                <center> <script src="http://www.stumbleupon.com/hostedbadge.php?s=1"></script> &nbsp; &nbsp; <a href="https://twitter.com/share" class="twitter-share-button" data-count="horizontal">Tweet</a> <g:plusone size="medium"></g:plusone></center>

        </td>
        </tr>
        <tr>
            <td colspan="2" class="tdrow2">
            <div class="sidebar">
    <div>
        <a class="removeAds" href="/premium">Remove ads [x]</a>
    </div>

            <center><iframe src='http://feeds.videosz.com/spots/index.php?sid=86' frameborder='0' scrolling='no' width='600' height='260'></iframe></center>
</div>
            </td>
        </tr>
        <tr>
            <td colspan="2" class="tdrow2"><br /><br />


<table cellpadding="5" cellspacing="0" border="0" style="width: 100%;">

    <tr>
        <td style="width: 20%;" valign="middle" class="text_align_center">
            <a href="http://imgchili.com/show/2765/2765317_9.jpg"><img src="http://t1.imgchili.com/2765/2765317_9.jpg" alt="2765317_9.jpg" /></a>
        </td>
        
        <td style="width: 80%;">

            <table cellspacing="1" cellpadding="0" border="0" style="width: 100%;">

                <tr>
                    <td><input readonly="readonly" class="input_field" onfocus="javascript: this.select()" type="text" style="width: 555px;" value="http://imgchili.com/show/2765/2765317_9.jpg" /></td>

                    <td>Share Link</td>
                </tr>
                <tr>
                    <td><input readonly="readonly" class="input_field" onfocus="javascript: this.select()" type="text" style="width: 555px;" value="&lt;a href=&quot;http://imgchili.com/show/2765/2765317_9.jpg&quot; target=&quot;_blank&quot;&gt;&lt;img src=&quot;http://t1.imgchili.com/2765/2765317_9.jpg&quot; border=&quot;0&quot; alt=&quot;2765317_9.jpg&quot; /&gt;&lt;/a&gt;" /></td>
                    <td>Thumbnail for Website</td>

                </tr>
                <tr>

                    <td><input readonly="readonly" class="input_field" onfocus="javascript: this.select()" type="text" style="width: 555px;" value="[URL=http://imgchili.com/show/2765/2765317_9.jpg][IMG]http://t1.imgchili.com/2765/2765317_9.jpg[/IMG][/URL]" /></td>
                    <td>Thumbnail for Forum</td>
                </tr>
                <tr>
                    <td><input readonly="readonly" class="input_field" onfocus="javascript: this.select()" type="text" style="width: 555px;" value="&lt;a href=&quot;http://imgchili.com/&quot;&gt;Free image hosting&lt;/a&gt; by imgChili." /></td>
                    <td>Link to Us</td>

                </tr>

            </table>
        </td>
    </tr>
</table>
</td>
        </tr>
        <tr>
            <td colspan="2" class="table_footer">&nbsp;</td>
        </tr>

    </table>
</div>
            </div>
    </div>

    <div id="footer_cell" class="footer_cell"><table align="center" border="0" cellpadding="1" cellspacing="0" width="100%">
  <tbody><tr>               <td align="left">
            <a class="footer-content" href="./">Home</a>  | 
            <a class="footer-content" href="./abuse">Report abuse</a>  |  
            <a class="footer-content" href="./tos">ToS</a>  |
            <a class="footer-content" href="./privacy_policy">Privacy policy</a> |
            <a class="footer-content" href="./faq">FAQ</a> |
            <a class="footer-content" href="./forum">Support</a>

        </td>
        <td class="footer-content" align="right">Copyright &copy; 2011 - 2012 imgChili. All rights reserved</td>
    </tr></tbody>
  

</table></div></div>

<br />
                        <script type='text/javascript' src='http://static.creatives.livejasmin.com/marketing_javascript/popunder/i/im/imgchilli/imgchilli.js'></script>                        </body>

</html>"""
        self.chiliimage = imgchili.ImgchiliParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.chiliimage.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imgchili_get_image_src(self):
        self.imgchili_src = self.chiliimage.imgchili_get_image_src(lxml.html.fromstring(self.example_chiliimage_page))
        self.assertIsInstance(self.imgchili_src, list)
        self.assertTrue(self.imgchili_src[0])

    def test_imgchili_get_image_name(self):
        self.imagename = self.chiliimage.imgchili_get_image_name(self.image_url)

        self.assertIsInstance(self.imagename, list)

    def test_imgchili_save_image(self):
        urllist = []
        urllist.append(self.image_url)
        urlnamelist = []
        urlnamelist.append('testname.jpg')
        self.chiliimage.imgchili_save_image(urllist, urlnamelist)
        savefile = join(self.basedir, urlnamelist[-1])
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImgchili)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
