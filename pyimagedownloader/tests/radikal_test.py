#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import radikal
import lxml.html

class TestRadikal(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://radikal.ru/F/s58.radikal.ru/i159/0904/4d/2f35f54b7251.jpg.html'
        self.example_rdkl_page = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>
    
  Радикал-Фото :: Увеличенное изображение

</title>
  <script type="text/javascript" src="/scripts/DefaultMasterPageAction.js"></script>
  <script type="text/javascript" src="/scripts/geo_integration_action.js"></script>
  
  <script type="text/javascript" src="/BridgeLegacy/Static/SCRIPTS/jquery-1.3.1.min.json.js"></script>
  <script type="text/javascript" src="/BridgeLegacy/Static/SCRIPTS/inj_dlg.js"></script>

  <script type="text/javascript" src="/BridgeLegacy/Static/SCRIPTS/inject_vote.js?3"></script>
  
  <script type="text/javascript">
    var MainImg = new Object();
    MainImg.Url = 'http://s58.radikal.ru/i159/0904/4d/2f35f54b7251.jpg';
    MainImg.ID_DISPLAY_FOR_USER = '121878307';
    MainImg.UrlPreviewPageF = 'http://radikal.ru/';
  </script>
  <link href="/BridgeLegacy/Static/Design/InjStyleSheet.css" rel="stylesheet" type="text/css" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><meta name="description" content="Специализированный ресурс для публикации фотографий на форумах: автоматическая оптимизация, создание превью" /><meta name="keywords" content="закачать фото на сайт, на форум, загрузить фотографии, фото, фотки, картинки, юзерпик, как разместить фотографию на форуме, публикация фотографий, оптимизация фотографий для Интернета, хостинг фотографий, где разместить фотографии, эффективная интернет реклама, pr кампании, размещение рекламы, маркетинг в интернет, продвижение, целевая аудитория" /><link href="/Design/cssStyles/main.css" rel="stylesheet" type="text/css" /></head>
<body>
  
  <div style="position: absolute; top: -1000px; left: -1000px;">
    



<!--LiveInternet counter--><script type="text/javascript"><!--
new Image().src = "http://counter.yadro.ru/hit?r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";"+Math.random();//--></script><!--/LiveInternet-->


<!--begin of Rambler's Top100 code -->
<a href="http://top100.rambler.ru/top100/" style="left: 1px; position: absolute; top: 1px;">
<img src="http://counter.rambler.ru/top100.cnt?741781" alt="" width="1" height="1" border="0" /></a>
<!--end of Top100 code-->

<!-- tns-counter.ru -->
<script language="JavaScript" type="text/javascript">
    var img = new Image();
    img.src = 'http://www.tns-counter.ru/V13a***R>' + document.referrer.replace(/\*/g,'%2a') + '*odnoklassniki_ru/ru/UTF-8/tmsec=radikal_total/';
</script>
<noscript>
    <img src="http://www.tns-counter.ru/V13a****odnoklassniki_ru/ru/UTF-8/tmsec=radikal_total/" width="1" height="1" alt=""/>
</noscript>
<!--/ tns-counter.ru -->

    

  </div>
  <form name="aspnetForm" method="post" action="default.aspx" id="aspnetForm" style="position: absolute;
  top: -200px;">

  <div>
    <input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
    <input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
    <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="" />
  </div>
  <script type="text/javascript">
    //<![CDATA[
    var theForm = document.forms['aspnetForm'];
    if (!theForm) {
      theForm = document.aspnetForm;
    }
    function __doPostBack(eventTarget, eventArgument) {
      if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
      }
    }
    //]]>
  </script>
  <script src="/scripts2/WebResource.axd.js" type="text/javascript"></script>
  <script src="/scripts2/ScriptResource.axd.1.js" type="text/javascript"></script>

  <script src="/scripts2/ScriptResource.axd.2.js" type="text/javascript"></script>
  <script src="/scripts2/Gallery.js" type="text/javascript"></script>
  <script src="/scripts2/integrforum.js" type="text/javascript"></script>
  <script src="/scripts2/MainPageAction.js" type="text/javascript"></script>
  <script type="text/javascript">
    //<![CDATA[
    Sys.WebForms.PageRequestManager._initialize('ctl00$ScriptManager1', document.getElementById('aspnetForm'));
    Sys.WebForms.PageRequestManager.getInstance()._updateControls([], [], [], 90);
    //]]>
  </script>
  <script type="text/javascript">
    //<![CDATA[
    Sys.Application.initialize();
    //]]>
  </script>

  </form>
  
  <div class="topp">
    <table cellpadding="0" cellspacing="0" border="0" width="1004">
      <tr>
        <td colspan="2">
          <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
            <tr style="width: 100%;">
              <td align="left" style="padding-left: 0px; width: 240px;">
                <div class="logo" style="text-align: left; height: 90px; width: 238px; overflow: hidden;">

                  <a href="/">
                    <img src="/Design/Logo/rf_logo.gif" width="240" height="94" border="0" title="Радикал-Фото - создай фотоальбом на любимом форуме"
                      alt="Радикал-Фото - создай фотоальбом на любимом форуме" /></a></div>
              </td>
              <td>
                

