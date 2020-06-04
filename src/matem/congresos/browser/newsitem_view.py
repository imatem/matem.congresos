 # -*- coding: utf-8 -*-
from zope.publisher.browser import BrowserView


class NewsItemView(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def image_class(self):
        """ return wheter image is wider or taller
        """
        image = self.context.getImage()
        if image is None:
            return
        if image.width < image.height:
            return 'newsImageContainer img-higher'
        return 'newsImageContainer img-wider'
