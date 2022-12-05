#!/usr/bin/env python3

""" Boilerplate package with example numerical tests. """


import sys
import logging
import argparse
from timeit import default_timer
from number_test import __version__
from .number_test import prime


def parseArgs() -> argparse.Namespace:
    epilog = 'Stephen Richer, (stephen.richer@proton.me)'
    baseParser = _getBaseParser(__version__)
    parser = argparse.ArgumentParser(
        epilog=epilog, description=__doc__, parents=[baseParser])
    
    parser.add_argument(
        'number', nargs='?', type=int, default=42,
        help='A number to test primality (default: %(default)s)')
    parser.set_defaults(function=prime_cli)

    args = parser.parse_args()
    if 'function' not in args:
        parser.print_help()
        sys.exit()

    return _executeCommand(args)


def _executeCommand(args):
    # Initialise logging
    logFormat = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level=args.verbose, format=logFormat)
    del args.verbose
    # Pop main function and excute script
    function = args.__dict__.pop('function')
    start = default_timer()
    rc = function(**vars(args))
    end = default_timer()
    logging.info(f'Total execution time: {end - start:.3f} seconds.')
    logging.shutdown()
    return rc


def _getBaseParser(version: str) -> argparse.Namespace:
    """ Create base parser of verbose/version. """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '--version', action='version', version='%(prog)s {}'.format(version))
    parser.add_argument(
        '--verbose', action='store_const', const=logging.DEBUG,
        default=logging.ERROR, help='verbose logging for debugging')
    return parser


def prime_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if prime(number):
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not prime number!')


