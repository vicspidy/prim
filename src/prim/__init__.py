import sys
import os
import glob

import yaml

from prim.exceptions import *
import prim.io as io

__all__ = ['PRIM_CONFIG', 'get_config']

# environment variable that prim looks for
PRIM_ROOT_VARNAME = 'PRIM_ROOT'

# Prim file names
PRIM_CONFIG_FILE_NAME = 'prim_config'

# initialize variables
PRIM_ROOT_PATH = os.getenv(PRIM_ROOT_VARNAME)
PRIM_CONFIG = None

def get_config():
    global PRIM_CONFIG
    if not PRIM_CONFIG:
        config_file = io.ls(PRIM_ROOT_PATH, '%s\.y[a]?ml' % PRIM_CONFIG_FILE_NAME)
        if config_file:
            with open(config_file[0], 'r') as f:
                PRIM_CONFIG = yaml.safe_load(f)
        else:
            raise PrimConfigNotFound
    return PRIM_CONFIG


# initialize Prim
if not PRIM_ROOT_PATH:
    raise PrimRootNotSetError
PRIM_CONFIG = get_config()
