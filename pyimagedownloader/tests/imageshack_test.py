#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import imageshack
import lxml.html

class TestImageshack(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.url = 'http://imageshack.us/photo/my-images/140/0299wg.jpg/'
        self.example_ishack_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:fb="http://www.facebook.com/2008/fbml">
<head>
<meta http-equiv="X-UA-Compatible" content="EmulateIE7"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>ImageShack&#174; - Online Photo and Video Hosting</title>
<meta name="copyright" content="Copyright 2010 ImageShack"/>
<meta name="google-site-verification" content="gFE6jG6VX-EGA3a-RV5ICuiGS5o3Xxnec4cgcmy8WPM" />


<meta name="medium" content="image"/>
<meta name="title" content="0299wg.jpg" />
<meta name="description" content="ImageShack offers image hosting, free photo sharing and video sharing. Upload your photos, host your videos, and share them with friends and family. ImageShack, share photos, pictures, free image hosting, free video hosting, image hosting, video hosting, photo image hosting site, video hosting site" />
<meta name="summary" content="Image with 0299wg.jpg" />
<meta name="revisit-after" content="1 days">
<meta name="keywords" content="ImageShack, share photos, pictures, free image hosting, free video hosting, image hosting, video hosting, photo image hosting site, video hosting site"/>

<meta name="robots" content="index,follow">
<meta property="og:title" content="http://imageshack.us/photo/my-images/140/0299wg.jpg/" />
<meta property="og:image" content="http://img140.imageshack.us/img140/4854/0299wg.jpg" />
<meta property="fb:admins" content="213637" />
<meta property="og:type" content="activity" />
<meta property="og:site_name" content="ImageShack" /> 
<meta property="og:url" content="http://imageshack.us/photo/my-images/140/0299wg.jpg/" />
<meta property="fb:app_id" content="124304810915979" />
<link rel="image_src" href="http://img140.imageshack.us/img140/4854/0299wg.jpg" />
<link rel="target_url" href="http://imageshack.us/photo/my-images/140/0299wg.jpg//"/>


<link href="http://crackle.imageshack.us/css/blue_round.css" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" type="text/css" href="http://crackle.imageshack.us/locale/en/locale.css"/>
<link rel="stylesheet" type="text/css" href="http://crackle.imageshack.us/css/lp.css"/>


<link type="application/rss+xml" href="http:////4854/0299wg.jpg.comments.xml" title="RSS" rel="alternate"/>




<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />

<!-- PUT THIS TAG IN THE head SECTION -->
<script type="text/javascript" src="http://partner.googleadservices.com/gampad/google_service.js">
</script>
<script type="text/javascript">
    GS_googleAddAdSenseService("ca-pub-7137941865592088");
    GS_googleEnableAllServices();
</script>
<script type="text/javascript">

                GA_googleAddAttr("category", "unmod");
    
    // Quantcast Segment API 
    function qc_results(result) {
      for (var i=0; i < result.segments.length; i++) {
        GA_googleAddAttr('qctargeting', result.segments[i].id); 
      }
    }
    
            GA_googleAddSlot("ca-pub-7137941865592088", "Imageshack_Landing_Pops");
        
    
</script>

<script type="text/javascript">
    GA_googleFetchAds();
</script>

<!-- END OF TAG FOR head SECTION -->

<script type="text/javascript" src="http://pixel.quantserve.com/api/segments.json?a=p-65DrxcUXjcWq6&callback=qc_results"></script>
</head>

<body >
<!-- Start Google Analytics -->
<script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
    var pageTracker = _gat._getTracker("UA-6232220-1");
    pageTracker._setDomainName(".imageshack.us");
    pageTracker._setSampleRate("80");
    _gaq.push(['b._setAccount', 'UA-6232220-1']);
    _gaq.push(['b._setDomainName', '.imageshack.us']);


    pageTracker._setCustomVar(1, 'page_type', 'landingpage', 3);
        


    pageTracker._trackEvent('page-speed', 'landingpage', '0.15');

    } catch(err) {}
    
// trackPageview
    pageTracker._trackPageview("/landingpage");
            pageTracker._trackEvent('moderation_tracking', 'unmoderated_page_view');
        
    if( navigator.userAgent.indexOf("iPad") == -1 && 
        (document.referrer.indexOf('google.com') != -1 || 
         document.referrer.indexOf('bing.com') != -1 || 
         document.referrer.indexOf('linkbucks.com') != -1) ) { // break search engine display
        var param = (document.referrer.indexOf('linkbucks.com') != -1) ? 'sr=0' : 'sr=1';
        window.top.location.href = ((location.href.indexOf('?') != -1) ? location.href + '&' + param : location.href + param);
    }

    
</script>
<!-- End Google Analytics -->


