# -*- coding: utf-8 -*-
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

from matem.congresos import congresosMessageFactory as _
from matem.congresos.interfaces import ICongreso
from matem.congresos.config import PROJECTNAME

from Products.DataGridField import DataGridField
from Products.DataGridField import DataGridWidget
from collective.datagridcolumns.DateColumn import DateColumn



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

    StringField('eventplace',
                required=False,
                searchable=False,
                # accessor='event_url',
                write_permission=ChangeEvents,
                # validators=('isURL', ),
                widget=StringWidget(
                    description=_(u'help_event_place', default=u"Indicate the Event place"),
                    label=_(u'label_event_place', default=u'Event Place'),
                    i18n_domain='matem.congresos',
                )),

    DataGridField(
        name='semanarydates',
        columns=('semdate',),
        write_permission=ChangeEvents,
        allow_reorder=False,
        widget=DataGridWidget(
            label=_(u"label_widget_semanarydates", default=u"Dates for include in the semanary"),
            i18n_domain='matem.congresos',
            helper_js=('datagridwidget.js', 'datagridwidget_patches.js', 'datagriddatepicker.js',),
            helper_css=('datagridwidget.css', 'congresos.css',),
            columns={
                'semdate': DateColumn(
                    _(u"semanarydate_label", default=u"Date for include in the semanary <dd/mm/yyyy>, Be careful the date is consider for the semanary"),
                    date_format='dd/mm/yy',
                ),
            },
        ),
        default=({'semdate': ''}, ),
    ),



))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CongresoSchema['title'].storage = atapi.AnnotationStorage()
CongresoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CongresoSchema, moveDiscussion=False)

CongresoSchema.moveField('startDate', after='description')
CongresoSchema.moveField('endDate', after='startDate')
CongresoSchema.moveField('eventUrl', after='endDate')
CongresoSchema.moveField('eventplace', after='eventUrl')
CongresoSchema.moveField('semanarydates', after='eventplace')


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

    def post_validate(self, REQUEST=None, errors=None):

        rstartDate = REQUEST.get('startDate', None)
        rendDate = REQUEST.get('endDate', None)

        try:
            end = DateTime(rendDate)
        except Exception:
            errors['endDate'] = u'La fecha de término no es valida'

        try:
            start = DateTime(rstartDate)
        except Exception:
            errors['startDate'] = u'La fecha de inicio no es valida'

        if 'startDate' in errors or 'endDate' in errors:
            return

        if start > end:
            errors['endDate'] = u'La fecha de término debe ser posterior a la de inicio'


atapi.registerType(Congreso, PROJECTNAME)
