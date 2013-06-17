import unittest

from matem.congresos.tests.base import TestCase


class TestInstall(TestCase):
    """ensure product is properly installed"""

    def test_types(self):
        t = 'Congreso'
        self.failUnless(t in self.portal.portal_types.objectIds(),
                            '%s content type not installed' % t)

    def test_skin_installed(self):
        skin_layer = 'matem_congresos'
        self.failUnless(skin_layer in self.portal.portal_skins.objectIds(),
                            '%s not in skins' % skin_layer)


class TestUninstall(TestCase):
    """ensure product is properly uninstalled"""

    def afterSetUp(self):
        self.loginAsPortalOwner()
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=['matem.congresos'])

    def test_product_uninstalled(self):
        self.failIf(self.qi.isProductInstalled('matem.congresos'))

    def test_skin_uninstalled(self):
        skin_layer = 'matem_congresos'
        self.failIf(skin_layer in self.portal.portal_skins.objectIds())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestInstall))
    suite.addTest(unittest.makeSuite(TestUninstall))
    return suite
