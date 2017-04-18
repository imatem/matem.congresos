# -*- coding: utf-8 -*-
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from zope.component.hooks import getSite
import datetime


class SemanaryCongressView(BrowserView):

    def __init__(self, context, request):
        """Initialize view."""
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        """."""
        return getToolByName(getSite(), 'portal_catalog')

    def getNextFriday(self):
        today = datetime.date.today()  # DateTime()
        friday = today + datetime.timedelta((4 - today.weekday()) % 7)
        return friday

    def semanaryCongress(self):
        ftoday = self.getNextFriday()
        today = DateTime('/'.join([str(ftoday.year), str(ftoday.month), str(ftoday.day)]))
        # ftoday = DateTime()
        # today = DateTime('/'.join([str(ftoday.year()), str(ftoday.month()), str(ftoday.day())]))

        start_date = today + 1
        end_date = today + 7.9999

        iso_start = start_date.ISO().split('-')
        day_start = iso_start[2].split('T')

        iso_end = end_date.ISO().split('-')
        day_end = iso_end[2].split('T')

        query = {
            'portal_type': 'Congreso',
            # 'end': {'query': [start_date, ], 'range': 'min'},
            # 'start': {'query': [end_date, ], 'range': 'max'},
            'review_state': 'frontpage_published',
            'sort_on': 'start',

        }

        brains = self.portal_catalog.searchResults(query)
        congress = []
        for brain in brains:
            obj = brain.getObject()
            dates = obj.getSemanarydates()
            for itemdates in dates:
                itemdate = itemdates.get('semdate', '')
                data = {}
                if itemdate:
                    effectivedate = DateTime(itemdate, datefmt='MX')
                    if effectivedate >= start_date and effectivedate <= end_date:
                        title = obj.Title()
                        dstart = obj.start()
                        dend = obj.end()
                        place = obj.getEventplace()
                        url = obj.event_url()
                        if title:
                            data['title'] = title
                        if dstart:
                            data['start'] = '/'.join([str(dstart.day()), str(dstart.month()), str(dstart.year())])
                        if dend:
                            data['end'] = '/'.join([str(dend.day()), str(dend.month()), str(dend.year())])
                        if place:
                            data['place'] = place
                        if url:
                            data['url'] = url
                        congress.append(data)
                        break

        return {
            'congress': congress,
            'start_date': '/'.join([day_start[0], iso_start[1], iso_start[0]]),
            'end_date': '/'.join([day_end[0], iso_end[1], iso_end[0]]),
        }
