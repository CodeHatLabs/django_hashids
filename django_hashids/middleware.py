import hashids

from django.conf import settings

from pygwanda.helpers import UNAMBIGUOUS_UPPER


class DjangoHashidsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.hid = hashids.Hashids(
            getattr(settings, 'DJANGO_HASHIDS_SALT', settings.SECRET_KEY),
            getattr(settings, 'DJANGO_HASHIDS_MIN_LENGTH', 36),
            getattr(settings, 'DJANGO_HASHIDS_CHARSET', UNAMBIGUOUS_UPPER)
            )
        return self.get_response(request)


