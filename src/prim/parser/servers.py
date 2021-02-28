import os
from pprint import pprint

import prim


def show_servers():
    config = prim.get_config()
    for server in config['servers']:
        print '%s - %s' % (server['name'], server['path'])