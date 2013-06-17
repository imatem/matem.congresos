from Products.Archetypes.atapi import DateTimeField
from Products.Archetypes.atapi import StringWidget
from Products.Archetypes.atapi import CalendarWidget
from Products.ATContentTypes.permission import ChangeEvents
from DateTime import DateTime
from Products.Archetypes.atapi import StringField
"""Definition of the Congreso content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import newsitem
from Products.ATContentTypes import ATCTMessageFactory as _
from matem.congresos.interfaces import ICongreso
from matem.congresos.config import PROJECTNAME

CongresoSchema = newsitem.ATNewsItemSchema.copy() + atapi.Schema((
    DateTimeField('startDate',
                  required=True,
                  searchable=False,
                  accessor='start',
                  write_permission=ChangeEvents,
                  default_method=DateTime,
                  languageIndependent=True,
                  widget=CalendarWidget(
                        description='',
                        label=_(u'label_event_start', default=u'Event Starts'),
                        show_hm=False,
                        )),

    DateTimeField('endDate',
                  required=True,
                  searchable=False,
                  accessor='end',
                  write_permission=ChangeEvents,
                  default_method=DateTime,
                  languageIndependent=True,
                  widget=CalendarWidget(
                        description = '',
                        label = _(u'label_event_end', default=u'Event Ends'),
                        show_hm=False,
                        )),

    StringField('eventUrl',
                required=False,
                searchable=True,
                accessor='event_url',
                write_permission = ChangeEvents,
                validators=('isURL', ),
                widget = StringWidget(
                        description = _(u'help_event_url',
                                        default=u"Web address with more info about the event. "
                                            "Add http:// for external links."),
                        label = _(u'label_event_url', default=u'Event URL'),
                        )),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CongresoSchema['title'].storage = atapi.AnnotationStorage()
CongresoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CongresoSchema, moveDiscussion=False)

CongresoSchema.moveField('startDate', after='description')
CongresoSchema.moveField('endDate', after='startDate')
CongresoSchema.moveField('eventUrl', after='endDate')


class Congreso(newsitem.ATNewsItem):
    """Enlace con imagen"""
    implements(ICongreso)

    meta_type = "ATCongreso"
    schema = CongresoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    url = atapi.ATFieldProperty('meetingUrl')

    def Description(self):
        if not self.event_url():
            return self.description
        url = '<a href="%s"> %s </a>' % (self.event_url(), self.event_url())
        return '%s <br/> %s' % (self.description, url)

atapi.registerType(Congreso, PROJECTNAME)
