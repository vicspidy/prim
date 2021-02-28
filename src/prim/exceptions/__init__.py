from prim import *

class PrimRootNotSetError(Exception):
    def __init__(self):
        self.message = 'No Prim root path found!\nPlease set ' \
            'environment variable \'%s\' to point to Prim root.' % PRIM_ROOT_VARNAME
        super(PrimRootNotSetError, self).__init__(self.message)

class PrimConfigNotFound(Exception):
    def __init__(self):
        self.message = 'Prim config file doesn\' exists!'
        super(PrimConfigNotFound, self).__init__(self.message)