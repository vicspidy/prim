import sys
import os
import yaml
import argparse

from . import server_cli

def add_default_args(parser):
    parser.add_argument('-v', '--verbose', dest='verbose', action='count')

parser = argparse.ArgumentParser(prog='prim', description='Helps you manage your pipeline...')
sub_parsers = parser.add_subparsers(dest='subparser')

server_parser = sub_parsers.add_parser('server', help='helps to maintain servers and its configuration')
add_default_args(server_parser)
server_cli.build(server_parser)


# # servers show parser
# servers_show_parser = servers_sub_parsers.add_parser('show', help='shows list of servers for Prim')
# servers_show_parser.set_defaults(func=servers.show_servers)

