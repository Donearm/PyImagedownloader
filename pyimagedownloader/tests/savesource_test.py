import unittest
import savesource
import http_connector

class TestSavesource(unittest.TestCase):

    def setUp(self):
        self.common_domain = 'http://www.google.com'
        self.brazilian_domain = 'http://www.tam.com.br'
        self.url = 'http://mode.newslicious.net/'
        self.utf8_url = 'http://mode.newslicious.net/2011/07/january-3-amanda-nrgaard-katrin.html'
        self.basedir = '/mnt/d/Maidens/Uploads/'
        self.creditor = 'nirari@celebrityforum'
        self.utf8_title = u'prover\xc3\xb2 a \xc3\xa6 in \xc3\xa5 for \xc3\x97'
        self.title_with_nonaccepted_chars = 'Try with [some] NOT accepted chars \' /\ '
        self.nonaccepted_chars = '\/\''
        self.ss = savesource.SaveSource(self.url, self.basedir, self.creditor)

    def test_extract_common_domain(self):
        """test for extraction of the TLD from a url"""
        string = self.ss.extract_domain(self.common_domain)
        self.assertIsInstance(string, str)

    def test_extract_brazilian_domain(self):
        """test for extraction of a TLD containing a dot (like brazilians or uk 
        ones)"""
        string = self.ss.extract_domain(self.brazilian_domain)
        self.assertIsInstance(string, str)
        self.assertIn('.', string)

    def test_get_page_title(self):
        """test for extraction of webpage's title as a string or as unicode
        (for sites containing unicode characters in the title)"""
        connector = http_connector.Connector()
        response = connector.reqhandler(self.url, 1)
        response_utf8 = connector.reqhandler(self.utf8_url, 1)
        title = self.ss.get_page_title(response)
        title_utf8 = self.ss.get_page_title(response_utf8)
        self.assertIsInstance(title, str)
        self.assertIsInstance(title_utf8, unicode)

    def test_decode_htmlentities(self):
        """test translation of html entities to corresponding unicode 
        characters"""
        no_htmlentities = self.ss.decode_htmlentities(self.utf8_title)
        self.assertIsInstance(no_htmlentities, unicode)

    def test_clean_title(self):
        """test for the removal of non accepted chars from webpage title"""
        neat_title = self.ss.clean_title(self.title_with_nonaccepted_chars)
        self.assertNotIn(self.nonaccepted_chars, neat_title)
        self.assertIsNotNone(neat_title)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSavesource)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
