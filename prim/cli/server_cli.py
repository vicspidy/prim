import os
from pprint import pprint as pp

import prim_config


def add_server(args):
    config = prim_config.get_config()
    config.setdefault('servers', dict())[args.server_name] = args.server_path
    prim_config.update_config(config)
    print('New server %s has been added successfully!' % args.server_name)

def remove_server(args):
    config = prim_config.get_config()
    if config and config.get('servers'):
        server_path = config['servers'].pop(args.server_name, None)
        if server_path:
            prim_config.update_config(config)
            print('%s server has been removed from config successfully!' % args.server_name)
        else:
            print('%s server not found in config!' % args.server_name)

def list_servers(args):
    # print(args)
    config = prim_config.get_config()
    if config.get('servers'):
        for server, path in config['servers'].items():
            print(server, path)

def build(parser):
    parser.set_defaults(func=list_servers)

    sub_parsers = parser.add_subparsers()

    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument('-n', '--name', dest='server_name', required=True)
    add_parser.add_argument('-p', '--path', dest='server_path', required=True)
    add_parser.set_defaults(func=add_server)

    remove_parser = sub_parsers.add_parser('remove')
    remove_parser.add_argument('server_name')
    remove_parser.set_defaults(func=remove_server)
    

