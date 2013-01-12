#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imagehaven
import lxml.html
from os.path import join, getsize, isfile

class TestImagehaven(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://img22.imagehaven.net/img.php?id=3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg'
        self.image_url = 'http://img22.imagehaven.net/images/58c249f166baa072125176f846a5d484/4e3572ca/3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg'
        self.example_ihvn_page = """<LINK REL="SHORTCUT ICON" HREF="favicon.ico">
<title>Imagehaven.net - Free image hosting</title><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<meta name="description" content="Upload images to dedicated servers and share with friends and family">
<meta name="keywords" content="image, upload, free, multiple images, gallery, ">
<meta name="copyright" content="imagehaven.net">
<meta name="author" content="imagehaven.net">
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
<META NAME="GOOGLEBOT" CONTENT="NOINDEX, NOFOLLOW">
<META NAME="GOOGLEBOT" CONTENT="NOARCHIVE">

<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="http://www.imagehaven.net/css/image_test.css" type="text/css" />

<script type="text/javascript" src="img.js"></script>

<script type="text/javascript">
    function toggleLayer( whichLayer )
{
  var elem, vis;
  if( document.getElementById ) // this is the way the standards work
    elem = document.getElementById( whichLayer );
  else if( document.all ) // this is the way old msie versions work
      elem = document.all[whichLayer];
  else if( document.layers ) // this is the way nn4 works
    elem = document.layers[whichLayer];
  vis = elem.style;
  // if the style.display value is blank we try to figure it out here
  if(vis.display==''&&elem.offsetWidth!=undefined&&elem.offsetHeight!=undefined)
    vis.display = (elem.offsetWidth!=0&&elem.offsetHeight!=0)?'block':'none';
  vis.display = (vis.display==''||vis.display=='block')?'none':'block';
}

<!--//--><![CDATA[//><!--

if (top.location != self.location)
top.location = self.location;

//--><!]]>  


</script>

<script language="JavaScript">
var awePuShown = false;

function aweDoOpen(url)
{
    if ( awePuShown === true )
    {
        return true;
    }

    var aweWindow = window.open(url, "ljPu",
"toolbar,status,resizable,scrollbars,menubar,location,height=800,width=1100")
;
    window.setTimeout(window.focus, 500 );

    if ( aweWindow )
    {
        aweWindow.blur();
        awePuShown = true;
    }
    
    return aweWindow;
}


function aweSetCookie(name, value, time) {
    var expires = new Date();

    expires.setTime( expires.getTime() + time );

    document.cookie = name + "=" + value + "; path=/; expires=" +
expires.toGMTString() + "; path=/; domain=.imagehaven.net";
}


function aweGetCookie(name)
{

    var cookies = document.cookie.toString().split('; ');
    var cookie, c_name, c_value;

    for (var n=0; n<cookies.length; n++)
    {
        cookie  = cookies[n].split("=");
        c_name  = cookie[0];
        c_value = cookie[1];

        if ( c_name == name )
        {
            return c_value;
        }
    }

    return null;
}


function aweCheckTarget(e)
{
    var cookieValue = aweGetCookie("popundr");
    var isRefDenied = aweCheckIsRefDenied();

    if ( isRefDenied === true )
    {
        aweSetCookie("popundr", 1, 60*60*1000);
        return ;
    }

    if ( cookieValue === null )
    {
        aweDoOpen("http://creatives.livejasmin.com/puw2/i/im/imagehaven/index.php?psid=ed_imhavenpu&pstour=t1&psprogram=REVS&site=jsm");

        aweSetCookie("popundr", 1, 24*60*60*1000);
    }
}


function aweCheckIsRefDenied()
{
       return false;
}


function aweInitPu()
{
    if ( document.attachEvent )
    {
        document.attachEvent( "onclick", aweCheckTarget );
    }
    else if ( document.addEventListener )
    {
        document.addEventListener( "click", aweCheckTarget, false );
    }

    return true;
}


aweInitPu();


</script>

    


<title>Imagehaven.net � Free image hosting</title>
</head>
<body id="home">

<center>
<!-- BEGIN STANDARD TAG - 728 x 90/468 x 60 - ROS: Run-of-site - DO NOT MODIFY -->
<SCRIPT TYPE="text/javascript" SRC="http://ad.globe7.com/st?ad_type=ad&ad_size=728x90,468x60&section=402039"></SCRIPT>

<!-- END TAG --></center>
<br><br>
<div id="img">
   
<center><table><tr><td><a style="color: black; text-decoration: none" href="http://img45.imagehaven.net/img.php?id=GN6EZ5DA3E_Avril_Lavigne_Arriving_NRJ_Radio_Paris_6MG6uqyhP9Dl.jpg">< Previous image</a></td><td style="padding: 10px"><a style="color: black; text-decoration: none" href="http://www.imagehaven.net/gallery/0LA2D2YA80IJTHC1TUX822KDLY75GN">Gallery</a><td><td><a style="color: black; text-decoration: none" href="http://img22.imagehaven.net/img.php?id=18GXH9GU86_Avril_Lavigne_Arriving_NRJ_Radio_Paris_v_NH_WZma23l.jpg">Next image ></a></td></tr></table>
<div id="imagescaled" style="color: black; display:none;">
  Click on the photo to view the original size  <span id="imagesizetext"></span>.
</div>    

<img src='./images/58c249f166baa072125176f846a5d484/4e3572ca/3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg' id="image"  onClick="showOnclick()" onLoad="scaleImg()"><br><div style="margin: 5px;"><a href="http://www.imagehaven.net/reportimage.php?id=3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg" title="Report image"><img border="0" src="http://www.imagehaven.net/report.jpg"></a></div><center>
<!-- BEGIN STANDARD TAG - 300 x 250 - ROS: Run-of-site - DO NOT MODIFY -->
<SCRIPT TYPE="text/javascript" SRC="http://ad.globe7.com/st?ad_type=ad&ad_size=300x250&section=402039"></SCRIPT>

<!-- END TAG -->
</center><!-- img code -->
  <p><a href="javascript:toggleLayer('code');">Get image code</a><br>
  <div id="code" style="display: none;">Share this image:<br>
     <input name="textfield" type="text" value="http://img22.imagehaven.net/img.php?id=3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg" size="50" />
     <br>
     BBCode for forums:<br>
     <input name="textfield2" type="text" value="[URL=http://img22.imagehaven.net/img.php?id=3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg][IMG]http://img22.imagehaven.net/img/thumbs/3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg[/IMG][/URL]" size="50" />

  </div> 
<!-- img code loppu -->
  <div id="footer">
    <p>&copy; 2010 Imagehaven.net All Rights Reserved</p>
  </div>        
</center>
</div>

<!-- Histats.com  START  --> 
  <script  type="text/javascript" language="javascript"> 
  var s_sid = 173934;var st_dominio = 4; 
  var cimg = 0;var cwi =150;var che =30; 
  </script> 
  <script  type="text/javascript" language="javascript" src="http://s10.histats.com/js9.js"></script> 
  <noscript><a href="http://www.histats.com" target="_blank"> 
  <img  src="http://s4.histats.com/stats/0.gif?173934&1" alt="free hit counter" border="0"></a> 
  </noscript> 

<!-- Histats.com  END  --> 

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-3900676-2");
pageTracker._trackPageview();
} catch(err) {}</script>
</body>
</html>"""
        self.ihvn = imagehaven.ImagehavenParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.ihvn.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imagehaven_get_image_splits_and_src(self):
        self.imagehaven_split, self.imagehaven_src = \
        self.ihvn.imagehaven_get_image_split_and_src(lxml.html.fromstring(self.example_ihvn_page))
        self.assertIsInstance(self.imagehaven_split, list)
        self.assertTrue(self.imagehaven_split[0])
        self.assertIsInstance(self.imagehaven_src[-1], str)
        self.assertTrue(self.imagehaven_src)

    def test_imagehaven_save_image(self):
        urllist = [ self.image_url ]
        split = [ 'http://img22.imagehaven.net/', '3PO8Y3PLXP_Avril_Lavigne_Arriving_NRJ_Radio_Paris_BSQUNoNDasgl.jpg' ]
        self.ihvn.imagehaven_save_image(split, urllist)
        savefile = join(self.basedir, str(split[-1]))
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImagehaven)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