<div class="layout">
    <div class="indent">

    <div id="top">       
         <div class="top_form right">
                        <div id="signOut" class="signOut">
               <a href="http://register.imageshack.us/" onClick="pageTracker._trackEvent('new-header-click','header-register');">Sign Up</a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;<a href="javascript:;" id="btnlogin" onClick="pageTracker._trackEvent('new-header-click','header-signin');">Login</a>  
            </div>            
            <!-- Search -->            
            <div class="search-box right" style="cursor:nohand; background:transparent;">
                <form id="searchform" >
                  <div class="left">

                                        <input name="q" id="searchfield" style="height:18px; padding-top:3px; font-family:Verdana,Arial,sans-serif; font-size:12px;" 
                     
                      onfocus="focussearch(this, 'Search'); pageTracker._trackEvent('new-header-click','header-search');" value="Search"
                     />&nbsp;&nbsp;
                  </div>
                  <div class="left" style="margin-top: 4px">
                    <a id="searchbutton" href="#" style="margin:0; padding:0; border:none;" onClick="pageTracker._trackEvent('new-header-click','header-search-btn');">
                    <img src="http://crackle.imageshack.us/images/blue/arrow-right-round.gif" width="21px" height="20px" /></a>
                  </div>
                 </form>
            </div>     
         </div>

         <div class="logo"><h1><a href="http://imageshack.us/" onClick="pageTracker._trackEvent('new-header-click','header-logo');">ImageShack</a></h1></div>      
         <div class="clear"></div>         
     </div>
<!-- Main Menu  -->
<div id="menu">
    <ul class="sf-menu">
        <li class=""><a class="topanchor" href="http://imageshack.us/">Media Upload</a></li>                                                             
        <!--<li style="width:329px; cursor:nohand; background:transparent;">
        </li>-->        
        <li id="menu_signupgrade" style="width:251px;"
            class="">
                    <a class="topanchor" href="http://register.imageshack.us/" onClick="pageTracker._trackEvent('new-header-click','header-menu-register');">Sign Up</a>

                  </li>                                                             
        <li class=""><a class="topanchor" href="http://imageshack.us/content.php?page=features" onClick="pageTracker._trackEvent('new-header-click','header-menu-tools');">Tools</a></li>                                                             
        <li id="menu_myimages" class="">
                              <a class="topanchor" href="http://my.imageshack.us/v_images.php" onClick="pageTracker._trackEvent('new-header-click','header-menu-myimages');"
                style="border-right:none" 
                 
                >My Images</a>
                             
                     </li>                                                          
    </ul>
</div>      

<div class="clear"></div>

<div id="ad_top" style="float:left;width:100%;text-align:center;margin-bottom:10px;">
  
  <script type="text/javascript">
  <!--
   if(window.location.hash !=''){
    window.location ='http://'+ window.location.host +  window.location.pathname;
   }
  //--></script>

  
      <iframe id="is_landing_top" rel="Imageshack_Landing_Top" marginwidth="0" marginheight="0" cellspacing="0" cellpadding="0" src="" width="728px" height="90px" style="display:; width:728px; height:90px; margin:10px auto" scrolling="no" frameborder="no"></iframe>
  </div>

<div class="clear"></div>

 <div class="column-left">

   
<!-- Actions Info Div -->
         <div class="action-div">
            <div id="action-share">

            </div>
        </div>   

