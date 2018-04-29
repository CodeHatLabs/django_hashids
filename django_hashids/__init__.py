from hashids import Hashids


def GetHashids():
    from django.conf import settings
    return Hashids(
        getattr(settings, 'DJANGO_HASHIDS_SALT', settings.SECRET_KEY),
        getattr(settings, 'DJANGO_HASHIDS_MIN_LENGTH', 0),
        getattr(settings, 'DJANGO_HASHIDS_CHARSET', Hashids.ALPHABET)
        )


