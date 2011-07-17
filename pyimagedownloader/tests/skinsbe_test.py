#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import skinsbe
import lxml.html

class TestSkinsbe(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://image.skins.be/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/'
        self.example_skin_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:og="http://opengraphprotocol.org/schema/"
    xmlns:fb="http://www.facebook.com/2008/fbml"
    xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <base href="http://image.skins.be/" />
        <link rel="icon shortcut" href="/favicon.ico"/>

                    <title>24797 septimiu29 danicathrall nutsuk 31dec2010 123 (#2831923) | free image hoster: upload.skins.be</title>
            <meta name="description" content="Free image hosting on upload.Skins.be for 24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg" />
            
        <meta name="robots" content="noarchive" />

        <meta name="keywords" content="24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg, image hosting, uploads, wallpaper, pictures, 1246 x 1700" />
        <link rel="canonical" href="http://image.skins.be/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/" />
        
        <meta property="og:title" content="24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg"/>
        <meta property="og:type" content="article"/>
        <meta property="og:url" content="http://image.skins.be/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/"/>
        <meta property="og:image" content="http://13img.skins.be/2/8/3/1/9/2/3/24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg"/>
        <meta property="og:site_name" content="Skins.be"/>
        <meta property="fb:page_id" content="468190645569"/>        
                
        <link rel="stylesheet" href="http://scripts.skins.be/css/image.skins.be/wallpaper.css" />

        <!--[if lte IE 6]>
        <link rel="stylesheet" href="http://scripts.skins.be/css/image.skins.be/ie6.css" />
        <![endif]-->

        <!--[if lte IE 7]>
        <link rel="stylesheet" href="http://scripts.skins.be/css/image.skins.be/ie7.css" />
        <![endif]-->
        
        <!--[if lte IE 6]>
        <script type="text/javascript" src="http://scripts.skins.be/js/skins.be/utilities.js"></script>
        
        <script type="text/javascript">
        <!--
            if ( ( typeof( set_min_width_rs ) ).toLowerCase() != 'undefined' ) { set_min_width_rs( 'wrapper' , 1000 ); }
        //-->
        </script>
        
        <![endif]-->
        
        <!-- TradeDoubler site verification 1654082 -->
                
        <!-- page/group config defined libs -->
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/prototype/1.6.1.0/prototype.js"></script>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/scriptaculous/1.8.3/scriptaculous.js"></script>

        <script type="text/javascript" src="http://scripts.skins.be/js/image.skins.be/conf.inc.js"></script>
        <script type="text/javascript" src="http://scripts.skins.be/js/image.skins.be/main.js"></script>
        <script type="text/javascript" src="http://scripts.skins.be/js/image.skins.be/livesearch.js"></script>
        <script type="text/javascript" src="http://scripts.skins.be/js/image.skins.be/wallpaper_resize.js"></script>
        <!-- end. -->
        
        
        <script type='text/javascript'
        src='http://partner.googleadservices.com/gampad/google_service.js'>
        </script>

        <script type='text/javascript'>
        GS_googleAddAdSenseService("ca-pub-9312530412557851");
        GS_googleEnableAllServices();
        </script>
        <script type='text/javascript'>
        GA_googleAddSlot("ca-pub-9312530412557851", "skins_be_125x125");
        GA_googleAddSlot("ca-pub-9312530412557851", "skins_be_160x250");
        GA_googleAddSlot("ca-pub-9312530412557851", "skins_be_160x600");
        GA_googleAddSlot("ca-pub-9312530412557851", "skins_forum_300x250");
        </script>
        <script type='text/javascript'>
        GA_googleFetchAds();
        </script>
        
        

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-495854-2']);
  _gaq.push(['_setDomainName', '.skins.be']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

    </head>

<body onload="if(top.location != document.location){top.location.href = document.location;} liveSearchInit();">

<div id="wrapper" >
<table border="0" cellspacing="0" cellpadding="0" >
    <tr>
    <td id="headerContent" class="clearfix">
        <div class="logo">
            <a href="http://www.skins.be/"><img src="http://img.skins.be/img/small/logo.jpg" alt="Skins.be - the biggest babe and celebrity wallpaper ressource in the world" /></a>
        </div>
        <div class="iconNav">
            <a href="http://www.skins.be/babes/" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('star','','http://img.skins.be/img/small/icon-star02.jpg',1)"><img src="http://img.skins.be/img/small/icon-star01.jpg" alt="skins.be home" name="star" height="40" border="0" align="middle" /></a>

            <a href="http://forum.skins.be" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Community','','http://img.skins.be/img/small/icon-community02.jpg',1)"><img src="http://img.skins.be/img/small/icon-community01.jpg" alt="skins.be Community" name="Community" height="40" border="0" align="middle" /></a>
            <a href="http://www.skins.be/imagehoster/" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Upload','','http://img.skins.be/img/small/icon-upload02.jpg',1)"><img src="http://img.skins.be/img/small/icon-upload01.jpg" alt="skins.be Imagehoster" name="Upload" height="40" border="0" align="middle" /></a>
                                        <a href="http://www.oleo.tv/" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Lyrics','','http://img.skins.be/img/small/icon-lyrcis02.jpg',1)"><img src="http://img.skins.be/img/small/icon-lyrcis01.jpg" alt="Oleo - Lyrics" name="Lyrics" height="40" border="0" align="middle" /></a>
                <a href="http://blog.skins.be/" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Blog','','http://img.skins.be/img/small/small-icon-blog-alt02.gif',1)"><img src="http://img.skins.be/img/small/small-icon-blog-alt01.gif" alt="Blog" name="Blog" height="40" border="0" align="middle" /></a>
                    </div>
    </td>
</tr>
<tr>
    <td>
        <div class="h_ad" id="aff_rep" align="center">

        <script type='text/javascript'>
        GA_googleFillSlot("skins_forum_300x250");
        </script>
        </div>      
    </td>
</tr>
<tr>
    <td id="content">
        <div class="clear"></div>
        <h1>24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg (1246 x 1700 px / 227 KB) </h1>
        <div id="wallData" class="clearfix">Upload date: December 25, 2010</div>

        <iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fimage.skins.be%2F2831923%2F24797-septimiu29-danicathrall-nutsuk-31dec2010-123%2F&amp;layout=standard&amp;show_faces=true&amp;width=600&amp;action=like&amp;font&amp;colorscheme=light&amp;height=80" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:600px; height:80px;" allowTransparency="true"></iframe>
        
            <div class="sp20"></div>
    <div id="image">
        <div id="adjust_info" style="display: none; padding-bottom: 4px;">
            <em>This image has been scaled down to fit your computer screen. Click on it to show it in the original size.</em>
        </div>

        <img id="wallpaper_image" onclick="adjust_wallpaper();" src="http://13img.skins.be/2/8/3/1/9/2/3/24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg"  alt="24797 septimiu29 danicathrall nutsuk 31dec2010 123" title="24797 septimiu29 danicathrall nutsuk 31dec2010 123" />

        <script type="text/javascript">set_wallpaper_size(1246, 1700); set_wallpaper_width();</script>
    </div>

    <div style="float:left;width:300px;padding:10px;margin: 30px 10px 10px;">       
            
    </div>
    <div style="float:left;width:700px;">
        <div id="imageTags">
                    </div>
    
        <div id="upload_form">

            <h2 class="clear">Get thumbnail</h2>
            
            <div id="image_codes" style="display: none;">
                <form>
                    <fieldset>
                        <legend>Get thumbnail</legend>
                        Thumbnail for websites:<br />
                        <input type="text" onClick="this.select();" class="uploadRes" size="60" value="&lt;a href=&quot;http://image.skins.be/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/&quot; target=&quot;_blank&quot;&gt;&lt;img src=&quot;http://13thumb.skins.be/2/8/3/1/9/2/3/24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg&quot; border=&quot;0&quot; /&gt;&lt;/a&gt;" />

                        <br />
                        Thumbnail for boards type 1<br />
                        <input type="text" onClick="this.select();" class="uploadRes" size="60" value="[URL=http://image.skins.be/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/][IMG]http://13thumb.skins.be/2/8/3/1/9/2/3/24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg[/IMG][/URL]" />
                        <br />
                        Thumbnail for boards type 2<br />
                        <input type="text" onClick="this.select();" class="uploadRes" size="60" value="[url=http://image.skins.be/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/][img=http://13thumb.skins.be/2/8/3/1/9/2/3/24797-septimiu29-danicathrall-nutsuk-31dec2010-123.jpg][/url]" />
                        <br />
                        Direct link to image<br />

                        <input type="text" onClick="this.select();" class="uploadRes" size="60" value="http://image.skins.be/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/" />
                    </fieldset>
                </form>
            </div>
            
            <form>
                <input type="button" value="Image Code" class="submitButton" onclick="toggle_up_down('image_codes');" />
            </form>
    
            <div class="sp18"></div>
            <h2 class="clear">Upload an image</h2>

            
            <form action="http://upload.skins.be/" enctype="multipart/form-data" method="post" target="_blank" onsubmit="return tagSearchSubmit('tag');">
        
                <fieldset class="blueBGfox">
    
                <legend >Choose images to upload</legend>
                <div class="blueBGie" >
                jpg - png - gif - zip<br /> maximum filesize: 5MB per image and 25MB per zip file<br /><br />
                    <input class="file_input" name="upload[]" type="file" size="50" maxlength="1024000" />
                </div>

            </fieldset>
    
            <fieldset>
                <legend>Add tags</legend>
            <label for="tag">Add some tags to categorise your upload </label><br />
                <input type="text" id="tag" name="tag" value="" onkeypress="liveSearchStart('tag');" /><br />
                <div id="tagsearch_LSResult" ><div id="tagsearch_LSShadow"></div></div>
            </fieldset>
            <input type="submit" name="submit" value="Upload" class="submitButton" />

            </form> 
            <div class="sp18"></div>
            <a href="http://upload.skins.be/"><b>Use our complete upload-form for more options</b></a>  
            <br /><br />
        </div>
    </div>

    </td>
</tr>
<tr>
    <td id="footer" >

        <div id="fLink">
<ul id="footerLinks" class="clearit">
    <li class="first">
        <dl>
            <dt>Pages</dt>
            <dd><a href="http://www.skins.be/babes/">Babes</a></dd>
            <dd><a href="http://www.skins.be/top-tags/">Tags</a></dd>
            <dd><a href="http://www.skins.be/botw/">Babes of the week</a></dd>

            <dd><a href="http://www.skins.be/suggest-babe/">Suggest a babe</a></dd>
            <dd><a href="http://www.skins.be/imagehoster/">User uploads</a></dd>
            <dd><a href="http://www.skins.be/poll/">Polls</a></dd>
            <dd>
                <a href="http://promi.skins.be/">
                    Promiblog
                </a>
                (de)
            </dd>

        </dl>
    </li>
    <li>
        <dl>
            <dt>Chart</dt>
            <dd><a href="http://www.skins.be/babe-chart/">Highest rated babe</a></dd>
            <dd><a href="http://www.skins.be/wallpaper-chart/">Highest rated wallpaper</a></dd>

            <dd><a href="http://www.skins.be/notification-chart/">Notification charts</a></dd>
            <dd><a href="http://www.skins.be/current-chart/">Current charts</a></dd>
            <dd><a href="http://www.skins.be/todays-favorites/">Today's charts</a></dd>
            <dd><a href="http://www.skins.be/hall-of-fame/">Hall of fame</a></dd>
        </dl>
    </li>
    <li>

        <dl>
            <dt>Community</dt>
            <dd><a href="http://forum.skins.be/">Forum</a></dd>
            <dd><a href="http://blog.skins.be/">Blog</a></dd>
            <dd><a href="http://www.skins.be/aboutus/">About us</a></dd>
        </dl>
    </li>

        <li>
        <dl>
            <dt>Login</dt>
            <dd><a href="http://www.skins.be/members/functions/">Why register?</a></dd>
            <dd><a href="http://www.skins.be/members/register/">Register</a></dd>
            <dd><a href="http://www.skins.be/members/login/">Log in</a></dd>
        </dl>

    </li>
        <li>
        <dl>
            <dt>Help</dt>
            <dd><a href="http://www.skins.be/help/">FAQ</a></dd>
            <dd><a href="http://www.skins.be/contact/">Contact</a></dd>
                    </dl>

    </li>
    <li>
        <dl>
            <dt>Upload</dt>
            <dd><a href="http://upload.skins.be/">Upload Images</a></dd>
        </dl>
        
        <dl class="second_row">
            <dt>Service</dt>

            <dd><a href="http://www.skins.be/toolbar/">Toolbar</a></dd>
            <dd><a href="http://www.skins.be/recommend/">Recommend</a></dd>
            <dd><a href="http://www.skins.be/webmaster/">Webmasters</a></dd>
            <dd><a href="http://www.skins.be/linksharing/">Linksharing</a></dd>
        </dl>
    </li>
</ul>

</div>

<div id="footerSP">
    <ul class="fSP">
        <li class="bold">Languages</li>
        <li>&nbsp;</li>
        <li><a href="/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/" onclick="set_language('en')">english</a></li>
        <li><a href="/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/" onclick="set_language('de')">deutsch</a></li>
        <li><a href="/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/" onclick="set_language('es')">espa&ntilde;ol</a></li>

        <li><a href="/2831923/24797-septimiu29-danicathrall-nutsuk-31dec2010-123/" onclick="set_language('nl')">nederlands</a></li>
    </ul>
</div>  </td>
</tr>
</table>
</div>

        
<script id="smimad" src="http://cdn.nsimg.net/shared/js/im/im.js?sk=streamate.com&flip=0" type="text/javascript" charset="utf-8"></script>

<!-- BEGIN ADCODE BLOCK -->
<script type="text/javascript">
(function(s,o,l,v,e,d){if(s[o]==null&&s[l+e]){s[o]="loading";s[l+e](d,l=function(){s[o]="complete";s[v+e](d,l,!1)},!1)}})(document,"readyState","add","remove","EventListener","DOMContentLoaded");
(function() {
                var rts = document.createElement('script'); rts.type = 'text/javascript'; rts.async = true;
                rts.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'streamate.doublepimp.com/Publishers/616be13126.js?ver=async&random=' + Math.floor(89999999*Math.random()+10000000) + '&millis='+new Date().getTime();
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(rts, s);
})();

</script>
<!-- END ADCODE BLOCK -->


<script type="text/javascript">ggv2id='bf9e6bea';</script>
<script type="text/javascript" src="http://g2.gumgum.com/javascripts/ggv2.js"></script>
</body>
</html>"""
        self.skin = skinsbe.SkinsbeParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.skin.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_skinsbe_get_image_src(self):
        self.skinsbe_src = self.skin.skinsbe_get_image_src(lxml.html.fromstring(self.example_skin_page))
        self.assertIsInstance(self.skinsbe_src, list)
        self.assertTrue(self.skinsbe_src[0])

    def test_skinsbe_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSkinsbe)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