<!-- Breadcrumbs  -->    
        <!-- Main Image  -->     
        <div id="main_image_frame" align="center">
                                                  <img id="main_image" onClick="pageTracker._trackEvent('fullimg-lp','fullimg-zoom-image-click');" class="border" src="http://img140.imageshack.us/img140/4854/0299wg.jpg" alt="" title="" style="width:318px;height:450px;cursor:pointer;"/>
                                    </div>



    <!-- tool bar-->
    <div style="float:left;width:660px;margin:5px 5px;"> 
    </div>

    <!-- end tool bar-->

    <!-- info bar-->
    <div> 
    <!-- info side-->
            <div class="new-generalinfo new-info" style="border: 1px #cccccc solid;">
          <div class="new-generalinfo-view">                <div class="report-abuse"><a onmouseover="document.getElementById('red_flag').src='http://crackle.imageshack.us/images/red_flag.png';"
                       onmouseout="document.getElementById('red_flag').src='http://crackle.imageshack.us/images/grey_flag.png';"
                       class="last"  style="margin-bottom: -1px;"
                           onclick="pageTracker._trackEvent('new-blue-click','abuse_icon_click');"
                           href="#" id="abusebox-btn" ><img id="red_flag"  src="http://crackle.imageshack.us/images/grey_flag.png" alt="Report Abuse" style="margin-bottom:-1px" /> Report Abuse</a>
                    </div>

          </div>
          <div class="new-generalinfo-view">Views: <span style="font-weight:normal">3</span></div>
    
            <div class="new-generalinfo-view">
                <div style="float:left;">Ratings: </div>
            <div id="rating" style="float:left;margin-top:-15px;" class="rating-width">
                <ul class="star-rating" onClick="pageTracker._trackEvent('new-blue-click','rate_click');" >
                <li class="current-rating" id="current-rating" style="width:0px;"></li>

                                <li><div class="rate1">1</div></li>
                <li><div class="rate2">2</div></li>
                <li><div class="rate3">3</div></li>
                <li><div class="rate4">4</div></li>
                <li><div class="rate5">5</div></li>
                <li><div class="rate6">6</div></li>

                <li><div class="rate7">7</div></li>
                <li><div class="rate8">8</div></li>
                <li><div class="rate9">9</div></li>
                <li><div class="rate10">10</div></li>
                                </ul>
                <div class="rating-message lp-rating-msg">0 ratings</div>

            </div>
          </div>
    
      </div>
          <!-- end info side-->
    <!-- Share section-->
      <div class="new-info" style="float:right;height:76px;width:332px;background-color:#FFFFFF;border: 1px #cccccc solid; _overflow:hidden;">
        <div style="margin-left:10px;margin-top:8px;color:#424242;width:100%;"><b>Share:</b>
        <span style="font-size:11px" class="lp-more"><a href="javascript:;" class="act_share" onClick="pageTracker._trackEvent('new-blue-click','landingpage-share-more_icon_click');" title="Share">More&gt;&gt;</a></span></div>

        <div id="Actions" style="margin-left:10px;margin-top:15px;color:#424242;width:100%;_display:inline">
    <!--
        <img style="float:left;margin-top:1px;" src="http://crackle.imageshack.us/images/myspace.png" />
    -->
        <script type="text/javascript">
        
        function GetThis(T, C, U, L)
        {
                var targetUrl = 'http://www.myspace.com/index.cfm?fuseaction=postto&' + 't=' + encodeURIComponent(T)
                + '&c=' + encodeURIComponent(C) + '&u=' + encodeURIComponent(U) + '&l=' + L;
                window.open(targetUrl);
        }
        function getTwitter(u) {
              window.open('http://twitter.com/home?status='+encodeURIComponent(u),'sharer','toolbar=0,status=0,width=850,height=400,scrollbars=no,resizable=no');
        }
        </script>
        
          
            <a onClick="pageTracker._trackEvent('new-blue-click','landingpage-share-myspace_click');" href="javascript:GetThis('ImageShack Posting','0299wg'+'\n'+'Hosted by ImageShack' ,'http%3A%2F%2Fimageshack.us%2Fphoto%2Fmy-images%2F140%2F0299wg.jpg%2F','1')">
                  <img title="Post To Myspace" style="float:left;margin-top:0px;" src="http://crackle.imageshack.us/images/blue/icon_myspace.png" border="0" alt="Post To MySpace!" />
            </a>
    
            <span onClick="pageTracker._trackEvent('new-blue-click','landingpage-share-facebook_icon_click');"><div style="float:left;margin-left:23px;padding:0px;"><script>function fbs_share() {u=location.href;t=document.title;window.open('http://www.facebook.com/share.php?u='+encodeURIComponent(u)+'&t='+encodeURIComponent(t),'sharer','toolbar=0,status=0,width=626,height=436');return false;}</script><div style="padding:0px"><a href="#" onclick="return fbs_share()" target="_blank"><img title="Post to Facebook" src="http://crackle.imageshack.us/images/blue/icon_facebook.png" /></a></div></div></span>
            <span style="float:left; margin-left:23px;">

              <a Title="Post to Digg" href="http://digg.com/submit?url=http%3A%2F%2Fimageshack.us%2Fphoto%2Fmy-images%2F140%2F0299wg.jpg%2F&amp;media=image" target=_blank onClick="pageTracker._trackEvent('new-blue-click','landingpage-share-digg_icon_click');" >
              <img style="" src="http://crackle.imageshack.us/images/blue/icon_digg.png" />
              </a>
            </span> 
          
            <span style="float:left; margin-left:23px;">
                <a href="javascript:getTwitter('http://imageshack.us/photo/my-images/140/0299wg.jpg/')" onClick="pageTracker._trackEvent('new-blue-click','landingpage-share-tweet_icon_click');">
                  <img title="Post to Twitter" src="http://crackle.imageshack.us/images/blue/icon_twitter.png" />    
                </a>
            </span> 
          
            <span style="float:left; margin-left:23px;">

                <a href="http://www.reddit.com/submit?url=http%3A%2F%2Fimageshack.us%2Fphoto%2Fmy-images%2F140%2F0299wg.jpg%2F" onClick="pageTracker._trackEvent('new-blue-click','landingpage-share-reddit_icon_click');"  target="_blank">
                  <img title="Post to Reddit" src="http://crackle.imageshack.us/images/blue/icon_reddit.png" />    
                </a>
            </span> 
            <span style="float:left;margin-left:22px; height:32px; width:32px;">
                <a href="javascript:;" class="act_emailthis" onClick="pageTracker._trackEvent('new-blue-click','landingpage-share-email_icon_click');">
                    <img title="Send as Email" src="http://crackle.imageshack.us/images/blue/icon_mail.png" />
                </a>
            </span> 
        </div>  
      </div>

    <!-- end share -->
      
    </div>
    <!-- end info bar-->

    
    <div class="clear"></div> 

<!-- Related Images -->              
        
        <div style="padding-left:10px;padding-top:10px" id="fbcomments">
          <input type="hidden" id="yfrogid" value="3w0299wgj" />
          <script src="http://static.ak.connect.facebook.com/connect.php/en_US" type="text/javascript"></script>
        </div>    
        </div>

