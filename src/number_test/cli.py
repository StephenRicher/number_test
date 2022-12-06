#!/usr/bin/env python3

""" Boilerplate package with example numerical tests. """


import sys
import argparse
from number_test import __version__
from ._cli_utils import _executeCommand, _getBaseParser
from .number_test import prime


def parseArgs() -> argparse.Namespace:
    epilog = 'Stephen Richer, (stephen.richer@proton.me)'
    baseParser = _getBaseParser(__version__)
    parser = argparse.ArgumentParser(
        epilog=epilog, description=__doc__, parents=[baseParser])
    
    # HINT: Add your command-line arguments here.
    # HINT: Add (default: %(default)s)') to help message if you have a default.
    # HINT: Refer to https://docs.python.org/3/library/argparse.html
    parser.add_argument('number', type=int, help='A number to test primality')
    # HINT: Define an entry-point function to pass command-line arguments.
    parser.set_defaults(function=prime_cli)
    args = parser.parse_args()
    if 'function' not in args:
        parser.print_help()
        sys.exit()

    return _executeCommand(args)

# HINT: CLI entry-point function which takes command-line arguments.
def prime_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if prime(number):
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not prime number!')


