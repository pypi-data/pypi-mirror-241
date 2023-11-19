
import sys
import pytest

from rich.text import Text

import fossl

from fossl import github
from fossl.__main__ import main


def test_exception():
    with pytest.raises(github.LicenseNotFoundError):
        try:
            fossl.get_license_info('foobar')
        except github.GitHubApiRateLimitExceeded as rate:
            print(rate)
            print('Aborting test.')
            return


def test_get_license_info(capsys):
    try:
        result = fossl.get_license_info('Apache-2.0', 'mit')
        info = fossl.get_license_info('mit')
    except github.GitHubApiRateLimitExceeded as rate:
        print(rate)
        print('Aborting test.')
        return
    assert 2 == len(result)
    assert 1 == len(info)
    assert result[0].key == 'apache-2.0'
    assert result[0].name == 'Apache License 2.0'
    assert result[0].spdx_id == 'Apache-2.0'
    assert info[0].key == 'mit'
    assert info[0].name == 'MIT License'
    assert info[0].spdx_id == 'MIT'
    description = info[0].description
    implementation = info[0].implementation
    assert description is not None
    assert implementation is not None
    #
    # Again, through the CLI
    #
    sys.argv = ['fossl', 'list']
    main()
    out, err = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    assert not err
    for lic in github.get_license_data():
        assert lic.name in plain
        assert lic.spdx_id in plain



def test_get_license_text(capsys):
    try:
        text = fossl.get_license_text('mit')
    except github.GitHubApiRateLimitExceeded as rate:
        print(rate)
        print('Aborting test.')
        return
    assert MIT_LICENSE_TEXT == text
    #
    # Again, through the CLI
    #
    sys.argv = ['fossl', 'show', 'mit']
    main()
    out, err = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    assert not err
    for field in ['SPDX ID', 'Name', 'Description', 'Implementation']:
        assert field in plain
    sys.argv = ['fossl', 'show', 'mit', '-text']
    main()
    out, err = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    assert not err
    assert len(MIT_LICENSE_TEXT.strip()) == len(plain)
    assert MIT_LICENSE_TEXT.strip() == plain


# def test_print_license_info(capsys):
#     try:
#         licenses = get_license_info('mit')[0]
#     except GitHubApiRateLimitExceeded as rate:
#         print(rate)
#         print('Aborting test.')
#         return
#     print_license_info(licenses, verbose=True)
#     out, _ = capsys.readouterr()
#     result = Text.from_ansi(out).plain
#     for text in ['Name:', 'Description:', 'Implementation:', 'GitHub API URL:',
#                  'MIT License', 'A short and simple permissive license',
#                  'Create a text file (typically named LICENSE or LICENSE.txt)',
#                  'https://api.github.com/licenses/mit']:
#         assert text in result


MIT_LICENSE_TEXT = '''MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
