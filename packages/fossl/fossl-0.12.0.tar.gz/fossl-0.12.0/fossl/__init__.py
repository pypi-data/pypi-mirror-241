'''
Access Free Open Source License information on the command line

:copyright: (c) 2022 Ralf Luetkemeier
:license: MIT License, see LICENSE for more details.
'''

from typing import List, Tuple

from . import github


__all__ = ['get_license_info', 'get_license_text', 'LicenseNotFoundError']
__version__ = '0.12.0'


TROVE_LICENSE_NAMES = {
    'AGPL-3.0' : 'GNU Affero General Public License v3',
    'Apache-2.0' : 'Apache Software License',
    'BSD-2-Clause' : 'BSD License',
    'BSD-3-Clause' : 'BSD License',
    'BSL-1.0' : 'Boost Software License 1.0 (BSL-1.0)',
    'CC0-1.0' : 'This license is not recognized by the PyPA.',
    'EPL-2.0' : 'Eclipse Public License 2.0 (EPL-2.0)',
    'GPL-2.0' : 'GNU General Public License v2 (GPLv2)',
    'GPL-3.0' : 'GNU General Public License v3 (GPLv3)',
    'LGPL-2.1' : 'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'MIT' : 'MIT License',
    'MPL-2.0' : 'Mozilla Public License 2.0 (MPL 2.0)',
    'Unlicense' : 'The Unlicense (Unlicense)',
}


# Uses GitHub's REST API to obtain Open Source license information
# See https://developer.github.com/v3/licenses/
_URL = "https://api.github.com/licenses"
_URL_RATE_LIMIT = "https://api.github.com/rate_limit"


def get_license_info(*spdx_ids: Tuple[str]) -> List[github.LicenseInfo]:
    '''
    :param: spdx_ids
    :raises: LicenseNotFoundError
    '''
    license_info = []
    if not spdx_ids:
        for data in github.get_license_data():
            license_info.append(data)
    else:
        license_info = []
        for spdx_id in spdx_ids:
            license_data = github.get_license_details(spdx_id)
            license_info.append(license_data)
    return license_info


# def get_data_for_license(spdx_id) -> dict[str, str]


def get_license_text(spdx_id: str) -> str:
    '''Returns the license text for the SPDX ID in the argument.'''
    license_info = github.get_license_details(spdx_id)
    return license_info.body


# Additional resources:
# Fetching license types
# https://api.github.com/licenses
# Returned JSON contains a list of dicts, 'key' contains the short name for
# each license.
# https://api.github.com/licenses/{license}
# Example:
# https://api.github.com/licenses/apache-2.0
