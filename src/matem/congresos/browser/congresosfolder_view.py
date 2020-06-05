 # -*- coding: utf-8 -*-
from plone import api
from zope.publisher.browser import BrowserView


class CongresosFolderView(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def foldercontents(self):
        brains = api.content.find(
            context=self.context,
            sort_on='start',
            sort_order='descending')
        return brains
