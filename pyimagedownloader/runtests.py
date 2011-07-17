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
