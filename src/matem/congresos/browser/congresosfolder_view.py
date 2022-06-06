 # -*- coding: utf-8 -*-
from plone import api
from zope.publisher.browser import BrowserView

from DateTime import DateTime


class CongresosFolderView(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.range = 'min'

    def foldercontents(self):
        folders = api.content.find(
            depth=1,
            context=self.context,
            portal_type='Folder')
        if folders:
            brains = api.content.find(
                context=self.context,
                portal_type='Congreso',
                start={'query':DateTime('%s/01/01 00:00:00 UTC' % self.current_year()), 'range': self.range},
                sort_on='start',
                sort_order='descending')
            return brains

        brains = api.content.find(
            context=self.context,
            portal_type='Congreso',
            sort_on='start',
            sort_order='descending')
        return brains

    def eventplace(self, congress):
        try:
            return congress.eventplace
        except AttributeError :
            return None


    def canedit(self, congress):
        if not api.user.is_anonymous():
            current = api.user.get_current()
            return api.user.has_permission('Edit', username=current.id, obj=congress)
        return False

    def current_year(self):
        return DateTime().year()


    def link(self, item):
        return item.eventUrl 


class CongresosPreviousView(CongresosFolderView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.range = 'max'
