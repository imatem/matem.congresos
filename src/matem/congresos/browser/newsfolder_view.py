# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.PloneBatch import Batch
from zope.publisher.browser import BrowserView


class NewsFolderView(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def foldercontents(self, b_size, b_start):
        brains = api.content.find(
            context=self.context,
            portal_type='News Item',
            sort_on='Date',
            sort_order='descending')
        batch = Batch(brains, b_size or 20, int(b_start), orphan=0)
        return batch
