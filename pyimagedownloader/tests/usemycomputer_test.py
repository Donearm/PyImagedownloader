#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import usemycomputer

class TestUsemycomputer(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://usemycomputer.com/show.html?w=900&h=1237&i=/indeximages/women/Emma.Watson/002181756.jpg'
        self.example_umc_page = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <title>UseMyComputer</title>
        <link rel='stylesheet' type='text/css' href='/a.css'>
        <link rel='alternate' type='application/atom+xml' title='UseMyComputer Atom v1.0 syndication feed' href='/atom.xml'>
        <link rel='alternate' type='application/rss+xml' title='UseMyComputer - New Forum Posts' href='http://forums.usemycomputer.com/index.php?action=.xml;sa=recent;type=rss'>
        <link rel='alternate' type='application/rss+xml' title='UseMyComputer - New Forum Topics' href='http://forums.usemycomputer.com/index.php?action=.xml;sa=news;type=rss'>

        <link rel='contents' href='/archive/' title='UseMyComputer archive'>
        <meta name='description' content='A constantly updated collection of links, images and news items that appear to have been assembled by a speed-fuelled army of monkeys with a penchant for supermodels and technology. It%27 not Shakespeare, but it%27s not half bad either.'>
        <meta name='keywords' content='Celebrity, Supermodel, Photos, Pictures, Shots, Celebrity Gossip, Technology News, Daily, Daily News, Hot women, News, Links, Reference, Celebrity Photos, Candids, Paparazzi, Supermodel Pictures, Celebrity Candids, Articles, High resolution, UHQ, High quality'>
        <script language='javascript' type='text/javascript'><!-- if( top != self ) top.location.href = location.href; if( top.frames.length != 0 ) top.location=self.document.location; --></script>
    </head>
    <body style='min-width:1043px;'>
        <table width='100%' ><tr><td align='center'>
        <div class='header'>

            <div class='name'><a href='/'>UseMyComputer</a></div>
            <div class='menu'><ul><li><a href='/submit.html' title='Submit a post'>Submit</a></li><li><a href='/random.php' title='Take a chance'>Random</a></li><li><a href='/indeximages/' title='Organized posts' >Gallery</a></li><li><a href='/archive/' title='Archived Pages' >Archive</a></li><li><a href='http://forum.usemycomputer.com' title='Come interact with us'>Forum</a></li><li><span class='iphouse'><a href='http://ipHouse.com/' title='Quality hosting without the bullshit'>ipHouse</a></span></li></ul></div>
            <div style='clear: both;'></div>
        </div>
        <div class='middle' id='m' style='overflow:hidden;margin-left:0;margin-right:0;'>

            <table width='100%'>
                <tr>
                    <td>&nbsp;</td>
                    <td width='300' align='center'>
                        <iframe src='http://pages.etology.com/imp2/73929.php' width='300' height='250' style='border:0px;margin:0px;overflow:hidden' frameborder='0' scrolling='no'></iframe>
                    </td>
                    <td>&nbsp;</td>
                    <td width='300' align='center'>

                        <iframe frameborder=0 marginwidth=0 marginheight=0 scrolling=no width=300 height=250 src="http://adserving.cpxinteractive.com/st?ad_type=iframe&amp;ad_size=300x250&amp;section=245695"></iframe>
                    </td>
                    <td>&nbsp;</td>
                    <td width='300' align='center'>
                        <script type="text/javascript" language="javascript" src="http://www.qksz.net/1e-h85p"> </script>
                    </td>
                    <td>&nbsp;</td>
                </tr>

            </table>
            <div id='sw' style='display: none; margin: 1em; text-align: center; background-color: #FFFFCC;'>This image has been scaled down to fit the window.</div>
            <div style='text-align:center;overflow:hidden;margin-top:1em;' id='usemyimage'></div>
            <script type="text/javascript" src="/show.js"></script>
            <p>2009-05-20: Press F5 once if you don't see an image above.<br>set auto-scaling to: <a href="javascript:defaultScaling()" title="set default scaling mode">default</a>, <a href="javascript:disableScaling()" title="disable scaling">never</a>, or <a href="javascript:enableScaling()" title="set scaling mode">always</a><br></p>

        </div>
        <!-- IE min-width fix: http://www.cssplay.co.uk/boxes/width.html -->
        <div style='position:relative; width:90%; min-width:1043px;'><div style='float:left; position:relative; margin-right:-1043px;}'></div></div>
        </td></tr></table>
        <div class='footer'></div>
        <script type="text/javascript">var gaJsHost=(("https:"==document.location.protocol)?"https://ssl.":"http://www.");document.write(unescape("%3Cscript src='"+gaJsHost+"google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));</script>
        <script type="text/javascript">try{var pageTracker=_gat._getTracker("UA-2634378-1");pageTracker._trackPageview()}catch(err){}</script>
    </body>

</html>"""
        self.umc = usemycomputer.UsemycomputerParse(self.url, self.basedir)

    def test_usemycomputer_get_image_split_and_name(self):
        self.usemycomputer_split, self.imagename = self.umc.usemycomputer_get_image_split_and_name(self.url)
        self.assertIsInstance(self.usemycomputer_split, list)
        self.assertTrue(self.usemycomputer_split[0])
        self.assertIsInstance(self.imagename, list)
        self.assertTrue(self.imagename[0])

    def test_usemycomputer_save_image(self):
        #TODO: how to test this?
        pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUsemycomputer)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
