''' CLI Parser

Module of tarpy.
Usage:
    tarpy [ROOT] [TARGET] -m {'w', 'e'} [--exclude_file] [--compression]

'''

import argparse
from typing import Any
from tarpy.tarhandler import TarArchive


def cliparser() -> Any:
    ''' CLI Parser

    Function takes parameters like defined below and
    returns the args.
    '''
    parser = argparse.ArgumentParser(
            description = 'Different TAR Archive operations.',
            epilog = 'Python3 version.',
            )
    parser.add_argument(
            'ROOT',
            type=str,
            help='The (starting) directory to archive respectively the file to extract.'
            )
    parser.add_argument(
            'TARGET',
            type=str,
            help='The path where archive will be written to.'
            )
    parser.add_argument(
            '-m',
            choices=['w', 'e'],
            help = 'Which Operation to run.'
            )

    parser.add_argument(
            '-ex-f',
            '--exclude-file',
            metavar='PATH',
            help='File with exclusions defined.'
            )

    parser.add_argument(
            '-c',
            '--compression',
            default='gz',
            choices=['gz', 'bz', 'lz'],
            help='The compression method.'
            )

    return parser.parse_args()

def cli() -> Any:
    ''' Core function of CLI
    '''
    args = cliparser()

    root = args.ROOT
    target = args.TARGET
    mode = args.m

    # Default Variables.
    ex_file = args.exclude_file
    compression = args.compression

    handler = TarArchive(root, target, ex_file, compression)
    print(handler)
    return handler(mode)


if __name__ == '__main__':

    # cli()
    print(cli.__annotations__)
