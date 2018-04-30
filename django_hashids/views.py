from uuid import UUID


class DjangoHashidsViewMixin(object):

    hidargs = {}

    def decode_hashids(self, request, kwargs):
        for argkey, argtype in self.hidargs.items():
            arg = request.hids.decode(kwargs[argkey])[0]
            if argtype == 'uuid':
                arg = UUID(int=arg)
            elif argtype == 'uuidhex':
                arg = UUID(int=arg).hex
            elif argtype == 'uuidstr':
                arg = str(UUID(int=arg))
            kwargs[argkey] = arg
        self.on_hashids_decoded(request, kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.decode_hashids(request, kwargs)
        return super().dispatch(request, *args, **kwargs)

    def on_hashids_decoded(self, request, kwargs):
        pass


