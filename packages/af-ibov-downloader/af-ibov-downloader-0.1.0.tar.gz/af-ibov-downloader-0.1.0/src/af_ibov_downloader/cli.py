"""
This module contains the main CLI code.
"""
import sys
import argparse

from . import handlers, errors


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='available sub-commands')

parser_global = argparse.ArgumentParser(add_help=False)
parser_global.add_argument('--output', '-o', type=str, choices=['text', 'json'], default='text')

parser_version = subparsers.add_parser('version', help='shows program version', parents=[parser_global])
parser_version.set_defaults(_handler=handlers.version)

parser_download = subparsers.add_parser('download', help='downloads ibovespa archives', parents=[parser_global])
parser_download.add_argument('--years', type=str, default=','.join([str(i) for i in range(1986, 2022)]),
    help='years to download, comma separated, downloads all if no value is provides')
parser_download.add_argument('--dest', '-d', type=str, required=True, help='folder to download archives to')
parser_download.add_argument('--workers', '-w', type=int, help='The maximum amount of workers to use')
parser_download.add_argument('--extract', '-e', action='store_true', help='extracts zip file after download')
parser_download.set_defaults(_handler=handlers.download)


def run(*args: str, **kwargs: str) -> str:
    """
    Run ArgumentParser and returns a string
    containing the command result.
    """
    ns = parser.parse_args(*args, **kwargs)
    params = {k:v for k,v in vars(ns).items() if k != '_handler'}
    return str(ns._handler(**params))


def main(*args: str, **kwargs: str) -> None:
    """
    Prints result of ArgumentParser to stdout.

    Writes a str containing `errors.AFError'
    to stderr in case of an error.
    """
    try:
        print(run(*args, **kwargs))
    except errors.AFError as e:
        sys.stderr.write(f'{e}\n')
        sys.exit(e.code)

