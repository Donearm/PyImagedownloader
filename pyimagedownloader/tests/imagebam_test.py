#!/usr/bin/env python2

import unittest
import imagebam
import lxml.html
from os.path import join, getsize, isfile

class TestImagebam(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://www.imagebam.com/image/38af8c140780852'
        self.image_url = 'http://45.imagebam.com/download/pWQfnGAtSfxbP4m7f4Y3bg/14079/140780852/119274167.jpg'
        self.example_ibam_page = """<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">

<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>


<meta name="author" content="ImageBam.com"/>
<meta name="description" content="Free image hosting and photo sharing. Create picture galleries with bulk upload tools and share with family and friends."/>
<meta name="keywords" content="free image hosting, photo sharing, upload photo, free photo gallery, photo host, image gallery"/>

    <meta name="ROBOTS" content="NOINDEX, NOFOLLOW"/>
    <meta name="GOOGLEBOT" content="NOINDEX, NOFOLLOW"/>

    <meta name="GOOGLEBOT" content="NOARCHIVE"/>
    
<title>ImageBam - Fast, Free Image Hosting and Photo Sharing</title>
<style type="text/css">

        body{background-color:#FFF;margin:0px;padding:0px;font-size:12px;color:#564b47;text-align:center;font-family:sans-serif}
                a{text-decoration:underline;color:#000}a:hover{color:#001;text-decoration:underline}
        fieldset{border:1px solid #BBB;margin-bottom:20px;padding:20px;margin-left:20px;margin-right:20px}
        legend{font-size:14px;font-weight:bold;color:#232323;padding-left:8px;padding-right:8px}
        .navthing{margin:7px;padding:3px;border:1px solid #0060CC;font-size:14px;text-decoration:none;background-color:#FFF;margin-bottom:3px;line-height:32px;color:#00235F}
        .navthing:hover{text-decoration:none;background-color:#E3EEFE}
        .header{text-center:left;width:263px;margin-left:5px;margin-top:3px;margin:auto}
        .gallery{border:1px dotted black;width:400px;margin:auto;padding:7px;margin-top:5px;}
                .gallery_desc{margin-top:10px;}
        .sharing{border:1px solid white;width:400px;margin:auto;padding:7px;text-align:left}
        .gallery_title{font-size:125%;font-weight:bold}.cursor{cursor:pointer}
        .buttonblue{background-color:#F7F9FB;border:1px solid #0048C5;  text-decoration:none;color:#0C4EA6; font-size:12px; padding:3px; display:block; float:right; margin-left:1px; margin-right:1px;}
                .buttonblue img{
                    height:16px; width:16px; border:none; vertical-align:middle;
                }

                .buttonblue span{
                    vertical-align:middle;
                }


        .buttonblue:hover{text-decoration:none}

                .buttonblue2{background-color:#F7F9FB;border:1px solid #0048C5;  text-decoration:none;color:#0C4EA6; font-size:12px; padding:3px; display:block; margin-left:1px; margin-right:1px;}
                .buttonblue2 img{
                    height:16px; width:16px; border:none; vertical-align:middle;
                }

                .buttonblue2 span{
                    vertical-align:middle;
                }


        .buttonblue2:hover{text-decoration:none}


        .VkgcaoY{width:900px;border:2px solid #983429;background-color:#F3CCC9;text-align:center;font-size:16px;margin:auto;margin-top:5px;margin-bottom:5px; padding-top:60px; padding-bottom:60px;}

        .abtrand1{display:none;}

                #imageContainer{
                    opacity: 1.00;
                    -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
                    filter: alpha(opacity=100);

                }


                #jwHvGNThkbxgDgyI{
                    background-color: black;
                    opacity: 0.66;
                    width:100%;
                    height:100%;
                    position:absolute;
                    top:0px;
                    left:0px;
                    z-index:6;
                    display:none;
                    -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=66)";
                    filter: alpha(opacity=66);

                 }

                 other item{
                     background-color: black;
                    opacity: 1.00;

                    top:0px;
                    left:0px;
                    z-index:6;
                    display:none;
                    -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
                    filter: alpha(opacity=100);
                 }



                 #FZgAQgycJYGo{
                     z-index:1000;
                     position:absolute;
                     display:none;
                     font-size:18px;
                     width:300px;
                     height:130px;
                     text-align:center;
                     background-color:white;
                     border:5px solid orange;
                     padding:20px;

                 }

                .box_error{
                        background-color:#ffdede;
                        border:1px solid #ab0000;
                        padding:5px;
                        margin:15px;
                }

                .box_info{
                        background-color:#e0ffdb;
                        border:1px solid #117b00;
                        padding:5px;
                        margin:15px;
                }

                .box_wait{
                        background-color:#fffcd2;
                        border:1px solid #e5d800;
                        padding:5px;
                        margin:15px;
                }

                #scaleinfo{
                     width:890px; display:none; margin:auto;  margin-bottom:8px;  
                    /*border:2px solid #A0C397; background-color:#E9E9E9;  font-weight:bold; margin-top:10px; line-height:16px; height:16px; padding:3px;*/
                }


                #top_searches {
    
    position: relative;
    width: 710px;
    margin-top: 52px;
    text-align: left;
}
#top_searches h2 {
    margin: 0px;
    padding: 0px;
    font-size: 16px;
    color: #2b2b2b;
    font-weight: normal;
}
#top_searches p {
    margin: 10px 0px 0px 0px;
    padding: 0px;
    line-height: 23px;
    color: #727171;
    font-size: 13px;
}
#top_searches p a {
    color: #727171;
    text-decoration: underline;
}
#top_searches p a.link_style1 {
    font-weight: bold;
}
#top_searches p a.link_style2 {
    font-weight: bold;
    font-size: 20px;
    color: #ee59b3;
}
#top_searches p a.link_style3 {
    font-weight: bold;
    font-size: 15px;
}

#top_searches p a.link_style4 {
    font-size: 12px;
    color: #868686;
}

#top_searches p a:hover {
    text-decoration: none;
}


</style>






<script type="text/javascript">
    // <![CDATA[
var scaled = false;

function scaleonload(){
    e = document.getElementById('i140780852');
    scale(e);
}

function scale(e){

    var scaleinfo = document.getElementById('scaleinfo');
    var scaleinfoWH = document.getElementById('scaleinfoWH');
    if(scaled){
        e.width=originalWidth;
        e.height=originalHeight;
        scaleinfo.style.display='none';
        scaled=false;
    }else{
        if(e.width>900){
            originalWidth = e.width;
            originalHeight = e.height;
            e.style.cursor = "pointer";
            e.width=900;
            e.height = Math.ceil(900*(originalHeight/originalWidth));
            scaleinfo.style.display='block';
            scaleinfoWH.innerHTML = originalWidth+'x'+originalHeight+'px';
            scaled=true;
        }
    }
}


function closeWin() {
  this.focus();
    self.opener = this;
    self.close();
}
// ]]>
</script>


</head>
<body onload="scaleonload()">
    <div></div>

<div>
        <!-- FANBOY! WATCH YOUR FALSE-POSITIVES.. AT LEAST CHECK THE FUNCTIONALITY ON THE FRONT PAGE -->
    </div><div>
        <!-- FANBOY! WATCH YOUR FALSE-POSITIVES.. AT LEAST CHECK THE FUNCTIONALITY ON THE FRONT PAGE -->
    </div><div>
        <!-- FANBOY! WATCH YOUR FALSE-POSITIVES.. AT LEAST CHECK THE FUNCTIONALITY ON THE FRONT PAGE -->

    </div><div>
        <!-- FANBOY! WATCH YOUR FALSE-POSITIVES.. AT LEAST CHECK THE FUNCTIONALITY ON THE FRONT PAGE -->
    </div><div>
        <!-- FANBOY! WATCH YOUR FALSE-POSITIVES.. AT LEAST CHECK THE FUNCTIONALITY ON THE FRONT PAGE -->
    </div><div>
        <!-- FANBOY! WATCH YOUR FALSE-POSITIVES.. AT LEAST CHECK THE FUNCTIONALITY ON THE FRONT PAGE -->
    </div><div>
        <!-- FANBOY! WATCH YOUR FALSE-POSITIVES.. AT LEAST CHECK THE FUNCTIONALITY ON THE FRONT PAGE -->
    </div>


<div>
    <a href="http://www.imagebam.com" style='position:absolute; top:0px; left:0px; width:152px; height:36px;' title="Free Image Hosting"><img src='http://1.imagebam.com/imagebam_logo_small.gif' alt='free image hosting' class='cursor' style="border:0px;"/></a>
</div>


    <div id="banner_top">
    


<div style=' margin-bottom:6px; margin-top:2px; text-align:center; height:90px;'>

    <div style="width:728px; margin:auto; margin-top:2px; margin-bottom:6px;">

    <script type="text/javascript"  language="JavaScript">
        // <![CDATA[
    <!-- Hide from old browsers
    // Modify to reflect site specifics
    adserver = "http://show.altitudedigitalpartners.com/altitude";
    target = "/site=Imagebam/size=728x90";

    // Cache-busting and viewid values
    random = Math.round(Math.random() * 100000000);
    if (!pageNum) var pageNum = Math.round(Math.random() * 100000000);

    document.write('<scr');
    document.write('ipt src="' + adserver + '/jserver/random=' + random + target + '/viewid=' + pageNum + '">');
    document.write('</scr');
    document.write('ipt>');

    // End Hide -->
    // ]]>
    </script>

    </div>

</div>    </div><!--banner_top-->
    <div id='yFYMcCJ'></div><div id='xOHQAgqOBvvZLSx'></div><div id='zKpsFDPBwE'></div>
    <div id='lMfxjZobJAuT'></div>
    



<div id="TGaYfDrf" style="top: 2px; left: 0px; display: block;">
<div style="display: block;">
<div id="imageContainer" class="imageContainer">
<table cellpadding="0" cellspacing="2" style="margin:auto;">
    <tr>

       <td style="padding-right: 2px; text-align: left; font-size:15px;">
       <a href='http://www.flixya.com/sign-up/' target='_blank' style='color:#0C4EA6;'>Get Paid to Share Photos, Videos &amp; Blogs</a>       </td>
            <td style="text-align: right;">

                <a href='javascript:closeWin();' onclick='closeWin();' class='buttonblue'><img src='http://2.imagebam.com/static/cross.png' alt=""/><span> close page</span></a>
                    
                <a href='http://45.imagebam.com/download/pWQfnGAtSfxbP4m7f4Y3bg/14079/140780852/119274167.jpg' class='buttonblue' style="margin-left:6px;"><img src='http://2.imagebam.com/static/disk.png' alt=""/><span> save image</span></a>


                                        
                        <a class='buttonblue' href='/image/079866140780860'><span>next image </span><img src='http://2.imagebam.com/static/resultset_next.png' alt=''/></a>                   




                    
                    <div style="clear:right;"></div>
            </td>
            </tr>
    <tr>
            <td colspan="2">
            

 
            
                <img id="i140780852" onclick="scale(this);" src="http://45.imagebam.com/download/pWQfnGAtSfxbP4m7f4Y3bg/14079/140780852/119274167.jpg" alt="loading" style="border:1px solid black;"/>
            </td>

    </tr>
</table>
</div>
</div>
</div>

<div id="scaleinfo">
<img src='http://2.imagebam.com/static/magnifier_zoom_in.png' style='vertical-align:middle; border:none;' alt=""/> <!-- height:16px; line-height:16px; -->
Click on the photo to view the original image with <span id="scaleinfoWH"></span>.
</div><!--/scaleinfo-->



<div style="width:630px; margin:auto; margin-top:10px; margin-bottom:10px;">


<table><tr>
        <td style="width:300px; height:250px;">
        <script type="text/javascript">
                    // <![CDATA[

                    <!-- Hide from old browsers
                    // Modify to reflect site specifics
                    adserver = "http://show.altitudedigitalpartners.com/altitude";
                    target = "/site=Imagebam/size=300x250";

                    // Cache-busting and viewid values
                    random = Math.round(Math.random() * 100000000);
                    if (!pageNum) var pageNum = Math.round(Math.random() * 100000000);

                    document.write('<scr');
                    document.write('ipt src="' + adserver + '/jserver/random=' + random + target + '/viewid=' + pageNum + '">');
                    document.write('</scr');
                    document.write('ipt>');

                    // End Hide -->
                // ]]>
                </script>

                </td>
        <td style="width:300px; height:250px; padding-left:30px;">
    
            <script type="text/javascript">
                // <![CDATA[
            <!-- Hide from old browsers
                    // Modify to reflect site specifics
                    adserver = "http://show.altitudedigitalpartners.com/altitude";
                    target = "/site=Imagebam/size=300x250";

                    // Cache-busting and viewid values
                    random = Math.round(Math.random() * 50000000);
                    if (!pageNum) var pageNum = Math.round(Math.random() * 50000000);

                    document.write('<scr');
                    document.write('ipt src="' + adserver + '/jserver/random=' + random + target + '/viewid=' + pageNum + '">');
                    document.write('</scr');
                    document.write('ipt>');

                    // End Hide -->
            // ]]>
            </script>

        </td>

</tr></table>


</div>


<div id="navigation_bottom">
    <a class='navthing' href='/image/079866140780860'>next image <img src='http://2.imagebam.com/static/resultset_next.png' style='height:16px; line-height:16px; vertical-align:middle; border:none;' alt=''/></a></div><!--/navigation_bottom-->




<div class='gallery'><div class='gallery_title'><a href='http://www.imagebam.com/gallery/7jauxf1kj8s0amhtjg8gpgo55cuse0wu/'>Gallery Index</a></div></div><!--/gallery-->    <div style='text-align:center; color:darkgreen; margin:6px;'>Keyboard shortcuts: <b>b</b> back, <b>n</b> next, <b>x</b> close</div><!--/shortcuts-->
    






<div class='sharing' style="margin-top:14px;">
<table style="width:100%">

           <tr><td>
        <form action="" onsubmit="return false;"><div><br/>
            BB-Code<br/><input type='text' style='width:100%;' onclick="this.select();" value='[URL=http://www.imagebam.com/image/38af8c140780852][IMG]http://thumbnails45.imagebam.com/14079/38af8c140780852.jpg[/IMG][/URL] '/><br/><br/>
            HTML-Code<br/><input type='text' id='sharegigya' style='width:100%;' onclick='this.select();' value='<a href="http://www.imagebam.com/image/38af8c140780852" target="_blank"><img src="http://thumbnails45.imagebam.com/14079/38af8c140780852.jpg" alt="imagebam.com"></a>
'/><br/><br/>
            URL only<br/><input type='text' style='width:100%;' onclick='this.select();' value='http://www.imagebam.com/image/38af8c140780852'/>
            </div>
        </form>

        </td></tr>
    </table>

</div><!--/sharing-->




<div style=' width:400px; margin:auto; margin-top:4px; margin-bottom:none; padding:2px;  border:1px solid #00A311; background-color:#CCE8DC; ' onclick="void(0); top.location='http://www.imagebam.com/premium';">

<div style='text-align:center; line-height:16px; vertical-align:middle; font-size:14px;'><a href='/premium' style='line-height: 16px; vertical-align: middle; text-decoration: none;'>I <img src='http://2.imagebam.com/static/heart.png' style='height:16px; line-height:16px; vertical-align:middle; border:none;' alt=""/> ImageBam: Upgrade to Premium (&euro;9.95/year)</a></div></div>

<div style='line-height: 16px; text-align:center; margin:14px;'>
    <a href='/nav/login' style="text-decoration: none; color:#00235F; font-weight: bold;">
    <img src='/img/icons/door_in.png' alt='?' style='vertical-align:middle; line-height:16px; height:16px; border:none;'/>
     Premium Surfer Login
    </a>
</div>


<h1><a href='http://www.imagebam.com' title="free image hosting" style="font-size:12px; font-weight:normal;">Free Image Hosting by ImageBam</a></h1>
<div class="footer" id="footer" style="margin-top:10px;">
    
    <span style="font-size:10px"><a href="http://www.imagebam.com">ImageBam</a> | <a href="/login">login</a> | <a href="/register">register</a> | <a href="http://www.imagebam.com/report-abuse">report abuse</a> | <a href="http://www.imagebam.com/terms-of-service">terms of service</a> </span>

</div>







<script type="text/javascript">



if (document.addEventListener) {
    document.addEventListener('keypress',
    function (evt) {
        // back
                
        // next
                            if(evt.charCode==110) top.location = "http://www.imagebam.com/image/079866140780860";
                        if(evt.charCode==120) self.close();
    },
    false
    );
}




    function getPosition(element){
        var elem=element,tagname="",x=0,y=0;
        while ((typeof(elem)=="object")&&(typeof(elem.tagName)!="undefined")){
            y+=elem.offsetTop;
            tagname=elem.tagName.toUpperCase(); /* tag-Name ermitteln, Grossbuchstaben */

            if (tagname=="BODY")
                elem=0;


            if (typeof(elem)=="object")
                if (typeof(elem.offsetParent)=="object")
                    elem=elem.offsetParent;
        }
        return y;
    }

if(getPosition(document.getElementById('lMfxjZobJAuT'))<=10){
var abt = document.getElementById('lMfxjZobJAuT');
abt.innerHTML = '<div style="width:889px;border:1px solid #F99B05;background-color:#FFEECA;line-height:24px;text-align:center;font-size:16px;margin:auto;margin-top:5px;margin-bottom:5px; padding-top:14px; padding-bottom:14px;">Dear Adblock User: <a href="/premium" style="font-size:18px;">Upgrade to ImageBam Premium</a> to Remove the Ads! (&euro;0.027 / day)</div>';
}

</script>





<br/><br/>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-2424497-2");
pageTracker._trackPageview();
} catch(err) {}</script>


<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-2424497-8");
pageTracker._trackPageview();
} catch(err) {}</script>



</body>
</html>"""
        self.ibam = imagebam.ImagebamParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.ibam.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imagebam_get_image_src_and_name(self):
        self.imagebam_src, self.imagename = self.ibam.imagebam_get_image_src_and_name(lxml.html.fromstring(self.example_ibam_page))
        self.assertIsInstance(self.imagebam_src, list)
        self.assertTrue(self.imagebam_src[0])
        self.assertIsInstance(self.imagename, str)
        self.assertTrue(self.imagename)

    def test_imagebam_save_image(self):
        urllist = []
        urllist.append(self.image_url)
        self.ibam.imagebam_save_image(urllist, 'kate.jpg')
        savefile = join(self.basedir, 'kate.jpg')
        self.assertTrue(isfile(savefile))
        self.assertTrue(getsize(savefile) >= 1000)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImagebam)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
