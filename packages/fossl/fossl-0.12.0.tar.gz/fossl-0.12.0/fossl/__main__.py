#!/usr/bin/env python3

'''
This script makes the functionality in the fossl module available
on the command line.

Usage:

% fossl list
<list of known FOSS licenses and brief summaries>
% fossl show apache-2.0
<details on the Apache 2.0 license>
% fossl show apache-2.0 -text
<text of the Apache 2.0 license>
% fossl show -text apache-2.0
<text of the Apache 2.0 license>

'''

import argparse

from rich_argparse_plus import RichHelpFormatterPlus

from . import get_license_info, get_license_text
from .console import console, print_license_info, print_license_list
from .github import LicenseNotFoundError, GitHubApiRateLimitExceeded

def on_list_licenses(options=None):
    '''
    Lists the Open Source licenses available through the GitHub REST API
    '''
    licenses = get_license_info()
    print_license_list(licenses, options.brief)


def on_show_license(options):
    '''
    Shows license information

    :param: options, these are the arguments from the command line
    '''
    if options.text:
        license_text = get_license_text(options.spdx_id)
        print(license_text, end='')
    else:
        license_info = get_license_info(options.spdx_id)[0]
        print_license_info(license_info, verbose=not options.short)


def parse_args(main_parser):
    '''
    Configures the command line interface
    '''
    main_parser.description = ('Obtains information on various Open Source '
                               'licenses using the GitHub REST API.')
    main_parser.formatter_class = RichHelpFormatterPlus
    sub_parsers = main_parser.add_subparsers(
        metavar='COMMAND',
        help='[u]Description[/]',
        dest='subcommand'
    )

    list_parser = sub_parsers.add_parser(
        name='list',
        description='List the Open Source licenses which are available '
                    'via the GitHub REST API.',
        help='show the Open Source licenses available on GitHub',
        epilog=('SPDX: Software Package Data eXchange, '
                'see [dodger_blue1]https://spdx.org/licenses/[/] '
                'and [dodger_blue1]https://spdx.dev/ids/[/].'),
        formatter_class=RichHelpFormatterPlus,
    )
    list_parser.add_argument(
        '-b', '--brief',
        action='store_true',
        default=False,
        help='list only the SPDX IDs of the licenses'
    )

    show_parser = sub_parsers.add_parser(
        name='show',
        description='Display information on the specified license.',
        help='display information on the selected license',
        epilog=list_parser.epilog,
        formatter_class=RichHelpFormatterPlus,
    )
    show_parser.add_argument(
        'spdx_id',
        help='the SPDX ID of the license'
    )
    group = show_parser.add_mutually_exclusive_group()
    group.add_argument(
        '-full',
        action='store_true',
        default=False,
        help='show all license information except for the text of the license'
    )
    group.add_argument(
        '-short',
        action='store_true',
        default=False,
        help='show just the license name and its permissions'
    )
    group.add_argument(
        '-text',
        action='store_true',
        default=False,
        help='show the full text of the license'
    )

    list_parser.set_defaults(func=on_list_licenses)
    show_parser.set_defaults(func=on_show_license)

    return main_parser.parse_args()


def main():
    '''A docstring to please pylint.'''

    parser = argparse.ArgumentParser()
    args   = parse_args(parser)

    if not args.subcommand:
        parser.print_usage()
        return

    try:
        args.func(args)
    except LicenseNotFoundError as lic:
        console.print(f'Unkown license [b]{lic.spdx_id}')
    except GitHubApiRateLimitExceeded as rate:
        console.print(rate)


if __name__ == "__main__":
    main()
