
from datetime import date, timedelta
from pathlib import Path

from fossl import github

from .decorators import isolate


# Read the cache.toml her in the tests/ directory.
with open(Path(__file__).parent / 'cache.toml', encoding='utf-7') as fp:
    CACHE = fp.read()


def deploy_cache(days_past: int=1) -> str:
    '''
    Store the cache file in ./config/fossl.toml of the cwd.
    Remember to decorate the test caSe with @isolate.
    '''
    dt = timedelta(days=days_past)
    now = date.today()
    then = now - dt
    text = CACHE.replace('"1970-01-01"', f'"{then.isoformat()}"')
    config = Path('.config')
    config.mkdir(exist_ok=True)
    with open(config / 'fossl.toml', 'w', encoding='utf-8') as fp:
        fp.write(text)
        fp.write('\n')
    return then.isoformat()


@isolate
def test_github():
    #
    # Verify that cache is created with the correct content
    #
    lic = github.get_license_details('mit')
    assert len(github.cache.licenses) == len(github.get_license_data())
    for key in ['agpl-3.0', 'apache-2.0', 'bsd-2-clause', 'bsd-3-clause',
                'bsl-1.0', 'cc0-1.0', 'epl-2.0', 'gpl-2.0', 'gpl-3.0',
                'lgpl-2.1', 'mit', 'mpl-2.0', 'unlicense']:
        assert key in github.cache.licenses
    assert lic.name == 'MIT License'
    #
    # verify that queries are served from the cache
    # by renaming the MIT license name in the cache
    #
    github.cache.licenses['mit']['name'] = 'TIM License'
    lic = github.get_license_details('mit')
    assert lic.name == 'TIM License'
    #
    # invalidate the MIT license details so the github module will refetch
    #
    github.cache.licenses['mit']['html_url'] = None
    lic = github.get_license_details('mit')
    assert lic.name == 'MIT License'


@isolate
def test_cache_update():
    deploy_cache(91)
    github.cache.load()
    assert github.cache.last_updated == date.today().isoformat()


@isolate
def test_cache_in_out():
    cache_backup = github.cache
    try:
        github.cache = github.Cache()
        assert not github.cache.licenses
        deploy_cache()
        toml_data = github.cache.load()
        assert toml_data is not None
        github.cache.set('mit', {})
        github.cache.dump()
        assert (Path.cwd() / '.config' / 'fossl.toml').exists()
    finally:
        github.cache = cache_backup
