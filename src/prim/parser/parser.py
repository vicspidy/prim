import sys
import os
import yaml
import argparse

import prim

from . import servers

parser = argparse.ArgumentParser(description='Helps you manage your pipeline...')
sub_parsers = parser.add_subparsers()

# servers parser
servers_parser = sub_parsers.add_parser('servers', help='helps to maintain servers for Prim')
servers_sub_parsers = servers_parser.add_subparsers()
# servers_parser.add_argument('-s', '--show', action='store_true', help='shows list of servers added to prim')
# servers_parser.add_argument('-u', '--update', action='store', nargs=2, help='shows list of servers added to prim')
# servers_parser.set_defaults(func=_servers)

# servers show parser
servers_show_parser = servers_sub_parsers.add_parser('show', help='shows list of servers for Prim')
servers_show_parser.set_defaults(func=servers.show_servers)

