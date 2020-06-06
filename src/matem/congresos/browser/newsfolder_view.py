# -*- coding: utf-8 -*-
from plone import api
from zope.publisher.browser import BrowserView


class NewsFolderView(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def foldercontents(self):
        brains = api.content.find(
            context=self.context,
            portal_type='News Item',
            sort_on='Date',
            sort_order='descending')
        return brains