<div id="top_ban" style="width: 760px; height: 90px; padding: 0px; margin: 0px; border-style: none; border-width: 0px; overflow:hidden;">



 <!-- izitizi.ru, REFLECTION -->
  <div id="div_teaser_2542">загрузка...</div>

 <!-- izitizi.ru, END -->
 
</div>

                
              </td>
            </tr>
          </table>
        </td>
        <td valign="top" rowspan="4">
           

<div id="right_ban0" style="width:240px; height:140px; margin:0px; padding:0px; overflow:hidden; ">



<div id="PC_Teaser_Block_37524">загрузка...</div>

</div>

<div id="right_ban" style="width: 240px; height:420px; margin:0px; padding:0px; overflow:hidden; ">

  <iframe src="http://r.radikal.ru/bh.ashx?pt=4&ur=&rnd=365740559&syncid=9da80131f04b47ee90cfa1ba7eb77f87"
    frameborder="0" marginheight="0" marginwidth="0" scrolling="no" width="240" height="400">
  </iframe>


</div>

<div id="right_ban2"  style="width: 240px; height:420px; margin-top:0px; margin-right: 0px; margin-left: 0px; margin-bottom: 5px; overflow:hidden;">



<div class="rtv_videofield"></div> 
<script type="text/javascript" src="http://sdata.7rtv.com/js/0001radikal_fs.js"></script>

</div>


        </td>
      </tr>
      <tr>

        <td style="width: 245px;" valign="top" rowspan="2" id="imgtd">
           
<div style="margin-top: 0px; margin-bottom: 2px;">
  
  
  
  <div style="margin-top:20px;"></div>
  
</div>
<div id="left_ban" style="width: 240px; height:420px; margin:0px; padding:0px; overflow:hidden;">

  <iframe src="http://r.radikal.ru/bh.ashx?pt=1&ur=&rnd=365740559&syncid=9da80131f04b47ee90cfa1ba7eb77f87"
    frameborder="0" marginheight="0" marginwidth="0" scrolling="no" width="240" height="400">
  </iframe>


</div>


<div id="left_ban2"  style="width: 240px; height:420px; margin-top:0px; margin-right: 0px; margin-left: 0px; margin-bottom: 5px; overflow:hidden;">



<!-- izitizi.ru, REFLECTION -->
  <div id="div_teaser_3200">загрузка...</div>
 <!-- izitizi.ru, END -->
 
</div>


        </td>

        <td valign="top" style="border-spacing: 10px">
          
<input type="hidden" id="sn" value="S35" />


          
  <!--
  
  
  
    -->
  
  <input type="hidden" id="h_codetype" value="0" />
  <input type="hidden" id="h_codeset" value="0" />
  <input type="hidden" id="h_codeisburl" value="1" />
  <input type="hidden" id="h_codeburl" value="http://www.radikal.ru" />
  <div style="text-align: left; margin-left: 15px; border-color: Red; border-style: solid;
    border-width: 0px;">

    <div style="text-align: left; margin: 5px;">
      <a style="display: none;" class="blue11" target="_blank" href="#" onclick="ButGetImgCodeClick2(); return false;">
        Получить ссылки</a> <a href="/toadmin.aspx?t=0&bimg=http%3a%2f%2fs58.radikal.ru%2fi159%2f0904%2f4d%2f2f35f54b7251.jpg"
          style="margin-left: 10px;" target="_blank" class="blue11">Пожаловаться администратору</a>
      
      <div id="PhCodeImgDialog2" style="position: relative;">
      </div>
      <img src="http://s58.radikal.ru/i159/0904/4d/2f35f54b7251.jpg" border="0" />
    </div>

  </div>
  <!-- 




<script language="javascript" charset="windows-1251" src="http://c.am10.ru/code/sb/radikal.ru.js"></script>

 <!-- izitizi.ru, CLIENT -->
 <script language="Javascript">
  var id = '3200';
  var ref = escape(document.referrer); var server = 'izitizi.ru';
  document.write('<scr'+'ipt type="text/jav'+'ascript" src="http://'+server+'/teaser.php?id='+id+'"></scr'+'ipt>');
 </script>
 <!-- izitizi.ru, END -->
 
 <!-- izitizi.ru, CLIENT -->
 <script language="Javascript">
  var id = '2542';
  var ref = escape(document.referrer); var server = 'izitizi.ru';
  document.write('<scr'+'ipt type="text/jav'+'ascript" src="http://'+server+'/teaser.php?id='+id+'"></scr'+'ipt>');
 </script>
 <!-- izitizi.ru, END -->

