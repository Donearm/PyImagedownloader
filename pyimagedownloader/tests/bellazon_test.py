#!/usr/bin/env python2

import unittest
import bellazon
import http_connector
from os.path import isfile, join, getsize

class TestBellazon(unittest.TestCase):

    def setUp(self):
        self.basedir = '/mnt/documents/Maidens/Uploads/'
        self.url = 'http://www.bellazon.com/main/topic/4517-lena-gercke/page__st__800#entry2978466'
        self.image_url = 'http://www.bellazon.com/main/index.php?app=core&module=attach&section=attach&attach_rel_module=post&attach_id=1647508'
        self.bz = bellazon.BellazonParse(self.url, self.basedir)

    def test_bellazon_save_image(self):
        connector = http_connector.Connector()
        self.bz.bellazon_save_image(self.image_url)
        # get the filename to save on disk
        savefile = join(self.basedir, str(connector.get_filename(self.image_url, 'attach_id=')))
        # has the file been downloaded?
        self.assertTrue(isfile(savefile))
        # check that file is bigger than 1K
        self.assertTrue(getsize(savefile) >= 1000)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBellazon)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
