
'''
This module has two purposes, only:
1) Provide a console instance for the whole package.
2) Initialize the style for the command line help.
'''

from cozyconsole.consolex import ConsoleX
from rich.table import Table
from rich_argparse_plus import RichHelpFormatterPlus

from .github import LicenseInfo


console = ConsoleX()

RichHelpFormatterPlus.choose_theme('black_and_white')
RichHelpFormatterPlus.styles['argparse.args'] = 'default'
RichHelpFormatterPlus.styles['argparse.groups'] = 'bold'
RichHelpFormatterPlus.styles['argparse.help'] = 'default'
RichHelpFormatterPlus.styles['argparse.metavar'] = 'default'
RichHelpFormatterPlus.styles['argparse.syntax'] = 'bold'
RichHelpFormatterPlus.styles['argparse.text'] = 'default'
RichHelpFormatterPlus.group_name_formatter = str.title


def print_license_info(license_info: LicenseInfo, verbose: bool=True):
    '''Prints detailed license information on the SPDX ID in the
       argument.'''
    if not verbose:
        console.print(f'[b]{license_info.name}[/], '
                      f'Permissions: {", ".join(license_info.permissions)}')
        return
    table = Table(show_header=False, show_edge=False)
    table.add_column('left')
    table.add_column('right')
    if verbose:
        table.add_row('SPDX ID:', f'[b]{license_info.spdx_id}[/]')
        table.add_row('Name:', f'[b]{license_info.name}[/]')
        table.add_row('Description:', license_info.description)
        table.add_row('Implementation:', license_info.implementation)
        table.add_row('Permissions:', ', '.join(license_info.permissions))
        table.add_row('Conditions', ', '.join(license_info.conditions))
        table.add_row('Limitations:', ', '.join(license_info.limitations))
    table.add_row('HTML URL:', f'[dodger_blue1]{license_info.html_url}[/]')
    table.add_row('GitHub API URL:', f'[dodger_blue1]{license_info.url}[/]')
    table.add_row('Featured on GitHub:',
                  'Yes' if license_info.featured else 'No')
    console.print(table)


def print_license_list(licenses: list[LicenseInfo], brief: bool=False):
    '''Prints a table of the known (to GitHub) FOSS licenses.'''
    spdx_ids = sorted([x.spdx_id for x in licenses])
    if brief:
        console.print(', '.join(spdx_ids))
        return
    table = Table(show_header=True, show_edge=True)
    table.add_column('SPDX ID')
    table.add_column('License Name')
    for val in spdx_ids:
        licinfo = [x for x in licenses if x.spdx_id == val][0]
        table.add_row(licinfo.spdx_id, licinfo.name)
    console.print(table)
