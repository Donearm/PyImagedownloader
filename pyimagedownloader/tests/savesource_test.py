import unittest
#import pyimagedownloader.savesource
#from pyimagedownloader.pyimagedownloader import savesource
#from .. import savesource
# from . import savesource
import savesource

class TestSavesource(unittest.TestCase):

    def setUp(self):
        self.common_domain = 'http://www.google.com'
        self.brazilian_domain = 'http://www.tam.com.br'
        self.url = 'http://forum.phun.org/showthread.php?t=652134'
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.creditor = 'nirari@celebrityforum'
        self.utf8_title = u'prover\xc3\xb2 a \xc3\xa6 in \xc3\xa5 for \xc3\x97'
        self.title_with_nonaccepted_chars = 'Try with [some] NOT accepted chars \' /\ '
        self.nonaccepted_chars = '\/\''
        self.ss = savesource.SaveSource(self.url, self.basedir, self.creditor)

    def test_extract_common_domain(self):
        string = self.ss.extract_domain(self.common_domain)
        self.assertIsInstance(string, str)

    def test_extract_brazilian_domain(self):
        string = self.ss.extract_domain(self.brazilian_domain)
        self.assertIsInstance(string, str)

    def test_get_page_title(self):
        response, url_string = self.ss.process_page(self.url)
        title = self.ss.get_page_title(response)
        self.assertIsInstance(title, str)

    def test_decode_htmlentities(self):
        no_htmlentities = self.ss.decode_htmlentities(self.utf8_title)
        self.assertIsInstance(no_htmlentities, unicode)

    def test_clean_title(self):
        neat_title = self.ss.clean_title(self.title_with_nonaccepted_chars)
        self.assertNotIn(self.nonaccepted_chars, neat_title)


def main():
#     unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSavesource)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
