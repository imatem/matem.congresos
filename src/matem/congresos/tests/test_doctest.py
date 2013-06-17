import unittest
import doctest

from Testing import ZopeTestCase as ztc
from matem.congresos.tests import base


def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'README.txt', package='matem.congresos',
            test_class=base.FunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
        ])