<div class="column-right">
    
      <div id="ad1" align="center" style="margin-left:2px;">
        <!-- PUT THIS TAG IN DESIRED LOCATION OF SLOT Imageshack_Landing  -->
                                <iframe id="is_landing" rel="Imageshack_Landing" marginwidth="0" marginheight="0" cellspacing="0" cellpadding="0" src="" width="300px" height="250px" style="display:none; width:300px; height:250px;" scrolling="no" frameborder="no"></iframe>
                          <!-- END OF TAG FOR SLOT Imageshack_Landing  -->
      </div>
      <div style="height:7px;"></div> <!-- spaces -->

<!-- Images Info - Accordion -->       
       <div id="image-info-links" class="image-info">

            <div id="ImageCodesHeader" class="image-info-tab non-active" state="1">
                <h2>Links to share this image <a href="#" class="tt" style="cursor:help"><img src="/images/blue/help.gif" width="17" height="16" style="vertical-align:middle"/><span class="left-tooltip"><span class="left-top"></span><span class="middle">ImageShack generates automatic image links and code for your images.  Using this code, you can link to your files in a number of ways.  You can embed your files into web pages or show them to friends via email and Instant messenger.<br /><br />In order to use these links or codes, click anywhere inside the code-box, then press CTRL+C to copy the linking code. The linking code now exists inside your computer's "clipboard" and can be pasted anywhere.  Now, you can open your target location (such as a messenger window or a message board post box) and paste your link or code there.<br /><br />"Link" is the Imageshack landing page for images and is great for sharing via Email and IM."Direct" is the actual location of the image on ImageShack's servers."Short" (yfrog only for now...) is a link shortened via the bit.ly URL redirection service.</span><span class="bottom"></span></span></a>
</h2>
            </div>
            <div id="ImageCodes" class="image-info-view"  style="display:none">
                <div class="codes">

                    <div>
                        <label>Link</label><input onClick="pageTracker._trackEvent('new-blue-click','short_click');"  readonly="readonly" class="readonly" value="http://imageshack.us/photo/my-images/140/0299wg.jpg/"/>
                    </div>
                                        <div>
                        <label><a href="#" class="tt" style="cursor:default;">Direct Link<span class="left-tooltip" style="top:8px; cursor:default; left:-210px;"><span class="left-top"></span><span class="middle"><div style="cursor:default;">&nbsp;&nbsp; Please <span id="signin" style="color:#003399;cursor:pointer;display:inline;text-decoration:underline;">Sign in</span> or <span id="signup" style="color:#003399;cursor:pointer;display:inline;text-decoration:underline;">Sign up</span> to get this link.</div></span><span class="bottom" style="padding-bottom:22px"></span></span></a></label>

                        <a href="#" class="tt" style="cursor:default"><input wrap="off" disabled="disabled" onmousedown="return false;" onselectstart="return false;" onClick="return false;" onDoubleClick="return false;" readonly="readonly" class="readonly" value="http://img140.imageshack.us/img140/4854/0299wg.jpg" /><span class="left-tooltip" style="top:8px; cursor:default; left:-100px;"><span class="left-top"></span><span class="middle"><div style="cursor:default;">&nbsp;&nbsp; Please <span id="signin" style="color:#003399;cursor:pointer;display:inline;text-decoration:underline;">Sign in</span> or <span id="signup" style="color:#003399;cursor:pointer;display:inline;text-decoration:underline;">Sign up</span> to get this link.</div></span><span class="bottom" style="padding-bottom:22px"></span></span></a>
                    </div>
                          </div>
                <div class="clear"></div>
            </div>



            <div id="LinkCodesHeader" class="image-info-tab non-active" state="2">
                <h2>Embed this image <a href="#" class="tt" style="cursor:help"><img src="/images/blue/help.gif" width="17" height="16" style="vertical-align:middle"/><span class="left-tooltip"><span class="left-top"></span><span class="middle">"Forum" allows you to hotlink your original uploaded image on BBcode-compatible message boards and forums.<br />"Alt Forum" If your image does not show up after submitting your post, please use "Alt Forum". This occurs because some message boards use different BBcode and are not compatible.<br />"HTML" allows you to hotlink your original uploaded image on HTML-compatible websites, e.g., livejournal, blogger, etc.</span><span class="bottom"></span></span></a>
</h2>
            </div>
            <div id="LinkCodes" class="image-info-view"  style="display:none">
                <div class="codes">

                                                            <div>
                        <label><a href="#" onClick="pageTracker._trackEvent('new-blue-click','link-widget-click');" rel="overlay">Widget</a> <a href="#" class="tt" style="cursor:help"><img src="/images/blue/help.gif" width="17" height="16" style="vertical-align:middle"/><span class="left-tooltip"><span class="left-top"></span><span class="middle">Contains Javascript.&nbsp;&nbsp;&nbsp;Does not work on forums.</span><span class="bottom"></span></span></a>
