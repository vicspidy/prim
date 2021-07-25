import argparse

from . import cli


def parse_args():
    args = cli.parser.parse_args()
    # print('args -- ', args)
    args.func(args)
