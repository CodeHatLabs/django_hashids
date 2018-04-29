from uuid import UUID


class DjangoHashidsViewMixin(object):

    hidargs = {}

    def decode_hashids(self, kwargs):
        for argkey, argtype in self.hidargs.items():
            arg = self.request.hid.decode(kwargs[argkey])[0]
            if argtype == 'uuid':
                arg = UUID(int=arg)
            elif argtype == 'uuidhex':
                arg = UUID(int=arg).hex
            elif argtype == 'uuidstr':
                arg = str(UUID(int=arg))
            kwargs[argkey] = arg

    def dispatch(self, request, *args, **kwargs):
        self.decode_hashids(kwargs)
        return super().dispatch(request, *args, **kwargs)


