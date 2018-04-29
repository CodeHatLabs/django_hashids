from hashids import Hashids

from django.conf import settings


class DjangoHashidsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.hid = Hashids(
            getattr(settings, 'DJANGO_HASHIDS_SALT', settings.SECRET_KEY),
            getattr(settings, 'DJANGO_HASHIDS_MIN_LENGTH', 0),
            getattr(settings, 'DJANGO_HASHIDS_CHARSET', Hashids.ALPHABET)
            )
        return self.get_response(request)


