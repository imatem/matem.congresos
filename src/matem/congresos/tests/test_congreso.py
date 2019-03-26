# -*- coding: utf-8 -*-
import unittest
from zope.interface.verify import verifyObject
from DateTime import DateTime
from Products.Archetypes.atapi import StringWidget
from Products.Archetypes.atapi import CalendarWidget
from Products.Archetypes.atapi import AttributeStorage
from Products.Archetypes.interfaces.layer import ILayerContainer
from Products.Archetypes.public import DisplayList
from Products.ATContentTypes.interface import IATNewsItem
from Products.ATContentTypes.permission import ChangeEvents
from Products.ATContentTypes.tests.utils import dcEdit
from Products.ATContentTypes.tests.utils import URLValidator
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName
from matem.congresos.content import Congreso
from matem.congresos.interfaces import ICongreso
from matem.congresos.tests.base import TestCase

EV_URL = 'http://example.org/'
S_DATE = DateTime()
E_DATE = DateTime() + 1
TEXT = "lorem ipsum"


def editATCT(obj):
    dcEdit(obj)
    obj.setEventUrl(EV_URL)
    obj.setStartDate(S_DATE)
    obj.setEndDate(E_DATE)
    obj.setText(TEXT)


class TestCongreso(TestCase):
    """Tests some basics of a Congreso type
    """
    klass = Congreso
    portal_type = 'Congreso'
    title = 'Congreso'
    meta_type = 'ATCongreso'
    icon = 'newsitem_icon.gif'

    def afterSetUp(self):
        self._ATCT = self._createType(self.folder, self.portal_type, 'ATCT')

    def _createType(self, context, portal_type, id, **kwargs):
        """Helper method to create a new type
        """
        ttool = getToolByName(context, 'portal_types')
        cat = self.portal.portal_catalog
        fti = ttool.getTypeInfo(portal_type)
        fti._constructInstance(context, id, **kwargs)
        obj = getattr(context.aq_inner.aq_explicit, id)
        cat.indexObject(obj)
        return obj

    def test_setup(self):
        # test if we really have the right test setup
        # portal type
        self.failUnlessEqual(self._ATCT.portal_type, self.portal_type)
        # classe
        self.failUnlessEqual(self._ATCT.__class__, self.klass)

    def test_typeInfo(self):
        ti = self._ATCT.getTypeInfo()
        self.failUnlessEqual(ti.getId(), self.portal_type)
        self.failUnlessEqual(ti.Title(), self.title)
        self.failUnlessEqual(ti.getIcon(), self.icon)
        self.failUnlessEqual(ti.Metatype(), self.meta_type)

    def test_implementsICongreso(self):
        iface = ICongreso
        self.failUnless(iface.providedBy(self._ATCT))
        self.failUnless(verifyObject(iface, self._ATCT))

    def test_implementsATNewsItem(self):
        iface = IATNewsItem
        self.failUnless(iface.providedBy(self._ATCT))
        self.failUnless(verifyObject(iface, self._ATCT))

    def test_edit(self):
        new = self._ATCT
        editATCT(new)
        url = '<a href="%s"> %s </a>' % (EV_URL, EV_URL)
        description = 'Test description <br> %s' % url
        self.failUnlessEqual(new.Description(), description)

    def test_startDateField(self):
        field = self._ATCT.getField('startDate')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 1, 'Value is %s' % field.required)
        self.failUnless(field.default == None, 'Value is %s' % str(field.default))
        self.failUnless(field.default_method == DateTime,
                        'Value is %s' % str(field.default_method))
        self.failUnless(field.searchable == False, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'start',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setStartDate',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == View,
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        ChangeEvents,
                        'Value is %s' % field.write_permission)
        self.failUnless(field.generateMode == 'veVc',
                        'Value is %s' % field.generateMode)
        self.failUnless(field.force == '', 'Value is %s' % field.force)
        self.failUnless(field.type == 'datetime', 'Value is %s' % field.type)
        self.failUnless(isinstance(field.storage, AttributeStorage),
                        'Value is %s' % type(field.storage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage(),
                        'Value is %s' % field.getLayerImpl('storage'))
        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.validators == (),
                        'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, CalendarWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(self._ATCT)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))

    def test_endDateField(self):
        dummy = self._ATCT
        field = dummy.getField('endDate')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 1, 'Value is %s' % field.required)
        self.failUnless(field.default == None, 'Value is %s' % str(field.default))
        self.failUnless(field.default_method == DateTime,
                        'Value is %s' % str(field.default_method))
        self.failUnless(field.searchable == False, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'end',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setEndDate',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == View,
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        ChangeEvents,
                        'Value is %s' % field.write_permission)
        self.failUnless(field.generateMode == 'veVc',
                        'Value is %s' % field.generateMode)
        self.failUnless(field.force == '', 'Value is %s' % field.force)
        self.failUnless(field.type == 'datetime', 'Value is %s' % field.type)
        self.failUnless(isinstance(field.storage, AttributeStorage),
                        'Value is %s' % type(field.storage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage(),
                        'Value is %s' % field.getLayerImpl('storage'))
        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.validators == (),
                        'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, CalendarWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))

    def test_eventUrlField(self):
        dummy = self._ATCT
        field = dummy.getField('eventUrl')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'event_url',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setEventUrl',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == View,
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        ChangeEvents,
                        'Value is %s' % field.write_permission)
        self.failUnless(field.generateMode == 'veVc',
                        'Value is %s' % field.generateMode)
        self.failUnless(field.force == '', 'Value is %s' % field.force)
        self.failUnless(field.type == 'string', 'Value is %s' % field.type)
        self.failUnless(isinstance(field.storage, AttributeStorage),
                        'Value is %s' % type(field.storage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage(),
                        'Value is %s' % field.getLayerImpl('storage'))
        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnlessEqual(field.validators, URLValidator)
        self.failUnless(isinstance(field.widget, StringWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))

    def test_indexed_dates(self):
        cat = self.portal.portal_catalog
        self._ATCT.edit(startDate=S_DATE, endDate=E_DATE)
        brains = cat(start=S_DATE, end=E_DATE)
        self.failUnlessEqual(len(brains), 1)
        self.failUnlessEqual(brains[0].getObject().UID(), self._ATCT.UID())
#TODO: para prueba de vista ver Products.ATContentTypes.tests.test_atevent.py


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCongreso))
    return suite
