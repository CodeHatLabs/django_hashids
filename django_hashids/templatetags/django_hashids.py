from uuid import UUID

from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def hashid(context, arg, argtype=None):
    arg = UUID(arg).int if argtype == 'uuid' else int(arg)
    return context['view'].request.hid.encode(arg)


