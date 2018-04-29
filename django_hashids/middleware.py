from hashids import Hashids

from django.conf import settings

from django_hashids import GetHashids


class DjangoHashidsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.hids = GetHashids()
        return self.get_response(request)


