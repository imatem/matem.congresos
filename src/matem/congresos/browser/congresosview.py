# -*- coding: utf-8 -*-
from Products.Five import BrowserView


class congresosView(BrowserView):
    """
    congresos browser view
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
