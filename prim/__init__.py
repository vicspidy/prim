# import sys
# import os
# import glob

# import yaml


# from prim.exceptions import *
# import prim.io as io

# __all__ = ['PRIM_CONFIG', 'get_config']

# # environment variable that prim looks for
# PRIM_ROOT_VARNAME = 'PRIM_ROOT'

# # Prim file names
# PRIM_CONFIG_FILE_NAME = 'prim_config'

# # initialize variables
# PRIM_ROOT_PATH = os.getenv(PRIM_ROOT_VARNAME)
# PRIM_CONFIG = None


# # initialize Prim
# if not PRIM_ROOT_PATH:
#     raise PrimRootNotSetError
# PRIM_CONFIG = get_config()