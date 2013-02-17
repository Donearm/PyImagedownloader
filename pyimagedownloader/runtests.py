#!/usr/bin/env python2
#
"""Run all unit tests"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))


if __name__ == '__main__':
    import tests.savesource_test
    import tests.http_connector_test
    import tests.bellazon_test
    import tests.imagebam_test
    import tests.imageboss_test
    import tests.imagehaven_test
    import tests.imagehostorg_test
    import tests.imageshack_test
    import tests.imagetitan_test
    import tests.imageupper_test
    import tests.imgbox_test
    import tests.imgchili_test
    import tests.imgur_test
    import tests.pixroute_test
    import tests.postimage_test
    import tests.radikal_test
    import tests.servimg_test
    import tests.shareapic_test
    import tests.sharenxs_test
    import tests.skinsbe_test
    import tests.tumblr_test
    import tests.turboimagehost_test
    import tests.typepad_test
    import tests.usemycomputer_test
