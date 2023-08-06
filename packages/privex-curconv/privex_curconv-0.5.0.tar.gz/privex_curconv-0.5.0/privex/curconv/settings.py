import json
import os
import sys
import logging
import dotenv
from os import getenv as env
from pathlib import Path
from decimal import getcontext
from privex.helpers import empty, env_int, env_bool, env_csv, env_keyval,  HOUR, DictObject
from privex.helpers import settings as pvx_settings
from privex.helpers.cache import async_adapter_set, adapter_set
from privex.loghelper import LogHelper

DEBUG = env_bool('DEBUG', False)

CONF_PATH = env_csv('CONF_PATH', ['~/.curconv', '~/.curconv.env', '/etc/curconv', '/etc/curconv.env'], csvsplit=":")
"""
To override the list of config path locations, the env var CONF_PATH has to be set
to a colon separated list of paths, similar to the system PATH var.
Example: ``~/.curconv:~/.curconv.env:/etc/curcon``
"""

CONF_OVERRIDE = env_bool('CONF_OVERRIDE', False)
"""
If set to ``True`` in the environment, then variables in the .env config file will take
priority over system environment vars. Otherwise, .env vars won't override system ones.
"""

# CONF_LOCAL_PATH_ALT = env('CONF_LOCAL_PATH', '~/.curconv.env')
CONF_LOCAL = None


########
# Iterate through CONF_PATH to try and locate a .env config file which exists.
########
for p in CONF_PATH:
    lp = Path(p).expanduser().resolve()
    if lp.exists():
        if DEBUG: print(f"Found existing file in CONF_PATH - using as CONF_LOCAL: {lp!s}", file=sys.stderr)
        CONF_LOCAL = lp
        break
    if DEBUG: print(f"SKIPPING - Path does not exist: {lp!s}", file=sys.stderr)

if not empty(CONF_LOCAL):
    try:
        # First assume dotenv = python-dotenv
        dotenv.load_dotenv(str(CONF_LOCAL), override=CONF_OVERRIDE)
    except (AttributeError, KeyError, IndexError):
        # If load_dotenv throws certain exceptions, it may be due to
        # dotenv = django-dotenv, instead of python-dotenv, so try read_dotenv instead.
        dotenv.read_dotenv(str(CONF_LOCAL), override=CONF_OVERRIDE)

# Now that we've potentially loaded a .env file, re-set DEBUG incase it's influenced by .env
# print("__name__ is: ", __name__)
# print(json.dumps(dict(os.environ), indent=4))
DEBUG = env_bool('DEBUG', False)
CONF_DEFAULT = Path('~/.curconv.env').expanduser().resolve()
LOG_LEVEL = env('LOG_LEVEL', 'DEBUG' if DEBUG else 'WARNING').upper()

# _lh = LogHelper('privex.curconv', handler_level=logging.getLevelName(LOG_LEVEL), clear_handlers=False)
_lh = LogHelper('privex.curconv', handler_level=logging.getLevelName(LOG_LEVEL))
_lh.copy_logger('privex')
h = _lh.add_console_handler(stream=sys.stderr)

# _lh.copy_logger('privex.curconv.base', 'privex.curconv.ratesapi', 'privex.curconv.app', 'conv')

# log = _lh.get_logger()
# log.propagate = True
getcontext().prec = 28

# API_BASE = env('API_BASE', 'https://api.exchangeratesapi.io').rstrip('/')
API_BASE = env('API_BASE', 'https://api.ratesapi.io/api').rstrip('/')
API_URI = env('API_URI', '/latest')
API_CACHE_TIME = env_int('API_CACHE_TIME', 1 * HOUR)
pvx_settings.SQLITE_APP_DB_NAME = env('SQLITE_APP_DB_NAME', 'pvx-curconv')
CACHE_ADAPTER = env('CACHE_ADAPTER', 'sqlite')
"""
Available adapters:

  * ``memory`` - Not really useful for this kind-of application, as the cache is stored entirely
                 in the memory of the app, thus is lost as soon as the command finishes.
  * ``sqlite`` - Stores the cache in an SQLite3 database. By default, the database will be stored
                 at ``~/.privex_cache/{SQLITE_APP_DB_NAME}``
                 If you haven't changed :attr:`.SQLITE_APP_DB_NAME` then it'll be stored in
                 the database ``~/.privex_cache/pvx-curconv``
  * ``redis``  - (Recommended) -
                 
"""

CUR_SYMBOLS = {
    'CA$':  'CAD',
    'CAD$': 'CAD',
    'AU$':  'AUD',
    'AUD$': 'AUD',
    'NZ$':  'NZD',
    'NZD$': 'NZD',
    '$':    'USD',
    '€':    'EUR',
    '£':    'GBP',
    'kr':   'SEK',
}

CUST_CUR_SYMBOLS = dict(env_keyval('CUR_SYMBOLS', {}))
CUR_SYMBOLS = {**CUR_SYMBOLS, **CUST_CUR_SYMBOLS}

CONF = DictObject(
    dp=env_int('DEFAULT_DP', 3),
    base_coin=env('BASE_COIN', 'EUR'),
    cur_list=env_csv('CURRENCY_LIST', ['USD', 'EUR', 'GBP', 'CAD', 'SEK', 'TRY'])
)

adapter_set(CACHE_ADAPTER)
async_adapter_set(CACHE_ADAPTER)
