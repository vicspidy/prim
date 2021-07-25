import os, sys

import yaml

import ios
import errors


# ------------------------------------------ Exceptions ----------------------------------------------------
class ConfigPathNotDefined(errors.PrimError):
    def __init__(self, message=None):
        if not message: message = 'Config path not defined! Please set "PRIM_CONFIG_PATH" to locate configuration file for prim!'
        super().__init__(message)


class ConfigFileNotFound(errors.PrimError):
    def __init__(self, message=None):
        if not message: message = 'Config file not found! Please contact pipeline!'
        super().__init__(message)


class CorruptConfigFileError(errors.PrimError):
    def __init__(self, message=None):
        if not message: message = 'Prim config file is corrupt! Please contact pipeline!'
        super().__init__(message)

# -----------------------------------------------------------------------------------------------------------

def _load_config(path):
    with open(path, 'r') as fid:
        try:
            config = yaml.safe_load(fid)
        except yaml.YAMLError as err:
            raise CorruptConfigFileError(err)
        else:
            if not config: config = dict()
    return config
                
# ---------------------------------- CONSTANTS -------------------------------------------
PRIM_CONFIG_PATH = os.getenv('PRIM_CONFIG_PATH')
if not PRIM_CONFIG_PATH: raise ConfigPathNotDefined

PRIM_CONFIG_FILE = ios.ls(PRIM_CONFIG_PATH, regex=r'config.ya?ml')
if PRIM_CONFIG_FILE:
    PRIM_CONFIG_FILE = os.path.join(PRIM_CONFIG_PATH, PRIM_CONFIG_FILE[0])
else:
    raise ConfigFileNotFound

PRIM_CONFIG = _load_config(PRIM_CONFIG_FILE)

# --------------------------------- PUBLIC FUNCTIONS -----------------------------------------

def get_config(reload=False):
    global PRIM_CONFIG
    if not PRIM_CONFIG or reload:
        PRIM_CONFIG = _load_config(PRIM_CONFIG_FILE)

    return PRIM_CONFIG


def update_config(config):
    with open(PRIM_CONFIG_FILE, 'w') as fid:
        yaml.dump(config, fid)