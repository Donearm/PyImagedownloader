#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import tumblr
import lxml.html

class TestTumblr(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://fuckyeahsimodels.tumblr.com/post/6544001799'
        self.example_tum_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">


<!--    
    'Heart In A Cage' theme for Tumblr by Fusels (c) 2010
    http://fusels.tumblr.com
-->

<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="color:background" content="#f1ddb8"/>
        <meta name="color:text" content="#868686"/>
        <meta name="color:title" content="#56aac4"/>
        <meta name="color:link" content="#7dd8db"/>

        <meta name="color:hover" content="#d5aedb"/>
        <meta name="text:title font size" content="24px"/>
        <meta name="text:title line height" content="23px"/>
        <meta name="text:title letter spacing" content="-1px"/>
        <meta name="text:title font weight" content="normal"/>
        <meta name="font:title" content="arial"/>
        <meta name="image:Background" content=""/>
        <meta name="image:Sidebar" content=""/>
        <meta name="if:show sidebar image" content="0"/>

        <meta name="if:show blog title" content="1"/>
    <meta name="if:cursive font" content="1">

<!-- 'Lorie' font from Anthagio.com -->
<!-- Script from typeface.js -->


<meta name="description" content="" />
    <title>Fuck Yeah Sports Illustrated Swimsuit Models!</title>

    <style type="text/css">
body {
margin:0px;
background-color: #f1ddb8;
background-image:url(1);
background-attachment: fixed;
background-repeat: repeat;}
body, div, p, textarea, submit, input{
font-family: arial;
font-size: 11px;
line-height:13px;
color:#d5aedb;
}

p {
margin:0px;
margin-top:5px;
}


a:link, a:active, a:visited{
color: #868686; 
text-decoration: none; 
}

a:hover {
color:#56aac4;
text-decoration: none;
}


div#cage{
margin:auto;
position:relative;
width:750px;
overflow:hidden;
color: #7dd8db;
_margin-left:10%;
}


div#center{
margin:auto;
position:relative;
width:740px;
background-color:;
overflow:auto;
overflow-y:hidden;
}

div#content{
float:right;
width:500px;
padding:10px;
padding-top: 0px;
margin-right: 10px;
background: #fff;
}

div#entry{
background-color:;
margin-top:px;
padding-top:10px;
padding-bottom:10px;
}


div#sidebar{
position:fixed !important;
width: 200px;
height:100%;
background-color:white;
margin: 0px 0px 0px 0px; 
border-right:1px dashed #ddd;
padding-top:10px;
padding-left:10px;
}


#postnotes{
text-align: justify;}

#postnotes blockquote{
border: 0px;}

.title{
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
font-size: 24px;
line-height: normal;
color: #7dd8db; 
letter-spacing: -1px;
font-weight: 23px;
padding:1px 1px 0px 1px; 
}

.title2{
font-family: Arial, Helvetica;
font-size: 24px;
line-height: normal;
color: #7dd8db; 
letter-spacing: -1px;
font-weight: 23px;
padding:1px 1px 0px 1px; 
}

blockquote{
padding:0px 0px 2px 5px;
margin:0px 0px 2px 1px;
border-left: 1px dashed #d5aedb;
}

blockquote p, ul{
margin:0px; 
padding:0px; 
}


a img{border: 0px;}

ul, ol, li{list-style:none; margin:0px; padding:0px;}

