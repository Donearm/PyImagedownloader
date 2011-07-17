#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import turboimagehost
import lxml.html

class TestTurboimagehost(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://www.turboimagehost.com/p/5787190/La_Senza.jpg.html'
        self.example_turbo_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>La Senza.jpg - Free Image Hosting at TurboImageHost</title>
<meta name="description" content="Uploaded image: La Senza.jpg" />
<meta name="keywords" content="La Senza.jpg, free image hosting, image hosting, photo sharing, free picture hosting, picture hosting, picture host, image host, free image host, image hosting site" />
<meta name="robots" content="index, follow, all" /> 
<link href="/style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript">

var imWidth = 2000; 
var imHeight = 2000; 

function scaleImg() {
im = document.getElementById('imageid');
//imHeight= image.height; 
//imWidth= image.width;
if (  FIW() ) return true;

im.width=900;
im.height = (imHeight/imWidth) * im.width;
document.getElementById('minus').style.display= 'none';
document.getElementById('plus').style.display= '';
return true;
}

function OC() {
    im = document.getElementById('imageid');

    if (imWidth == im.width)
            return scaleImg();
    else if (imWidth > im.width)
    {
        im.width=imWidth;
        im.height=imHeight;
        document.getElementById('plus').style.display= 'none';
        document.getElementById('minus').style.display= '';
    }
    return true;
}

function FIW() {
   im = document.getElementById('imageid');
  if (imWidth<=900) {
      return true;
  } else {
      return false;
  }
}
</script>



<STYLE type="text/css">

#blanket {
background-color:#111;
opacity: 0.65;
filter:alpha(opacity=65);
position:absolute;
z-index: 9001;
top:0px;
left:0px;
width:100%;
}
#popUpDiv1 {
font-size:17px;
position:absolute;
background-color:#ffffff;
width:300px;
height:130px;
z-index: 9002;
text-align:center; 
border:5px solid #000000; 
padding:20px;
}

</STYLE>

<script type="text/javascript">


function toggle(div_id) {
    var el = document.getElementById(div_id);
    if ( el.style.display == 'none' ) { el.style.display = 'block';}
    else {el.style.display = 'none';
    aweSetCookie("entercook", 1, 24*60*60*1000);
    
    }
}
function blanket_size(popUpDiv1Var) {
    if (typeof window.innerWidth != 'undefined') {
        viewportheight = window.innerHeight;
    } else {
        viewportheight = document.documentElement.clientHeight;
    }
    if ((viewportheight > document.body.parentNode.scrollHeight) && (viewportheight > document.body.parentNode.clientHeight)) {
        blanket_height = viewportheight;
    } else {
        if (document.body.parentNode.clientHeight > document.body.parentNode.scrollHeight) {
            blanket_height = document.body.parentNode.clientHeight;
        } else {
            blanket_height = document.body.parentNode.scrollHeight;
        }
    }
    var blanket = document.getElementById('blanket');
    blanket.style.height = blanket_height + 'px';
    var popUpDiv1 = document.getElementById(popUpDiv1Var);
    //popUpDiv1_height=blanket_height/2-65;//150 is half popup's height
    popUpDiv1_height='250';
    popUpDiv1.style.top = popUpDiv1_height + 'px';
}
function window_pos(popUpDiv1Var) {
    if (typeof window.innerWidth != 'undefined') {
        viewportwidth = window.innerHeight;
    } else {
        viewportwidth = document.documentElement.clientHeight;
    }
    if ((viewportwidth > document.body.parentNode.scrollWidth) && (viewportwidth > document.body.parentNode.clientWidth)) {
        window_width = viewportwidth;
    } else {
        if (document.body.parentNode.clientWidth > document.body.parentNode.scrollWidth) {
            window_width = document.body.parentNode.clientWidth;
        } else {
            window_width = document.body.parentNode.scrollWidth;
        }
    }
    var popUpDiv1 = document.getElementById(popUpDiv1Var);
    window_width=window_width/2-150;//150 is half popup's width
    popUpDiv1.style.left = window_width + 'px';
}
function popup(windowname) {
    blanket_size(windowname);
    window_pos(windowname);
    toggle('blanket');
    toggle(windowname);     
}


</script>




<script language="javaScript" type="text/javascript"> 
        if (top.location != location)
            top.location.href = document.location.href; 
    </script> 

</head>

<body>
<div id="main" style="width:900px;margin-top:3px;padding-bottom:0px;border-bottom:0px;">
  <div align="center" id="ads"> 
  

    <iframe src="/728.html?" width="728" height="140" style="border:none;" scrolling="no" frameborder=0></iframe>

      </div>
  
  <div id="menu"><a href="http://www.turboimagehost.com">Image Hosting</a> | <a href="/addtoforum.tu">Add Image Hosting to Your Forum</a> | <a href="/forum" target="_blank">Forum</a> | <a href="/tos.html" target="_blank">ToS</a> | <script language=javascript type="text/javascript">
