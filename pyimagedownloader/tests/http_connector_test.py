import unittest
#import re
import http_connector
import urllib2
from urllib import urlencode
from pyimg import *


class TestHttpConnector(unittest.TestCase):

    def setUp(self):
        self.urllist = ['www.google.com', 'www.repubblica.it', 'www.corriere.it']
        self.url = 'http://fashionography.net/'
        self.image_url = 'http://4.bp.blogspot.com/-xi8CKQeMa9U/TiB5xL4pP6I/AAAAAAAAQek/VHabxbfyKlc/s400/Sophie%2BHolmes%2Bby%2BPasquale%2BAbbattista%2B%2528Jet-Set%2BChic%2B-%2BElle%2BGermany%2BJune%2B2011%2529.jpg'
        self.referer = 'http://twitter.com/#!/fshngrphy'
        self.values = {}
        self.user_agent = user_agent
        self.headers = { 'User-Agent' : self.user_agent, 'Connection' : 'Keep-Alive' }
        self.connector = http_connector.Connector()

    def test_threadsafe_opener_debug(self):
        """Test for the correct creation of urllib's opener with activated 
        debug"""
        debug = 1
        self.opener_debug = self.connector.threadsafe_opener()
        self.assertIsInstance(self.opener_debug, urllib2.OpenerDirector)

    def test_threadsafe_opener(self):
        """Test for the correct creation of urllib's opener"""
        debug = 0
        self.opener = self.connector.threadsafe_opener()
        self.assertIsInstance(self.opener, urllib2.OpenerDirector)

#    def test_site_login(self, url, opener=''):
#       TODO: how to test this?
#        pass

    def test_post_request(self):
        response = self.connector.post_request(self.url, urlencode(self.values), self.headers)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_post_request_with_referer(self):
        response = self.connector.post_request(self.url, urlencode(self.values), self.headers, self.referer)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_get_request(self):
        response = self.connector.get_request(self.url, self.headers)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_get_request_with_referer(self):
        response = self.connector.get_request(self.url, self.headers, self.referer)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_get_filename(self):
        filename = self.connector.get_filename(self.image_url) 
        self.assertIsInstance(filename, str)
        self.assertTrue(len(filename) > 0)

    def test_check_string_or_list(self):
        uri_from_list = self.connector.check_string_or_list(self.urllist)
        uri_from_url = self.connector.check_string_or_list(self.url)
        self.assertIsInstance(uri_from_list, str)
        self.assertIsInstance(uri_from_url, str)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHttpConnector)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
