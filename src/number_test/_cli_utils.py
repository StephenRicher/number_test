#!/usr/bin/env python3

import sys
import argparse


class OptionsParser():
    def __init__(self, argv: list[str] | None = None,
                 epilog: str = '', version: str = ''):
        self.argv = argv
        self.epilog = epilog
        self.base_parser = self._get_base_parser(version)

    def _prepare_subparser(self) -> tuple[argparse.ArgumentParser, argparse._SubParsersAction]:
        parser = self._prepare_parser()
        subparser = self._get_subparser(parser)
        self.subparser = True
        return parser, subparser

    def _prepare_parser(self) -> argparse.ArgumentParser:
        """ Create base parser of verbose/version. """
        parser = argparse.ArgumentParser(
            epilog=self.epilog, description=__doc__,
            parents=[self.base_parser])
        return parser

    def _get_base_parser(self, version: str) -> argparse.ArgumentParser:
        """ Create base parser of verbose/version. """
        base_parser = argparse.ArgumentParser(add_help=False)
        base_parser.add_argument(
            '--version', action='version', version=f'%(prog)s {version}')
        base_parser.add_argument(
            '--verbose', action='count',
            default=0, help='verbose logging for debugging')
        return base_parser

    def _get_subparser(self, parser: argparse.ArgumentParser
                       ) -> argparse._SubParsersAction:
        subparser = parser.add_subparsers(
            title='required commands',
            description='',
            dest='command',
            metavar='Commands',
            help='Description:')
        return subparser

    def _validate_subcommand(self, args: argparse.Namespace,
                             parser: argparse.ArgumentParser) -> None:
        if (self.subparser) and ('function' not in args):
            parser.print_help()
            sys.exit()


class IntRange:
    def __init__(self, imin: int | None = None, imax: int | None = None):
        self.imin = imin
        self.imax = imax

    def __call__(self, arg: str):
        try:
            value = int(arg)
        except ValueError:
            raise self.exception()
        if ((self.imin is not None and value < self.imin)
                or (self.imax is not None and value > self.imax)):
            raise self.exception()
        return value

    def exception(self):
        if self.imin is not None and self.imax is not None:
            return argparse.ArgumentTypeError(
                f'Must be an integer in the range [{self.imin}, {self.imax}].')
        elif self.imin is not None:
            return argparse.ArgumentTypeError(
                f'Must be an integer >= {self.imin}.')
        elif self.imax is not None:
            return argparse.ArgumentTypeError(
                f'Must be an integer <= {self.imax}.')
        else:
            return argparse.ArgumentTypeError('Must be an integer.')
