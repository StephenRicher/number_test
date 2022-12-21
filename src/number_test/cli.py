#!/usr/bin/env python3

""" Boilerplate package with example numerical tests. """


import sys
import argparse
from number_test import __version__
from ._cli_utils import _executeCommand, _getBaseParser
from .number_test import prime, fibonacci


def parseArgs() -> argparse.Namespace:
    epilog = 'Stephen Richer, (stephen.richer@proton.me)'
    baseParser = _getBaseParser(__version__)
    parser = argparse.ArgumentParser(
        epilog=epilog, description=__doc__, parents=[baseParser])
    
    subparser = parser.add_subparsers(
        title='required commands',
        description='',
        dest='command',
        metavar='Commands',
        help='Description:')
    # HINT: Add your each subcommand and arguments to a new subparser.
    # HINT: Refer to https://docs.python.org/3/library/argparse.html
    sp1 = subparser.add_parser(
        'prime',
        description=prime_cli.__doc__.split('\n')[0],
        help='Check if a number is prime.',
        parents=[baseParser],
        epilog=parser.epilog)
    # HINT: Add (default: %(default)s)') to help message if you have a default.
    sp1.add_argument('number', type=int, help='A number to test primality.')
    # HINT: For each subcommand, define an entry-point function.
    sp1.set_defaults(function=prime_cli)

    # HINT: Create a new sub-parser with disctinct arguments.
    sp2 = subparser.add_parser(
        'fib',
        description=fibonacci_cli.__doc__.split('\n')[0],
        help='Check if a number is part of the fibonacci sequence.',
        parents=[baseParser],
        epilog=parser.epilog)
    sp2.add_argument('number', type=int, help='A number to check.')
    sp2.set_defaults(function=fibonacci_cli)
    
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


def fibonacci_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if fibonacci(number):
        print(f'{number} is part of the fibonacci sequence!')
    else:
        print(f'{number} is not part of the fibonacci sequence!')