</label><input readonly="readonly" class="readonly" onClick="pageTracker._trackEvent('new-blue-click','shareable_link_click');" value="&lt;script src=&#039;http://imageshack.us/shareable/?i=0299wg.jpg&amp;s=140&#039; type=&#039;text/javascript&#039;&gt;&lt;/script&gt;&lt;noscript&gt;[URL=http://imageshack.us/photo/my-images/140/0299wg.jpg/][IMG]http://img140.imageshack.us/img140/4854/0299wg.jpg[/IMG][/URL]&lt;/noscript&gt;"/>
                    </div>
                                        <div>
                        <label>Forum</label>
                        <textarea wrap=off onClick="pageTracker._trackEvent('new-blue-click','forum_link_click');" readonly="readonly" class="readonly multilinebox">[URL=http://imageshack.us/photo/my-images/140/0299wg.jpg/][IMG]http://img140.imageshack.us/img140/4854/0299wg.jpg[/IMG][/URL]

Uploaded with [URL=http://imageshack.us]ImageShack.us[/URL]</textarea>

                    </div>
                    <div>
                        <label>Alt Forum</label>
                        <textarea wrap=off onClick="pageTracker._trackEvent('new-blue-click','alt_forum_link_click');" readonly="readonly" class="readonly multilinebox">[URL=http://imageshack.us/photo/my-images/140/0299wg.jpg/][IMG=http://img140.imageshack.us/img140/4854/0299wg.jpg][/IMG][/URL]

Uploaded with [URL=http://imageshack.us]ImageShack.us[/URL]</textarea>
                    </div>
                    
                    <div>
                        <label>HTML</label>

                        <textarea wrap=off onClick="pageTracker._trackEvent('new-blue-click','html_link_click');" readonly="readonly" class="readonly multilinebox">&lt;a target=&#039;_blank&#039; title=&#039;ImageShack - Image And Video Hosting&#039; href=&#039;http://imageshack.us/photo/my-images/140/0299wg.jpg/&#039;&gt;&lt;img src=&#039;http://img140.imageshack.us/img140/4854/0299wg.jpg&#039; border=&#039;0&#039;/&gt;&lt;/a&gt;

Uploaded with &lt;a target=&#039;_blank&#039; href=&#039;http://imageshack.us&#039;&gt;ImageShack.us&lt;/a&gt;</textarea>
                    </div>
                </div>
                <div class="clear"></div>
            </div>


                        <div id="ThumbCodesHeader" class="image-info-tab non-active" state="3">
                <h2>Embed thumbnails of this image <a href="#" class="tt" style="cursor:help"><img src="/images/blue/help.gif" width="17" height="16" style="vertical-align:middle"/><span class="left-tooltip"><span class="left-top"></span><span class="middle">"Forum" allows you to hotlink clickable thumbnails on BBcode-compatible message boards and forums.<br />"Alt Forum" If your image does not show up after submitting your post, please use "Alt Forum". This occurs because some message boards use different BBcode and are not compatible.<br />"HTML" allows you to hotlink clickable thumbnails on HTML-compatible websites, e.g., livejournal, blogger, etc.</span><span class="bottom"></span></span></a>

</h2>
            </div>
            <div id="ThumbCodes" class="image-info-view"  style="display:none">
                <div class="codes">
                    <div>
                        <label>Forum</label>
                        <textarea wrap=off onClick="pageTracker._trackEvent('new-blue-click','thumb_forum_click');" readonly="readonly" class="readonly multilinebox">[URL=http://imageshack.us/photo/my-images/140/0299wg.jpg/][IMG]http://img140.imageshack.us/img140/4854/0299wg.th.jpg[/IMG][/URL]

Uploaded with [URL=http://imageshack.us]ImageShack.us[/URL]</textarea>
                    </div>

                    <div>
                        <label>Alt Forum</label>
                        <textarea wrap=off onClick="pageTracker._trackEvent('new-blue-click','thumb_alt_click');" readonly="readonly" class="readonly multilinebox">[URL=http://imageshack.us/photo/my-images/140/0299wg.jpg/][IMG=http://img140.imageshack.us/img140/4854/0299wg.th.jpg][/IMG][/URL]

Uploaded with [URL=http://imageshack.us]ImageShack.us[/URL]</textarea>
                    </div>
                    <div>
                        <label>HTML</label>
                        <textarea wrap=off onClick="pageTracker._trackEvent('new-blue-click','thumb_html_click');" readonly="readonly" class="readonly multilinebox">&lt;a target=&#039;_blank&#039; href=&#039;http://imageshack.us/photo/my-images/140/0299wg.jpg/&#039;&gt;&lt;img src=&#039;http://img140.imageshack.us/img140/4854/0299wg.th.jpg&#039; border=&#039;0&#039;/&gt;&lt;/a&gt;

Uploaded with &lt;a target=&#039;_blank&#039; href=&#039;http://imageshack.us&#039;&gt;ImageShack.us&lt;/a&gt;</textarea>

                    </div>
                </div>
                <div class="clear"></div>
            </div>
            

                        <div id="GeneralInfoHeader" class="image-info-tab non-active" state="4">
                <h2>Image Details</h2>
            </div>
            
            <div id="GeneralInfo" class="image-info-view" style="display:none">

                <table cellspacing=0 cellpadding=0 border=0>
                                <tr><td>Filename:</td><td class="image-details-value">0299wg.jpg</td></tr>
                                    <tr><td>Size:</td><td class="image-details-value">45Kb</td></tr>
                    <tr><td>Resolution:</td><td class="image-details-value">318 x 450</td></tr>
                                    
                
                                </table>                            

                <p style="line-height:16px">

                </p>    
            </div>

            

                              
                   </div>
         
            <div id="ad2" align="center" style="margin:5px 0 0 2px;">
        <!-- PUT THIS TAG IN DESIRED LOCATION OF SLOT Imageshack_Landing  -->
        <iframe id="is_landing_sidebottom" rel="Imageshack_Landing_SideBottom" marginwidth="0" marginheight="0" cellspacing="0" cellpadding="0" src="" width="300px" height="250px" style="display:none; width:300px; height:250px;" scrolling="no" frameborder="no"></iframe>
        <!-- END OF TAG FOR SLOT Imageshack_Landing  -->
      </div>

            <div style="height:7px;"></div> <!-- spaces -->

             <div class="ads">
                   </div> 
      </div> <!-- end of div.column-right -->
       
       
       
<textarea id="postcontent" style="display:none" rows="0" cols="0">&lt;a href=&quot;http://img140.imageshack.us/my.php?image=0299wg.jpg&quot; target=&quot;_blank&quot;&gt;&lt;img src=&quot;http://img140.imageshack.us/img140/4854/0299wg.th.jpg&quot; border=&quot;0&quot; alt=&quot;Free Image Hosting at www.ImageShack.us&quot;&gt;&lt;/a&gt;&lt;br/&gt;&lt;br/&gt;
&lt;a href=&quot;http://imageshack.us&quot;&gt;
    &lt;img src=&quot;http://crackle.imageshack.us/img/is4.gif&quot; border=&quot;0&quot; alt=&quot;&quot;/&gt;
&lt;/a&gt; 
&lt;a href=&quot;http://img604.imageshack.us/content.php?page=blogpost&amp;amp;files=0299wg.jpg-&quot; title=&quot;QuickPost&quot;&gt;
    &lt;img src=&quot;http://crackle.imageshack.us/img/butansn.png&quot; alt=&quot;QuickPost&quot; border=&quot;0&quot;&gt;&lt;/a&gt;   
Quickpost this image to Myspace, Digg, Facebook, and others!&lt;br/&gt;&lt;br/&gt;
</textarea>



    <div class="clear"></div>

   
 <!-- Bottom Menu -->   
     <div class="menu-bottom">
         <div class="menu-header">      
            <a href="http://imageshack.us/content.php?page=aboutus" onClick="pageTracker._trackEvent('new-footer-click','footer-about');" title="About Us" class="menu-bottom-link">About</a>|
            <a href="http://imageshack.us/content.php?page=advertising" onClick="pageTracker._trackEvent('new-footer-click','footer-advertising');" title="Advertise on ImageShack" class="menu-bottom-link">Advertising</a>|
            <a href="http://stream.imageshack.us/content.php?page=email&q=customer" onClick="pageTracker._trackEvent('new-footer-click','footer-contact');" title="Report Lost or Missing Images" class="menu-bottom-link">Contact</a>|
            <a href="http://stream.imageshack.us/content.php?page=email&amp;q=abuse" onClick="pageTracker._trackEvent('new-footer-click','footer-reportabuse');" title="Report Abuse or Request Deletion" class="menu-bottom-link">Report Abuse</a>|
            <a href="http://imageshack.us/content.php?page=developer" onClick="pageTracker._trackEvent('new-footer-click','footer-api');" title="API" class="menu-bottom-link">API</a>|
            <a href="http://imageshack.us/content.php?page=features" onClick="pageTracker._trackEvent('new-footer-click','footer-tools');" title="Tools" class="menu-bottom-link">Tools</a>|                
            <a href="http://imageshack.us/content.php?page=rules" onClick="pageTracker._trackEvent('new-footer-click','footer-tos');" title="ToS" class="menu-bottom-link">ToS</a>|
            <a href="http://imageshack.us/sitemap/" title="Sitemap" onClick="pageTracker._trackEvent('new-footer-click','footer-sitemap');" class="menu-bottom-link">Sitemap</a>|      
            <a href="http://blog.imageshack.us/blog/" title="Blog" onClick="pageTracker._trackEvent('new-footer-click','footer-blog');" class="menu-bottom-link">Blog</a>|     
            <a href="http://imageshack.us/content.php?page=jobs" onClick="pageTracker._trackEvent('new-footer-click','footer-jobs');" title="Jobs" class="menu-bottom-link">Jobs</a>|
            <a href="http://imageshack.us/content.php?page=faq" onClick="pageTracker._trackEvent('new-footer-click','footer-faq');" title="FAQ" class="menu-bottom-link">FAQ</a>|
        <a href="http://imageshack.us/content.php?page=help" onClick="pageTracker._trackEvent('new-footer-click','footer-help');" title="Help" class="menu-bottom-link">Help</a>

                 </div>    
     </div>           
     <div id="copyright">
         &copy; 2003-2010 ImageShack Corp. All rights reserved. 
     </div>
     

                  <div align="center">
        <form name="langForm" id="langForm" method="post" >
            <select class="lang" id="language" name="language" onChange="pageTracker._trackEvent('new-header-click','lang-'+this.value);" onmouseover="showBottomAd(false)" onmouseout="showBottomAd(true)"> 
              <option value="en" selected="selected">English</option>
              <option value="de">Deutsch</option>

              <option value="es">Español Ibérico</option>
              <option value="es_MX">Español latinoamericano</option>
              <option value="fr">Français</option>
              <option value="it">Italiano</option>
              <option value="pl">Polski</option>
              <option value="pt">Português do Brasil</option>

              <option value="tr">Türkçe</option>
              <option value="ru">Русский</option>
            </select> 
        </form>
      </div>
           
    </div> <!-- div.indent -->         
</div>  <!-- div.layout -->

<div id="login_dialog" title="Login" style="display:none">
    Login with your Imageshack username or email:    <table cellpadding="0" cellpadding="0" border="0" style="width:100%">
        <tr>
            <td style="width:100px; text-align:right;">
                &nbsp;
            </td>
            <td style="text-align:left;">
                <div style="width:245px;">
                    <div id="l_no_user_error" class="error" style="display:none; color:#D34209;font-weight:bold;"><i>Please enter your username or email address</i></div>

                    <div id="l_no_pass_error" class="error" style="display:none; color:#D34209;font-weight:bold;"><i>Please enter your password</i></div>
                    <div id="l_auth_failed_error" class="error" style="display:none; color:#D34209;font-weight:bold;"><i>Authentication failed. Please check username and password entered</i></div>
                </div>
            </td>
        </tr>
        <tr>
            <td style="width:100px; text-align:right;">
                Email:            </td>

            <td style="text-align:left;">
                <input id="l_login" style="font-style:italic;"/>
            </td>
        </tr>
        <tr>
            <td style="width:100px; text-align:right;">
                Password:            </td>
            <td style="text-align:left;">

                <input type="password" id="l_password"/>
            </td>
        </tr>
        <tr>
            <td style="width:100px; text-align:right;">
                &nbsp;
            </td>
            <td style="text-align:left;">
                <input type="checkbox" id="stay_logged_in" checked="checked" /><label for="stay_logged_in" style="font-size: 8pt;">Remember me</label>

                <input type="button" id="okbtn_login" style="cursor:pointer; margin-top:5px; margin-left:15px;" value="OK" onClick="pageTracker._trackEvent('new-header-click','login-ok');"/>
            </td>
        </tr>
    </table>

    <!--<input type="button" id="okbtn_login" style="cursor:pointer; margin-top:5px;" value="OK" onClick="pageTracker._trackEvent('new-header-click','login-ok');"/>-->
    <!--<input type="button" id="cancelbtn_login" value="Cancel" onClick="pageTracker._trackEvent('new-header-click','login-cancel');"/>-->
    <div align="left">    
       <a class="ser" href="http://my.imageshack.us/registration/passwordrecovery.php" onClick="pageTracker._trackEvent('new-header-click','login-forgot-password');" style="font-style:italic;font-size:8pt;">Forgot your password?</a>

    </div>
    <hr/>
    <p style="font-size:8pt;text-align:left;">If you are already registered with ImageShack, but do not have a password, please log in using your registration link and click on &quot;Preferences&quot; to create your new password.</p>
</div>
    <script type='text/javascript' src='http://crackle.imageshack.us/scripts/jquery/jquery-1.3.2.min.js'></script>
<script type="text/javascript" src="http://crackle.imageshack.us/scripts/jquery/jquery-ui-1.7.2.custom.min.js"></script>
<script type="text/javascript" src="http://crackle.imageshack.us/scripts/common/core-1.0.1.min.js"></script>

<div id="ad" align="center" style="margin-left:2px;">
  <!-- ca-pub-7137941865592088/Imageshack_Landing_Bottom -->
  <iframe id="is_landing_bottom" marginwidth="0" marginheight="0" cellspacing="0" cellpadding="0" src="" width="728px" height="90px" rel="Imageshack_Landing_Bottom" style="display:none; width:728px; height:90px; margin:10px auto" scrolling="no" frameborder="no"></iframe>
</div>


<div id="overlay" class="lightbox" style="width:340px; " >
  <div style="border:1px solid #ccc; background-color:white; padding:10px; margin:0 auto; width:318px;">
      <script src='http://imageshack.us/shareable/?i=0299wg.jpg&s=140&p=bl' type='text/javascript'></script><noscript>[URL=http://imageshack.us/photo/my-images/140/0299wg.jpg/][IMG]http://img140.imageshack.us/img140/4854/0299wg.jpg[/IMG][/URL]</noscript>

    </div>
  <div style="border:1px solid #ccc; padding:10px 10px 5px; width:318px; height:25px;">
    <input onClick="pageTracker._trackEvent('new-blue-click','shareable-click');" style="width:313px;" readonly="readonly" class="readonly" value="&lt;script src=&#039;http://imageshack.us/shareable/?i=0299wg.jpg&amp;s=140&#039; type=&#039;text/javascript&#039;&gt;&lt;/script&gt;&lt;noscript&gt;[URL=http://imageshack.us/photo/my-images/140/0299wg.jpg/][IMG]http://img140.imageshack.us/img140/4854/0299wg.jpg[/IMG][/URL]&lt;/noscript&gt;" />
  </div>
</div>

<div style="display: block; opacity: 0;" id="image-controls">
        <a id="rotate_right" title="Rotate Right" alt="Rotate Right" class="rotate-right" href="#">Right</a>
        <a id="zoominbutton" title="Zoom" alt="Zoom" class="zoom" href="#">Zoom</a>

        <a id="rotate_left" title="Rotate Left" alt="Rotate Left" class="rotate-left" href="#">Left</a>
</div>

<input type="hidden" id="org_fullimg_link" value="http://imageshack.us/photo/my-images/140/0299wg.jpg/"/>
<input type="hidden" id="in_ifs" value=""/>
<input type="hidden" id="media_width" value="318"/>
<input type="hidden" id="media_height" value="450"/>
<input type="hidden" id="_from_search" value=""/>
<input type="hidden" id="_from_newlp" value="1"/>
<input type="hidden" id="_kwd" value="my-images"/>
<input type="hidden" id="_server" value="140"/>
<input type="hidden" id="_image" value="0299wg.jpg"/>
<input type="hidden" id="is_porn" value=""/>
<input type="hidden" id="is_checked_nude" value=""/>
<script type="text/javascript">

   pageTracker._trackPageview("/search/None/Landing_page");

    pageTracker._trackEvent('ad-stats', 'ads-shown' );            
var LANG = 'en';
var SERVER = '140';
var IMAGE = '0299wg.jpg';
var RELATED_MODE = false;

    
    var RELATED_IMAGES = [];
var PREV_IMAGE = 'null';
var PREV_TYPE = 'photo';
var PREV_KWD = 'my-images';
var PREV_SERVER = null;
var NEXT_IMAGE = 'null';
var NEXT_TYPE = 'photo';
var NEXT_KWD = 'my-images';
var NEXT_SERVER = null;
var SITE_NAME   = 'blue';

var GEO = null;

var CHECK_VIDEO = false;

var GOOGLE_API_KEY = 'ABQIAAAAb4okmU6pZdrTn0X7lV3G7RRterEEbOrmoBhwISCGr9dC0WvkPxTTC2AunDwvdLh686P1woHbVx1iLA';

var prev_list = new Array();
var next_list = new Array();



<!-- ca-pub-7137941865592088/Imageshack_Landing_Pops -->
  GA_googleFillSlot("Imageshack_Landing_Pops");

// blur() made a problem in firefox so it should be removed.
function openPopunder(u,n,v) 
{  
    var ppp=window.open(u,n,v);
        window.focus();
}

</script>


<script type="text/javascript" src="http://crackle.imageshack.us/scripts/jquery/jquery.rotate.1-1.js"></script>
<script type="text/javascript" src="http://crackle.imageshack.us/nudejs/nude.min.js"></script>
<script type="text/javascript" src="http://crackle.imageshack.us/scripts/my/is_my.js"></script>
<script type="text/javascript" src="http://cdn.gigya.com/wildfire/js/wfapiv2.js"></script>



<input type="hidden" id="Quantcast_label" value="LPPage">
 
 
<!-- START OF New Rubicon insight API tag -->

<script type="text/javascript">
oz_api_key = "GRQL-G7FNS3Z0";
oz_api = "insight";
oz_ad_server = "gam1";

// RadiumOne code begin
document.write('<img src="http://rs.gwallet.com/r1/pixel/x1247r'+Math.round(Math.random()*10000000)+'" width="1" height="1" border="0" alt=""/>');
// RadiumOne code end 
</script>
<script type="text/javascript" src="http://tap-cdn.rubiconproject.com/partner/scripts/rubicon/dorothy.js"></script>
<!-- END OF New Rubion insight API tag -->

<!-- Rubicon insight tag -->
<script type="text/javascript" defer="defer" src="http://tap-cdn.rubiconproject.com/partner/scripts/rubicon/alice.js?pc=7991/12852"></script>

<!-- RadiumOne code begin -->
<noscript>
<img src="http://rs.gwallet.com/r1/pixel/x1247" width="1" height="1" border="0" alt=""/>
</noscript>
<!-- RadiumOne code end -->

<!-- Quantcast & comScore tags -->
<script type="text/javascript" src="http://crackle.imageshack.us/scripts/common/is-comscore.js"></script>

<!-- Start Quantcast tag -->
<noscript>
<a href="http://www.quantcast.com/p-65DrxcUXjcWq6" target="_blank"><img src="http://pixel.quantserve.com/pixel/p-65DrxcUXjcWq6.gif?labels=MyPageBlue" style="display: none;" border="0" height="1" width="1" alt="Quantcast"/></a>
</noscript>
<!-- End Quantcast tag -->

<!-- Begin comScore Tag -->
<noscript>
<img src="http://b.scorecardresearch.com/p?c1=2&c2=7518627&c3=&c4=&c5=&c6=&c15=&cj=1" />
</noscript>
<!-- End comScore Tag -->



</body>
</html>"""
        self.ishack = imageshack.ImageshackParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.ishack.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_imageshack_get_image_src(self):
        self.imageshack_src = self.ishack.imageshack_get_image_src(lxml.html.fromstring(self.example_ishack_page))
        self.assertIsInstance(self.imageshack_src, list)
        self.assertTrue(self.imageshack_src[0])

    def test_imageshack_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImageshack)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