<script type="text/javascript">var RNum = Math.floor(Math.random()*10000); document.write('<scr'+'ipt language="javascript" type="text/javascript" src="http://n.adonweb.ru/payclick/adv-out/?Id=37524&RNum='+RNum+'&Referer='+escape(document.referrer)+'"><'+'/scr'+'ipt>');</script>

<script charset="windows-1251" type="text/javascript" src="http://www.directadvert.ru/show.cgi?adp=18034&div=DIV_DA_18034"></script>

    -->

          
<div>

<div id="DIV_DA_18034"></div>

</div>

          
          
          
        </td>
      </tr>
      <tr>

        <td colspan="2" valign="bottom">
          
          
        </td>
      </tr>
      <tr>
        <td colspan="2">
          

<table cellpadding="0" cellspacing="2" border="0" class="bottomcontr">
  <tr>
    <td>
      <a href="http://top100.rambler.ru/cgi-bin/stats_top100.cgi?741781" target="_blank"><img height="31" alt="Rambler's Top100" src="http://top100-images.rambler.ru/top100/banner-88x31-rambler-black2.gif" width="88" border="0" /></a>

    </td>
    <td>
      &nbsp;
    </td>
    <td width="100%" align="center">
       <a class="white10" href="/">Главная</a>
       &nbsp;|&nbsp;
       <a class="white10" href="/faq.aspx">Правила</a>

       &nbsp;|&nbsp;
       <a class="white10" href="/GALLERY/PageListGallery.aspx">Галереи</a>
       &nbsp;|&nbsp;
       <a class="white10" href="/contacts.aspx">Контакты</a>
       &nbsp;|&nbsp;
       <a class="white10" href="/youradv.aspx">Реклама</a>

       <br />
       Copyright Radikal.ru 2005-2011 | www.radikal.ru
    </td>
    <td>
      <a href="http://www.yandex.ru/cy?base=0&host=radikal.ru" target="_blank"><img src="http://www.yandex.ru/cycounter?radikal.ru" width="88" height="31" alt="Яндекс цитирования" border="0" /></a>
    </td>
    <td>
<!--LiveInternet logo--><a href="http://www.liveinternet.ru/click"
target=_blank><img src="http://counter.yadro.ru/logo?14.11"
title="LiveInternet: показано число просмотров за 24 часа, посетителей за 24 часа и за сегодня"
alt="" border=0 width=88 height=31></a><!--/LiveInternet-->
    </td>

  </tr>
</table>

        </td>
      </tr>
    </table>
  </div>

  <script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
  </script>
  <script type="text/javascript">
    try {
      var pageTracker = _gat._getTracker("UA-7858432-1");
      pageTracker._trackPageview();
    } catch (err) { }</script>

</body>
</html>





<script language="javascript" charset="windows-1251" src="http://c.am10.ru/code/sb/radikal.ru.js"></script>

 <!-- izitizi.ru, CLIENT -->
 <script language="Javascript">
  var id = '3200';
  var ref = escape(document.referrer); var server = 'izitizi.ru';
  document.write('<scr'+'ipt type="text/jav'+'ascript" src="http://'+server+'/teaser.php?id='+id+'"></scr'+'ipt>');
 </script>
 <!-- izitizi.ru, END -->

 
 <!-- izitizi.ru, CLIENT -->
 <script language="Javascript">
  var id = '2542';
  var ref = escape(document.referrer); var server = 'izitizi.ru';
  document.write('<scr'+'ipt type="text/jav'+'ascript" src="http://'+server+'/teaser.php?id='+id+'"></scr'+'ipt>');
 </script>
 <!-- izitizi.ru, END -->

<script type="text/javascript">var RNum = Math.floor(Math.random()*10000); document.write('<scr'+'ipt language="javascript" type="text/javascript" src="http://n.adonweb.ru/payclick/adv-out/?Id=37524&RNum='+RNum+'&Referer='+escape(document.referrer)+'"><'+'/scr'+'ipt>');</script>

<script charset="windows-1251" type="text/javascript" src="http://www.directadvert.ru/show.cgi?adp=18034&div=DIV_DA_18034"></script>"""
        self.rdkl = radikal.RadikalParse(self.url, self.basedir)

    def test_process_url(self):
        self.page = self.rdkl.process_url(self.url)
        self.assertIsInstance(self.page, lxml.html.HtmlElement)

    def test_radikal_get_image_src(self):
        self.radikal_src = self.rdkl.radikal_get_image_src(lxml.html.fromstring(self.example_rdkl_page))
        self.assertIsInstance(self.radikal_src, list)
        self.assertTrue(self.radikal_src[0])

    def test_radikal_get_image_name(self):
        self.imagename = self.rdkl.radikal_get_image_name(self.url)
        self.assertIsInstance(self.imagename, list)
        self.assertTrue(self.imagename[0])

    def test_radikal_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRadikal)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
