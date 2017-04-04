# -*- coding: utf-8 -*-
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from zope.component.hooks import getSite


class SemanaryCongressView(BrowserView):

    def __init__(self, context, request):
        """Initialize view."""
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        """."""
        return getToolByName(getSite(), 'portal_catalog')

    def semanaryCongress(self):
        ftoday = DateTime()
        today = DateTime('/'.join([str(ftoday.year()), str(ftoday.month()), str(ftoday.day())]))
        start_date = today + 1
        end_date = today + 7.9999

        iso_start = start_date.ISO().split('-')
        day_start = iso_start[2].split('T')

        iso_end = end_date.ISO().split('-')
        day_end = iso_end[2].split('T')

        return {
            'activities': [],
            'start_date': '/'.join([day_start[0], iso_start[1], iso_start[0]]),
            'end_date': '/'.join([day_end[0], iso_end[1], iso_end[0]]),
        }
