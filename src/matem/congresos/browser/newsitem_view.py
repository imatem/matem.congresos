 # -*- coding: utf-8 -*-
import urllib

from zope.component import getMultiAdapter
from zope.interface import implements
from zope.interface import alsoProvides
from zope.i18n import translate
from zope.publisher.browser import BrowserView

from AccessControl import Unauthorized
from Acquisition import aq_parent, aq_inner
from OFS.interfaces import IOrderedContainer
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import safe_unicode
from Products.CMFPlone.utils import pretty_title_or_id, isExpired

from plone.app.content.browser.interfaces import IContentsPage
from plone.app.content.browser.tableview import Table, TableBrowserView

class NewsItemView(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}
