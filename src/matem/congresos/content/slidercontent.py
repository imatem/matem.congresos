# -*- coding: utf-8 -*-
from matem.congresos import _
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


class SliderContent(model.Schema):
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
        title=_(u'ImageThumb'),
        required=True,
    )

    urlevent = schema.TextLine(
        title=_(u'Url event'),
        required=False,
    )
