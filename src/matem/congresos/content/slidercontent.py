# -*- coding: utf-8 -*-
# from matem.congresos import _
from matem.congresos import congresosMessageFactory as _
# from matem.annualreport.validators import isValidFileType
# from matem.annualreport.validators import validatesinged
# from plone import api
# from plone.autoform import directives
# from plone.dexterity.content import Item
# from plone.namedfile.field import NamedBlobFile
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope import schema
# from zope.interface import implementer
# from plone import api
# from z3c.form.interfaces import IAddForm
# from zope.i18n import translate


class ISliderContent(model.Schema):
    """Dexterity-schema for activities in slider"""

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
        # defaultFactory=request_title,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    image = namedfile.NamedBlobImage(
        title=_(u'Image'),
        required=True,
    )

    urlevent = schema.URI(
        title=_(u'Url Event'),
        required=False,
    )