<!-- 
var user = "contact"; 
var host = "turboimagehost.com"; 
var linktext = user + "@" + host; 
document.write("<a href=" + "mail" + "to:" + linktext +">Contact Us<" + "/a>") 
//--> </script></div>


  <div id="title-shhowi" class="title">
  <span id="minus" style="display:none"><a href="javascript:void(0);" onClick="OC();"><img src="http://www.turboimagehost.com/images/minus.gif" border="0" /> Normal Image Size (Best Fit) - </a></span>
  <span id="plus" style="display:none"><a href="javascript:void(0);" onClick="OC();"><img src="http://www.turboimagehost.com/images/plus.gif" border="0" /> Original Image Size</a> - </span>
  La Senza.jpg - 2000x2000 (270.32 KB) -  
 <script language=javascript type="text/javascript">
<!-- 
var user = "abuse"; 
var host = "turboimagehost.com?subject=Illegal_file_5787190_s2"; 
var linktext = user + "@" + host; 
document.write("<a href=" + "mail" + "to:" + linktext +">Report Abuse<" + "/a>") 
//--> </script>

          </div>
  

  </div>
    
  <a href="http://www.turboimagehost.com"><img src="http://s2d3.turboimagehost.com/sp/b66b32b24b95b7055395adb2ad7a08e8/La_Senza.jpg" class="upimage" id="imageid" border="0" alt="free image hosting" onLoad="scaleImg(); "/></a>
  <div style="margin-top:3px;text-align:center;font-size:24px;"><strong><a href="http://www.turbochannels.com" target="_blank">Internet TV</a> | <a href="http://fileservetrend.com" target="_blank">FileServe Search</a> | <a href="http://mediafiretrend.com" target="_blank">Mediafire Search</a> | <a href="http://megauploadtrend.com" target="_blank">Megaupload Search</a></strong></div>

  </div>
  <div id="main" style="width:850px;margin-top:3px;">
  <div style="float:left;width:570px;">
  
  <div id="title-showi-more" class="title">PUBLIC IMAGES</div>
  
  <div style="float:right;width:305px;">

<iframe src="/300.html?" width="300" height="250" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no"></iframe>


  </div>
  
  <div style="clear:left;"></div>
  
  <div id="showi-more">
  <ul style="float:left;width:50%;">
  <li></li>  </ul>
  <ul style="float:right;width:50%;">
   <li></li>  </ul>

  </div>
  </div>
  <div id="title-showi-codes" class="title">IMAGE CODES</div>
  <div style="clear:right;"></div>
  <div id="showi-codes">
  Clickable Thumbnail for Websites:<br />
<input type="text" onClick="select(this);" class="codes1" value="&lt;a href=&quot;http://www.turboimagehost.com/p/5787190/La_Senza.jpg.html&quot; target=&quot;_blank&quot;&gt;&lt;img src=&quot;http://s2d3.turboimagehost.com/t/5787190_La_Senza.jpg&quot; border=&quot;0&quot; alt=&quot;Free Image Hosting&quot; /&gt;&lt;/a&gt;" />
<br />
Clickable Thumbnail for Forums (1):<br />

<input type="text" onClick="select(this);" class="codes1" value="[URL=http://www.turboimagehost.com/p/5787190/La_Senza.jpg.html][IMG]http://s2d3.turboimagehost.com/t/5787190_La_Senza.jpg[/IMG][/URL]" /> 
<br />
Clickable Thumbnail for Forums (2):<br />
<input type="text" onClick="select(this);" class="codes1" value="[url=http://www.turboimagehost.com/p/5787190/La_Senza.jpg.html][img=http://s2d3.turboimagehost.com/t/5787190_La_Senza.jpg][/url]" /> 
<br />
Show image to friends:<br />
<input type="text" onClick="select(this);" class="codes1" value="http://www.turboimagehost.com/p/5787190/La_Senza.jpg.html" /> 
<br />
Link back to us on forums (thanks):<br />
<input type="text" onClick="select(this);" class="codes1" value="Thanks to TurboImageHost for [URL=http://www.turboimagehost.com]Free Image Hosting[/URL]" />
  </div>
  <div class="clear"></div>


  
  
</div>
<div id="footer">&copy;2006-2011 TurboImageHost.com - <a href="http://www.turboimagehost.com">Image Hosting</a></div>

<div id="blanket" style="display:none;"></div>
<div id="popUpDiv1" style="display:none;">
Press <strong>ENTER</strong> to agree to use TurboImageHost.com in accordance with our rules.
<br /><br />

<a href="#" onClick="popup('popUpDiv1')" style='font-size:18px;'><font color="red"> 

ENTER
</font>
</a>
<br />
<br />
<a href='http://www.turboimagehost.com/tos.html' target='_blank' style='font-size:11px;'>OUR TOS</a><br>
</div>





<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-508314-4";
urchinTracker();
</script>







</body>
</html>"""
        self.turbo = turboimagehost.TurboimagehostParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.turbo.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_turboimagehost_get_image_src(self):
        self.turboimagehost_src = self.turbo.turboimagehost_get_image_src(lxml.html.fromstring(self.example_turbo_page))
        self.assertIsInstance(self.turboimagehost_src, list)
        self.assertTrue(self.turboimagehost_src[0])

    def test_turboimagehost_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTurboimagehost)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