.user_1 .label, .user_2 .label, .user_3 .label, .user_4 .label, .user_5 .label, .user_6 .label, 
.user_7 .label, .user_8 .label, .user_9 .label {color:#7dd8db;}

.notes img{width:10px; position:relative; top:3px;}


.permalink{
display: block;
text-transform: lowercase;
font-size: 9px;
text-align: right;
}

small{font-size: 9px;}

    
    </style>

    <link rel="shortcut icon" href="http://28.media.tumblr.com/avatar_373b60f0b690_16.png">
    <link rel="alternate" type="application/rss+xml" title="RSS" href="http://fuckyeahsimodels.tumblr.com/rss" />
    <meta name="viewport" content="width=820" />
<meta http-equiv="x-dns-prefetch-control" content="off"/></head>
<body>

<div id="cage">
<div id="center">

<div id="sidebar">

<span class=title><a href="/">
Fuck Yeah Sports Illustrated Swimsuit Models!
</a></span><br>

This is a blog to appreciate the gorgeous Sports Illustrated Swimsuit issue models, Past and Present (but there will be much more of the present ones.)<p>

If you want to see more of  a specific model(s) leave suggestions in the ask box or submit pictures
<p><p>
<!-- Start FreeOnlineUsers.com -->
<a href="http://www.freeonlineusers.com">
<font color=#7dd8db><script type="text/javascript" src="http://st1.freeonlineusers.com/on3.php?id=532221"> </script> people doing the creep</font></a>
<!-- End FreeOnlineUsers.com -->
<p><p>
<a href="http://catfoy.tumblr.com/">Personal</a>
<br>
<br><center>

<a href="/archive">Archive</a> · <a
href="/random">Random</a> · <a href="http://fuckyeahsimodels.tumblr.com/rss">RSS</a> 


<a href="/ask">· Ask me anything</a>
<a href="/submit">· Submit</a>





</center>
<br>

<center>
  
  

  <a href="http://fuckyeahsimodels.tumblr.com/post/6543792964" class=title2>«</a>
  <a href="http://fuckyeahsimodels.tumblr.com/post/6544136623" class=title2>»</a>

</center>


</div>

<div id="content">
    
    <div id="entry">
    
    
    
    
    <CEnter>
        <a href="http://www.tumblr.com/photo/1280/6544001799/1/tumblr_lmtbgqlyIR1qjbzrl"><img src="http://29.media.tumblr.com/tumblr_lmtbgqlyIR1qjbzrlo1_500.jpg" alt="" width=500px></a></center>
        
    
    
    
    
    

    
    
    
    



<span class="permalink"><a href="http://fuckyeahsimodels.tumblr.com/post/6544001799">
Tuesday Jun 6 @ 11:38pm
</a></span>


<center>
9 notes<br>

 
tagged as: <a href="http://fuckyeahsimodels.tumblr.com/tagged/cintia_dicker">cintia dicker. </a><br> 

</center></span>
 <br>
<div id="postnotes">
<ol class="notes">
    <!-- START NOTES -->
                    
        <li class="
            note
            like                            tumblelog_circemalfoy                                    without_commentary        ">        
                                                <a href="http://circemalfoy.tumblr.com/" title="Circe Malfoy"><img src="http://28.media.tumblr.com/avatar_a9ced9aa582b_16.png" class="avatar" alt=""/></a>
                                
                <span class="action">                
                                        
                                            <a href="http://circemalfoy.tumblr.com/" title="Circe Malfoy">circemalfoy</a> liked this                                    </span>

                
                <div class="clear"></div>
                        
                        
                    </li> 
                    
        <li class="
            note
            reblog                            tumblelog_im-amazed                                    without_commentary        ">        
                   
                                                            <a href="http://im-amazed.tumblr.com/" title="it&#039;s a maze"><img
                        src="http://25.media.tumblr.com/avatar_4c44997cddb5_16.png" class="avatar" alt="" /></a>
                                        
                    <span class="action">
                                                                                
                                                                                                                                                                                    <a href="http://im-amazed.tumblr.com/" class="tumblelog" title="it&#039;s a maze">im-amazed</a> reblogged this from <a href="http://fuckyeahsimodels.tumblr.com/" class="source_tumblelog" title="Fuck Yeah Sports Illustrated Swimsuit Models!">fuckyeahsimodels</a>                                                                                                                                                                                    </span>
                    <div class="clear"></div>

                    
                                                            
                        
                    </li> 
                    
        <li class="
            note
            reblog                            tumblelog_lesboner                                    without_commentary        ">        
                   
                                                            <a href="http://lesboner.tumblr.com/" title="I have a huge lesboner."><img
                        src="http://25.media.tumblr.com/avatar_22f413f2a887_16.png" class="avatar" alt="" /></a>
                                        
                    <span class="action">
                                                                                
                                                                                                                                                                                    <a href="http://lesboner.tumblr.com/" class="tumblelog" title="I have a huge lesboner.">lesboner</a> reblogged this from <a href="http://fuckyeahsimodels.tumblr.com/" class="source_tumblelog" title="Fuck Yeah Sports Illustrated Swimsuit Models!">fuckyeahsimodels</a>                                                                                                                                                                                    </span>
                    <div class="clear"></div>
                    
                                                            
                        
                    </li> 
                    
        <li class="
            note
            reblog                            tumblelog_redmeansstopandadmire                                    with_commentary        ">        
                   
                                                            <a href="http://redmeansstopandadmire.tumblr.com/" title="Red Means Stop (&amp; admire)"><img
                        src="http://28.media.tumblr.com/avatar_ef0345a500b0_16.png" class="avatar" alt="" /></a>

                                        
                    <span class="action">
                                                                                
                                                                                                                                                                                    <a href="http://redmeansstopandadmire.tumblr.com/" class="tumblelog" title="Red Means Stop (&amp; admire)">redmeansstopandadmire</a> reblogged this from <a href="http://fuckyeahsimodels.tumblr.com/" class="source_tumblelog" title="Fuck Yeah Sports Illustrated Swimsuit Models!">fuckyeahsimodels</a> and added:                                                                                                                                                                                    </span>
                    <div class="clear"></div>
                    
                                            <blockquote>
                            <a href="http://redmeansstopandadmire.tumblr.com/post/6594061682" title="View post">
                                “Cintia was here.”                            </a>

                        </blockquote>
                                                            
                        
                    </li> 
                    
        <li class="
            note
            reblog                            tumblelog_tinythunder94                                    without_commentary        ">        
                   
                                                            <a href="http://tinythunder94.tumblr.com/" title="Tiny Thunder"><img
                        src="http://26.media.tumblr.com/avatar_4e131a8783d7_16.png" class="avatar" alt="" /></a>
                                        
                    <span class="action">
                                                                                
                                                                                                                                                                                    <a href="http://tinythunder94.tumblr.com/" class="tumblelog" title="Tiny Thunder">tinythunder94</a> reblogged this from <a href="http://thintothespo.tumblr.com/" class="source_tumblelog" title="thin to the spo">thintothespo</a>                                                                                                                                                                                    </span>
                    <div class="clear"></div>

                    
                                                            
                        
                    </li> 
                    
        <li class="
            note
            reblog                            tumblelog_thintothespo                                    without_commentary        ">        
                   
                                                            <a href="http://thintothespo.tumblr.com/" title="thin to the spo"><img
                        src="http://28.media.tumblr.com/avatar_a9d6ea81d496_16.png" class="avatar" alt="" /></a>
                                        
                    <span class="action">
                                                                                
                                                                                                                                                                                    <a href="http://thintothespo.tumblr.com/" class="tumblelog" title="thin to the spo">thintothespo</a> reblogged this from <a href="http://fuckyeahsimodels.tumblr.com/" class="source_tumblelog" title="Fuck Yeah Sports Illustrated Swimsuit Models!">fuckyeahsimodels</a>                                                                                                                                                                                    </span>
                    <div class="clear"></div>
                    
                                                            
                        
                    </li> 
                    
        <li class="
            note
            like                            tumblelog_beautyfetishist                                    without_commentary        ">        
                                                <a href="http://beautyfetishist.tumblr.com/" title="beautyfetishist"><img src="http://27.media.tumblr.com/avatar_f53bdb6db8f6_16.png" class="avatar" alt=""/></a>

                                
                <span class="action">                
                                        
                                            <a href="http://beautyfetishist.tumblr.com/" title="beautyfetishist">beautyfetishist</a> liked this                                    </span>
                
                <div class="clear"></div>
                        
                        
                    </li> 
                    
        <li class="
            note
            reblog                            tumblelog_fuckyeahsimodels                                    without_commentary        ">        
                   
                                                            <a href="http://fuckyeahsimodels.tumblr.com/" title="Fuck Yeah Sports Illustrated Swimsuit Models!"><img
                        src="http://28.media.tumblr.com/avatar_373b60f0b690_16.png" class="avatar" alt="" /></a>
                                        
                    <span class="action">
                                                                                
                                                            <a href="http://fuckyeahsimodels.tumblr.com/" class="tumblelog" title="Fuck Yeah Sports Illustrated Swimsuit Models!">fuckyeahsimodels</a> posted this                                                                        </span>

                    <div class="clear"></div>
                    
                                                            
                        
                    </li> 
        
        
    <!-- END NOTES -->
</ol></div><br>

<center></center>


        </div>
    

<small><center>Powered by <a href="http://tumblr.com">Tumblr</a> :: Themed by <a href="http://fusels.tumblr.com">Fusels</a>

</div></div>

</div><center>   


</center>

<!-- BEGIN TUMBLR CODE --><iframe src="http://assets.tumblr.com/iframe.html?9&src=http%3A%2F%2Ffuckyeahsimodels.tumblr.com%2Fpost%2F6544001799&amp;pid=6544001799&amp;rk=RGjDslIu&amp;lang=en_US&amp;name=fuckyeahsimodels" scrolling="no" width="330" height="25" frameborder="0" style="position:absolute; z-index:1337; top:0px; right:0px; border:0px; background-color:transparent; overflow:hidden;" id="tumblr_controls"></iframe><!--[if IE]><script type="text/javascript">document.getElementById('tumblr_controls').allowTransparency=true;</script><![endif]--><script type="text/javascript">_qoptions={qacct:"p-19UtqE8ngoZbM"};</script><script type="text/javascript" src="http://edge.quantserve.com/quant.js"></script><noscript><img src="http://pixel.quantserve.com/pixel/p-19UtqE8ngoZbM.gif" style="display:none; border-width:0px; height:1px; width:1px;" alt=""/></noscript><!-- END TUMBLR CODE --></body>
</html>""" 
        self.tum = tumblr.TumblrParse(self.url, self.basedir)

    def test_tumblr_get_image_split(self):
        self.tumblr_split = self.tum.tumblr_get_image_split(self.url)
        self.assertIsInstance(self.tumblr_split, list)
        self.assertTrue(self.tumblr_split[0])

    def test_tumblr_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTumblr)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
