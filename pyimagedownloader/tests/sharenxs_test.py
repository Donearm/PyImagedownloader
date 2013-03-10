#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import unittest
import sharenxs
import lxml.html
from os.path import join, getsize, isfile

class TestSharenxs(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://www.sharenxs.com/view/?id=tb5w2bf-05161681-7d2acgb'
        self.image_url = 'http://cache.sharenxs.com/images/wz/cabb/ci/ah/bg/aa/AmberHeard1.jpg'
        self.example_snxs_page = """


<html>
<head>  

        <script src="/jquery-1.5.2.js"></script> 

<title>ShareNXS</title>
<meta name="description" content="The easy way to store, share, manage, and backup your files." />

</head>

<body style='font-family:verdana;background:white;margin:0px;' >


<script>



function hidepm(x){
    var popup_notice = document.getElementById('popup_notice');
    popup_notice.style.visibility='hidden';
    popup_notice.style.display='none';

    // mark message as read
    if (x){
        $.post("/messages/read.php", { zid: "" + x + "" });
    }

}




</script>



        





<script type="text/javascript" language="JavaScript">
<!-- Copyright 2006,2007 Bontrager Connection, LLC
// http://bontragerconnection.com/ and http://www.willmaster.com/
// Version: July 28, 2007
var cX = 0; var cY = 0; var rX = 0; var rY = 0;
function UpdateCursorPosition(e){ cX = e.pageX; cY = e.pageY;}
function UpdateCursorPositionDocAll(e){ cX = event.clientX; cY = event.clientY;}
if(document.all) { document.onmousemove = UpdateCursorPositionDocAll; }
else { document.onmousemove = UpdateCursorPosition; }
function AssignPosition(d) {
if(self.pageYOffset) {
    rX = self.pageXOffset;
    rY = self.pageYOffset;
    }
else if(document.documentElement && document.documentElement.scrollTop) {
    rX = document.documentElement.scrollLeft;
    rY = document.documentElement.scrollTop;
    }
else if(document.body) {
    rX = document.body.scrollLeft;
    rY = document.body.scrollTop;
    }
if(document.all) {
    cX += rX; 
    cY += rY;
    }
d.style.right = 50 + "px";
d.style.top = (cY+10) + "px";
}
function HideContent(d) {
if(d.length < 1) { return; }
document.getElementById(d).style.display = "none";
}
function ShowContent(d) {
    if(d.length < 1) { return; }
    var dd = document.getElementById(d);
    if (dd.style.display == "block") return;
    AssignPosition(dd);
    dd.style.display = "block";
}

function ReverseContentDisplay(d) {
if(d.length < 1) { return; }
var dd = document.getElementById(d);
AssignPosition(dd);
if(dd.style.display == "none") { dd.style.display = "block"; }
else { dd.style.display = "none"; }
}
//-->

var curclip = 0;







   var http_request = false;


   function makePOSTRequest(url, parameters) {
      http_request = false;
      if (window.XMLHttpRequest) { // Mozilla, Safari,...
         http_request = new XMLHttpRequest();
         if (http_request.overrideMimeType) {
            // set type accordingly to anticipated content type
            //http_request.overrideMimeType('text/xml');
            http_request.overrideMimeType('text/html');
         }
      } else if (window.ActiveXObject) { // IE
         try {
            http_request = new ActiveXObject("Msxml2.XMLHTTP");
         } catch (e) {
            try {
               http_request = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {}
         }
      }
      if (!http_request) {
         alert('Cannot create XMLHTTP instance');
         return false;
      }
      
      http_request.onreadystatechange = alertContents;
      http_request.open('POST', url, true);
      http_request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      http_request.setRequestHeader("Content-length", parameters.length);
      http_request.setRequestHeader("Connection", "close");
      http_request.send(parameters);
   }



    var alreadystat = 0;

    function addstat(x){
        if (alreadystat != 1) {
            var sendthis = "id=" + x;
            //  makePOSTRequest('view_stat_post.php', sendthis);    
            alreadystat = 1;
        }
    }





   function alertContents() {
      if (http_request.readyState == 4) {
         if (http_request.status == 200) {
            result = http_request.responseText;            
    
         } else {
            
         }
      }
   }
   

































// used by tooltip



   var http_request3 = false;


   function makePOSTRequest3(url, parameters) {
      http_request3 = false;
      if (window.XMLHttpRequest) { // Mozilla, Safari,...
         http_request3 = new XMLHttpRequest();
         if (http_request3.overrideMimeType) {
            // set type accordingly to anticipated content type
            //http_request.overrideMimeType('text/xml');
            http_request3.overrideMimeType('text/html');
         }
      } else if (window.ActiveXObject) { // IE
         try {
            http_request3 = new ActiveXObject("Msxml2.XMLHTTP");
         } catch (e) {
            try {
               http_request3 = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {}
         }
      }
      if (!http_request3) {
         alert('Cannot create XMLHTTP instance');
         return false;
      }
      
      http_request3.onreadystatechange = fixContents;
      http_request3.open('POST', url, true);
      http_request3.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      http_request3.setRequestHeader("Content-length", parameters.length);
      http_request3.setRequestHeader("Connection", "close");
      http_request3.send(parameters);
   }





























</script>







<div style='text-align:center;background:gray;width:100%;color:white;font-weight:800'>
<table width=100% cellpadding=0 cellspacing=0>

<tr>

    <td  valign=top>
        &nbsp;
        <strong stlyle='font-size:8pt;'>
    <A href='/login.php' style='color:white;font-size:8pt;'>Login</a> &nbsp;&nbsp;&nbsp;
    <A href='/preferences.php' style='color:white;font-size:8pt;'>Set Preferences</a> &nbsp;&nbsp;&nbsp; 

            <a style='color:white;font-size:8pt;font-family:verdana;'  href='http://sharenxs.com/register.php' target='_blank'>Receive a free premium trial upon registration to Sharenxs.com!</a>&nbsp;&nbsp;&nbsp;

            
            <!-- 
                <a style='color:white;font-size:8pt;font-family:verdana;color:yellow' href='/'>We're experiencing server difficulties. We're working on it.</a>&nbsp;
            !-->
        </strong>
    </td>

    <td valign=top align=right>
        &nbsp;<strong>
            <a style='color:white;font-size:8pt;font-family:verdana;'  href='http://supportnxs.com/?subject=tb5w2bf-05161681-7d2acgb&site=65'>Contact Support to Report Abuse or Request Deletion</a>&nbsp;
        </strong>

    </td>



</tr>
</table>


<!--


<table width=100% cellpadding=5 cellspacing=0 style='text-align:center;background:#DCDCDC;width:100%;color:white;height:8pt;font-weight:800'>
<tr>
    <td><a href='/paypal/' style='color:blue'>This is what a premium subscription looks like...click here to find out more</a></td>
</tr>
</table>

!-->


<table width=100% cellpadding=0 cellspacing=0 style='text-align:center;background:silver;width:100%;color:white;height:8pt;font-weight:800'>
<tr>

    <td  valign=center>

        
        
<span style='font-size:10pt'>
<div style='z-index:0'>
<table border=0 cellspacing=0 cellpadding=0 align=center width=920
     style='color:white;font-family:verdana;font-size:10pt;font-weight:600;height:120px;'>
    <tr>

    <td>



    

    </td>
<!--
        <td valign=center align=center>

            <span style='line-height:6pt;'><BR>&nbsp;</span>
                                <a href='ad.php?id=3'  
                        style='text-decoration:underline;color:blue;font-size:18pt'>Just Free Pics</a>
                <BR>
            <a href ='http://justfreepics.org' style='font-size:8pt;color:blue;'>Click here to view more free  images </span>
            <BR><BR>

        </td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td align=center valign=center>


            <span style='line-height:6pt;'>&nbsp;<BR></span>                            
    

<a href='ad.php?id=19&celeb=' style='color:blue'>Click here to view <strong >58500</strong> clips at Moviesnxs.com</a>


<BR>

<a href='ad.php?id=20&celeb=' style='color:blue'>Click here to view <strong >46380</strong> clips at Reelcelebs.com</a>


            <BR><BR>

        </td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td valign=center align=center>

            <span style='line-height:6pt;'>&nbsp;<BR></span>
            
            <a href='ad.php?id=3&celeb=Amber%2BHeard'  style='text-decoration:uderline;color:blue;font-size:18pt'>Amber Heard</a><BR>
            <a href='ad.php?id=3&celeb=Amber%2BHeard' style='color:blue;font-size:8pt;'>Click here for <span style='color:white;font-size:8pt;'></span> more free images of Amber Heard</a>
    
            &nbsp;&nbsp;<BR><BR> 

        </td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <img src='' width=10 height=104 style='visibility:hidden'>
        </td>

!-->        
    </tr>
</table>

</div>

<div style='position:absolute;right:5;top:20;text-align:right;' align=right width=160 style='z-index:5'>


<div 
   id="uniquename2" 
   style="display:none; 
      position:absolute; 
      border-style: 1pt solid black; 
      background-color: white; 
      padding: 5px;">




    <table border=1 width=680 cellpadding=5 cellspacing=0 style='border:0pt solid #CACACA;'>
    <tr>
        <td width=100% align=center>

<!--START Livejasmin IFRAME-->
<iframe
src="http://creatives.livejasmin.com/iframes/s/sh/sharenxs/ifr2/index.html?psid=ed_sharenif&pstool=138_12572&pstour=t1&psprogram=REVS"
width="640" height="320" marginheight="0" marginwidth="0" allowtransparency="true" background-color="transparent"
scrolling="no" frameborder="no">
</iframe>
<!--END Livejasmin IFRAME-->

        </td>
    </tr>
    </table>



        <div style='clear:both'>&nbsp;</div>

        <a 
       onmouseover="HideContent('uniquename2'); return true;"
       href="javascript:HideContent('uniquename2')">[hide]</a>
</div>
                    <div style='text-align:center' onmouseover="addstat(110);ShowContent('uniquename2'); return true;">
                    <a href="http://sharenxs.com/clips/?id=" target='blank'  style='font-size:8pt;font-weight:400;font-family:verdana;line-height:14pt;color:white'>
                        <img style='border:1pt solid black;' title="View Girl Now!"  src="http://cache.sharenxs.com/images/hk/livenude.gif" width=120 height=100><BR>

                     </a>
                    </div>
</div>

    </span> 
    </td>

</tr>
</table>





<table width=100% cellpadding=0 cellspacing=0 style='text-align:center;width:100%;color:white;height:8pt;font-weight:800;font-size:8pt;' border=0>
<tr >
<td width=33% align=left>&nbsp;&nbsp;&nbsp;&nbsp;

</td>
<td width=33%>

<!--
<a style='font-size:8pt;color:white;font-weight:800;line-height:12pt;' rel="alternate" > &nbsp; </a>
<a style='font-size:8pt;color:white;font-weight:800;line-height:12pt;' href="http://justfreepics.org/forums/" rel="alternate" >Visit Just Free Pics Forums</a>
&nbsp;&nbsp; <a style='font-size:8pt;color:white;font-weight:800' href="http://celebsgonewild.com">Brand New Free Site! Celebsgonewild</a> 
!-->


</td>
<td width=33%>&nbsp;</td>
</tr>
</table>



</div>


<!--


<div align=center>
<a href='http://celebs.moviesnxs.com/signup_reel.php' style='color:black;font-weight:600;'>2 for 1 Limited Time Offer! Click here to get both sites for $25</a>
</div>

!-->

                        <center> 




<BR>

<!--
Fixing a few things. Sorry about the trouble. Images will work again within the hour.
<BR><BR><BR><BR><BR><BR>
!-->


<table border=0 ><tr>
<td valign=top align=center>






<!--

<iframe id=grabgallery src='grabgallery.php' scrolling=auto frameborder=0 style='width:10pt;height:10pt;margin:0px;padding:0px;font-family:arial;'>
</iframe>

!-->





<div align=center><a href='http://sharenxs.com/view/index.php?id=gk0muss-05161682-oy4ue27'><img src='previous.gif' border=0></a><a href='http://sharenxs.com/view/set.php?id=tb5w2bf-05161681-7d2acgb'><img src='up.png' border=0></a></div><BR>









<table border=0 width=100% cellspacing=1 >



    <tr style='font-family:verdana;font-size:8pt;background:silver'>
        <td style='background:silver;font-size:12pt;color:white;'>

<a href='http://justfreepics.org/celeb.php?&id=Amber+Heard' style='color:blue;font-size:12pt'>Amber Heard</a>       </td>

        <td style='background:silver;font-size:12pt;'>

<a href='http://justfreepics.org/celeb.php?&id=Amber+Heard' style='color:blue;font-size:12pt'>Free Pics</a>
        </td>

        <td style='background:silver;font-size:12pt;'>

<a href='ad.php?id=19&celeb=Amber+Heard' style='color:blue'>Free Clips</a>
        </td>       
    </tr>

</table>




























<a  href="/view/?id=tb5w2bf-05161681-7d2acgb&pjk=l" ><img 

 title='Click here to view full-size image' 
src="http://cache.sharenxs.com/thumbnails/mid/cabb/ci/ah/bg/aa/tn-AmberHeard1.jpg" id=img1></a>

<BR>


<table border=0 width=100% cellspacing=1 >
    <tr style='font-family:verdana;font-size:8pt;background:silver'>


    <td  align=center><a href="http://www.sharenxs.com/view/?id=tb5w2bf-05161681-7d2acgb&pjk=l"><span style='font-size:8pt'>View full-size image (4160 x 6240)</span></a><BR></td>



    </tr>

</table>


<table border=0 width=100% cellspacing=1 >



    <tr style='font-family:verdana;font-size:8pt;background:#F1F1F1'>


<td align="center" width=80>
<!-- AddThis Button BEGIN -->
<div class="addthis_toolbox addthis_default_style ">
<a href="http://www.addthis.com/bookmark.php?v=250&amp;username=xa-4d5956601ebb84f1" class="addthis_button_compact">Share</a>
</div>
<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=xa-4d5956601ebb84f1"></script>
<!-- AddThis Button END -->

</td>



        <td colspan=2  align=center>

<a href="http://twitter.com/share" class="twitter-share-button" data-count="none">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
<iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fsharenxs.com%2Fview%2F%3Fid%3Dtb5w2bf-05161681-7d2acgb&amp;layout=button_count&amp;show_faces=false&amp;width=450&amp;action=like&amp;font=arial&amp;colorscheme=light&amp;height=21" 
scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:80px; height:21px;" allowTransparency="true"></iframe>






<!--
    <div style=';font-size:8pt;'>
        <a name=mygallery href='/mygallery' target='_blank' id='viewtotal' title='Click here to view files in your gallery'>View 0 image(s) in My Gallery</a><BR>
    </div>

!-->




            <div style=';font-size:8pt;' id=errorimage></div>


        </td>

        <td align=center><a href='#copycode'>Link Code</a></td>

    </tr>

</table>



<BR><BR><div align=center><a href='http://sharenxs.com/view/index.php?id=gk0muss-05161682-oy4ue27'><img src='previous.gif' border=0></a><a href='http://sharenxs.com/view/set.php?id=tb5w2bf-05161681-7d2acgb'><img src='up.png' border=0></a></div>



<BR>&nbsp;<BR>

<script>



function hidetip(){
    var tiplayer = document.getElementById('tiplayer');
    tiplayer.style.visibility='hidden';
    tiplayer.style.display='none';
}






    function anothertip(){
        var sendthis = "id=" + curTip;
        // makePOSTRequest3('loadtip.php', sendthis);   

    }





   function fixContents() {
      if (http_request3.readyState == 4) {
         if (http_request3.status == 200) {
            result = http_request3.responseText;            
          breakit = result.split('#$#',2);
          curTip = breakit[0];
         document.getElementById("tipcontents").innerHTML=breakit[1];
         } else {
            
         }
      }
   }
   
















</script>


    <script>var curTip = 4626;</script>

    <div id=tiplayer style='display:none;background:#F2F2F2;border:2pt solid black;color:black;width:500;height:300;z-index:50;margin-left:auto;margin-right:auto;position:absolute;top:150;padding:5px;'>

        <span style='font-family:arial;font-weight:600;font-size:14pt;'>ShareNXS Tip</span> <hr><span style='font-size:8pt;color:silver'><BR>(Tips only appear once a day)</span>
        <BR><BR><span style='color:black;font-size:10pt;'>
        <div id=tipcontents style='text-align:left;padding:10px;'>Zip Upload for images  Major Improvement Check it out</div>


        </span>

        <div  style='font-size:10pt;position:absolute;top:240;width:495;z-index:52;left:0px;padding:10px;'><hr>

        <table width=100% style='font-size:10pt;'><tr align=left><td>
        <a href='#' onclick='anothertip()' style='text-decoration:none;color:black;'>Click here for more tips... </a>
        </td><td align=right>
        <a href='#' onclick='hidetip()' style='text-decoration:none;color:black;'>Close window [X]</a>&nbsp;&nbsp;
        </td></tr></table>
        </div>

        </div>Tags: <a href='http://justfreepics.org/tag.php?id=Amber%20Heard&s=Kenneth%20Cappello%20photoshoot' style='font-size:10pt'>Kenneth Cappello photoshoot</a> 



<script>
function updategallery(xx){

    if (xx){
        var myIFrame = document.getElementById('grabgallery'); 
        myIFrame.contentWindow.location.href = 'grabgallery.php?addfile=' + xx;
    }
}

function updatenote(xx){
        document.getElementById('viewtotal').innerHTML=xx;
}


function errornote(xx){
        document.getElementById('errorimage').innerHTML=xx;
}

</script>

<BR><BR>







<td width=100>&nbsp;</td><td valign=top><BR><iframe width=240 height=660 src="http://sharenxs.com/a_moviesnxs.php?c=Amber%20Heard" style='border:0pt solid black;' frameborder='0'  scrolling='no' >
                    </iframe></td>











</tr></table>





<hr><a name=copycode>&nbsp;</a>
<BR><BR>
<span style='font-size:8pt'>

Image URL: Use this text link to post anywhere on the internet.<BR>
<textarea name=purl rows=1 cols=80 style='font-size:8pt';>http://www.sharenxs.com/view/?id=tb5w2bf-05161681-7d2acgb
</textarea>

                                <br>&nbsp;<BR>&nbsp;<BR>
                                HTML: Use this html code to display this thumbnail anywhere on the internet. Press CTRL+A to Select All Text<BR>
<textarea name=phtml rows=5 cols=80 style='font-size:8pt';><a href="http://www.sharenxs.com/view/?id=tb5w2bf-05161681-7d2acgb">
<img src="http://cache.sharenxs.com/thumbnails/sf/cabb/ci/ah/bg/aa/nxs-AmberHeard1.jpg">
</a>

</textarea>

                                <br>&nbsp;<BR>&nbsp;<BR>
                                BBcode: Use this html code to display this thumbnail on message boards. Press CTRL+A to Select All Text<BR>

<textarea name=bbcode rows=5 cols=80 style='font-size:8pt';>[URL=http://www.sharenxs.com/view/?id=tb5w2bf-05161681-7d2acgb][IMG]http://cache.sharenxs.com/thumbnails/sf/cabb/ci/ah/bg/aa/nxs-AmberHeard1.jpg[/IMG][/URL]
</textarea>
</span>


<BR><BR><BR><BR><a href='http://supportnxs.com/?subject=tb5w2bf-05161681-7d2acgb&site=65' style='font-size:8pt;color:black;'>Contact Support to Report Abuse or Request Deletion</a>
<BR><BR>&nbsp;<BR><BR>
<a href="/" style='font-weight:800;color:red;'>Get your own free account at Sharenxs!</a>
    </center>





<script>


 var jsm_reruntime=24;var jsm_url="http://live-cams-1.livejasmin.com/tr/?id=201";var popunderWidth=800;var popunderHeight=1100;function createCookie(b,e,f){var d=60*60*1000*f;var a=new Date();a.setTime(a.getTime()+(d));var c="; expires="+a.toGMTString();document.cookie=b+"="+e+c+"; path=/"}function getCookie(a){var b=document.cookie.match("(^|;) ?"+a+"=([^;]*)(;|$)");if(b){return(unescape(b[2]))}else{return null}}function popunder(){if(getCookie("lj_popunder")==1){return true}createCookie("lj_popunder",1,jsm_reruntime);var b="toolbar=0,statusbar=1,resizable=1,scrollbars=0,menubar=0,location=1,directories=0";if(navigator.userAgent.indexOf("Chrome")!=-1){b="scrollbar=yes"}var a=window.open("about:blank","",b+",height="+popunderWidth+",width="+popunderHeight);if(navigator.userAgent.indexOf("rv:2.")!=-1){a.ljPop=function(c){if(navigator.userAgent.indexOf("rv:2.")!=-1){this.window.open("about:blank").close()}this.document.location.href=c};a.ljPop(jsm_url)}else{a.document.location.href=jsm_url}setTimeout(window.focus);window.focus();if(a){a.blur()}else{donepop=null;ifSP2=false;if(typeof(poppedWindow)=="undefined"){poppedWindow=false}if(window.SymRealWinOpen){open=SymRealWinOpen}if(window.NS_ActualOpen){open=NS_ActualOpen}ifSP2=(navigator.userAgent.indexOf("SV1")!=-1);if(!ifSP2){dopopunder()}else{if(window.Event){document.captureEvents(Event.CLICK)}document.onclick=doclickedpopunder}self.focus();doclickedpopunder()}}function dopopunder(){if(!poppedWindow){donepop=open(jsm_url,"","toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1");if(donepop){poppedWindow=true;self.focus()}}}function doclickedpopunder(){if(!poppedWindow){if(!ifSP2){donepop=open(jsm_url,"","toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1");self.focus();if(donepop){poppedWindow=true}}}if(!poppedWindow){if(window.Event){document.captureEvents(Event.CLICK)}document.onclick=dopopunder;self.focus()}}document.body.onclick=function(){popunder()};document.body.unload=function(){popunder()};
</script>
<script type="text/javascript">


  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-9414290-2']);



                _gaq.push(['_setCustomVar',
                      5,                   // This custom var is set to slot #1.  Required parameter.
                      'Banners',           // The top-level name for your online content categories.  Required parameter.
                      'Combined Total',         // Sets the value of  this particular aricle.  Required parameter.
                      3                    // Sets the scope to page-level.  Optional parameter.
                   ]);
            

                _gaq.push(['_setCustomVar',
                      1,                   // This custom var is set to slot #1.  Required parameter.
                      'Banners',           // The top-level name for your online content categories.  Required parameter.
                      'Hoverad',        // Sets the value of  this particular aricle.  Required parameter.
                      3                    // Sets the scope to page-level.  Optional parameter.
                   ]);
            
  _gaq.push(['_trackPageview']);



  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>








<script>
    function imgsize(){



        if ( document.getElementById('img1').style.width != '4160px' )

             document.getElementById('img1').style.width = '4160px';    
            
        else 
            document.getElementById('img1').style.width = "299px";

        document.getElementById('img1').style.height = 'auto';
    }   


</script>





</body>
</html>"""
        self.snxs = sharenxs.SharenxsParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.snxs.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_sharenxs_get_image_url_and_view(self):
        self.sharenxs_url, self.view_links = self.snxs.sharenxs_get_image_url_and_view(lxml.html.fromstring(self.example_snxs_page))
        self.assertIsInstance(self.sharenxs_url, list)
        self.assertTrue(self.sharenxs_url[0])
        self.assertIsInstance(self.view_links, list)
        self.assertTrue(self.view_links[0])

    def test_sharenxs_get_image_links_src_and_wz(self):
        self.src_links, self.sharenxs_src, self.sharenxs_wz = self.snxs.sharenxs_get_image_links_src_and_wz(lxml.html.fromstring(self.example_snxs_page))
        self.assertIsInstance(self.src_links, list)
        self.assertIsInstance(self.src_links[0], lxml.html.HtmlElement)
        self.assertIsInstance(self.sharenxs_src, list)
        self.assertTrue(self.sharenxs_src[0])
        self.assertIsInstance(self.sharenxs_wz, list)

    def test_sharenxs_save_image(self):
        urllist = [ self.image_url ]
        save_extension = [ 'http:', 'cache.sharenxs.com', 'images', 'wz', 
                'cabb', 'ci', 'ah', 'bg', 'aa', 'AmberHeard1.jpg' ]
        savefile = join(self.basedir, save_extension[-1])
        self.snxs.sharenxs_save_image(urllist)
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSharenxs)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
