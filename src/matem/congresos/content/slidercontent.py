# -*- coding: utf-8 -*-
from matem.congresos import congresosMessageFactory as _
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope import schema

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
