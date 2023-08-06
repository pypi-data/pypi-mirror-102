#!/usr/bin/env python3
"""
High level functions/classes for running the Python Currency Converter CLI

Official Repo: https://github.com/Privex/python-curconv
License: X11 / MIT


Copyright::

    +===================================================+
    |                 © 2021 Privex Inc.                |
    |               https://www.privex.io               |
    +===================================================+
    |                                                   |
    |        Python Currency Converter CLI              |
    |        License: X11/MIT                           |
    |                                                   |
    |        Core Developer(s):                         |
    |                                                   |
    |          (+)  Chris (@someguy123) [Privex]        |
    |                                                   |
    +===================================================+

    Python Currency Converter CLI - A small CLI tool for quick currency conversions on the command line
    Copyright (c) 2021    Privex Inc. ( https://www.privex.io )

"""
import sys
import asyncio
import textwrap
import argparse
from pathlib import Path
from decimal import Decimal
from privex.helpers import dec_round, ErrHelpParser
from typing import Union
from privex.curconv import settings
from privex.curconv.base import gen_env, is_numstr, replace_sym, to_keyval, trans_dict, trans_rate
from privex.curconv.ratesapi import RatesAPIAdapter
from privex.curconv.version import VERSION
import logging

# print("__name__ is: ", __name__)

__all__ = [
    'conv_adapter', 'convert', 'str_extract', 'str_convert',
    'main',
]

log = logging.getLogger(__name__)

conv_adapter = RatesAPIAdapter()
CONF = settings.CONF


async def convert(
    amt: Union[Decimal, float, int, str], from_coin: str, to_coin: str, base_coin: str = None
):
    if not isinstance(amt, Decimal):
        amt = Decimal(amt)
    log.debug(f" [convert] Calling conv_adapter.get_rates for base coin: {base_coin!r}")
    rates = await conv_adapter.get_rates(base=base_coin)
    trate = trans_rate(from_coin, to_coin, rates)
    return amt * trate


def str_extract(query: str):
    sq = list(query.split())
    if not is_numstr(sq[0]):
        rsm = replace_sym(sq[0]).split()
        if len(rsm) < 2:
            raise ValueError(f"First segment of string isn't a number, nor has a valid symbol prefix/suffix. Segment is: {sq[0]!r}")
        sq[0] = rsm[0]
        sq.insert(1, rsm[1])
    amt = Decimal(sq[0])
    fcoin = sq[1]
    log.debug(f" [str_extract] Extracted amt + fcoin: amt = {amt!r}; fcoin = {fcoin!r}")

    if len(sq) <= 2:
        return [amt, fcoin]
    dcoin = sq[3]
    if dcoin in settings.CUR_SYMBOLS:
        dcoin = replace_sym(dcoin)
    log.debug(f" [str_extract] Full extraction. amt = {amt!r}; fcoin = {fcoin!r}; dcoin = {dcoin!r}")

    return [amt, fcoin, dcoin]


async def str_convert(query: str, base_coin='EUR'):
    sq = str_extract(query)
    log.debug(f" [str_convert] Calling conv_adapter.get_rates with base_coin: {base_coin!r}")
    
    rates = await conv_adapter.get_rates(base_coin)
    amt, fcoin = sq[0], sq[1]
    if len(sq) <= 2:
        if fcoin.upper() == base_coin.upper():
            return {k: amt * v for k, v in rates['rates'].items()}
        tdt = trans_dict(fcoin, rates)
        return {k: amt * v for k, v in tdt.items()}
    dcoin = sq[2]
    if fcoin.upper() == base_coin.upper():
        return amt * rates['rates'].get(dcoin, rates['rates'].get(dcoin.upper()))
    return amt * trans_rate(fcoin, dcoin, rates)


async def main():
    descr = textwrap.dedent(f"""
        CLI Currency Converter - Version v{VERSION}
        (C) 2021 Someguy123 ( https://github.com/Someguy123 )
            Privex Inc.     ( https://www.privex.io )
            Official Repo:  https://github.com/Privex/python-curconv

        Easily get the exchange rate / conversion amount for either an individual coin pair,
        for any currency into all of your favourite currencies, or for any currency into
        all other currencies.

        Examples:

            # Show how much 1 USD would get you in your favourite currencies
            $ {sys.argv[0]} 1 usd
            # Show how much 1000 SEK is worth in USD
            $ {sys.argv[0]} 1000 SEK to USD
            # Show how much 50 GBP is worth in EUR, with full mode enabled (show from_coin and to_coin in output)
            $ {sys.argv[0]} -f £50 to eur
            # Show how much 20 CAD is worth in all supported currencies, with 6 dp precision used for displaying exchange rates
            $ {sys.argv[0]} -d 6 -a CA$20
            # Show how much 50 AUD is worth in NZD, USD, EUR, and JPY
            $ {sys.argv[0]} -c nzd,usd,eur,jpy AU$50

        ------------

        Customization:

            Default ENV config search path (CONF_PATH - colon separated):
                {' : '.join(settings.CONF_PATH)}

            # Generate a template ENV config file to the default location: {settings.CONF_DEFAULT!s}
            $ {sys.argv[0]} -Gd

            # Generate a template ENV config to STDOUT (the terminal), for piping or copying
            $ {sys.argv[0]} -G
            $ {sys.argv[0]} -G | sudo tee /etc/curconv.env

            # Generate a template ENV config to the file /etc/curconv.env
            $ {sys.argv[0]} -G -Gf /etc/curconv.env

        ENV Vars:

            DEBUG (bool)            - Enables debug mode, which also boosts LOG_LEVEL to DEBUG. Default: 'false'
            LOG_LEVEL (str)         - The level of logging to output (DEBUG,INFO,WARNING,ERROR,CRITICAL). Default: {settings.LOG_LEVEL!r}
            API_BASE (str)          - The base API URL to use - Default: {settings.API_BASE!r}
            API_CACHE_TIME (int)    - The number of seconds to cache exchange rates - Default: {settings.API_CACHE_TIME}
            CACHE_ADAPTER (str)     - Adapter to use for caching: memory,redis,memcached - Default: {settings.CACHE_ADAPTER!r}
            DEFAULT_DP (int)        - Decimal places to round output numbers to - Default: {settings.CONF.dp}
            BASE_COIN (str)         - The base coin used by the API for conversion - Default: {settings.CONF.base_coin!r}
            CURRENCY_LIST (str)     - Comma separated list of "favourite" currency codes.
                                      Default: {','.join(settings.CONF.cur_list)!r}
            CUR_SYMBOLS (str)       - A key value map of symbols to currencies, e.g. '$:USD,£:GBP,kr:SEK' etc.
                                      Default: {to_keyval(settings.CUR_SYMBOLS)!r}

            CONF_DEFAULT (str)      - This setting isn't too important, it purely controls where the
                                      "default config file" is considered to be located, and is only
                                      currently used when the '-Gd' flag is passed, to generate a
                                      template .env config and output it to the default location.
                                      Default: {str(settings.CONF_DEFAULT)!r}


        System Environment ONLY:

            These are ENV vars which can only be set dynamically by either injecting them with your shell
            when running the CLI tool, or exporting them before running the tool. They can't be set in
            the config (.env) file due to them being used prior to loading the .env file.

            (partially) DEBUG (bool)    - While DEBUG can be set in your config file, the config setting only
                                          affects the code ran AFTER your .env is loaded. If you set DEBUG=true
                                          in the system environment when running the tool, it enables
                                          debug logging early-on, including during the code which actually
                                          locates an existing .env file and loads it.

            CONF_OVERRIDE (bool)        - This is a boolean setting (Default: False) which controls whether
                                          settings in your .env config file take priority over system env vars.
                                          When True, if you pass 'DEBUG=true' via system env vars, but your
                                          .env config contains 'DEBUG=false', then your config setting takes
                                          priority and DEBUG will be false.
                                          When False, in the above scenario, the system env var would take
                                          priority and DEBUG would be True.

            CONF_PATH (str)             - This variable controls the list of config file locations to check
                                          for an existing file, in priority order (leftmost first).
                                          It's read similar to the system PATH variable, split into a
                                          list using the ':' colon character as the separator,
                                          e.g. '~/.curconv:~/.curconv.env:/etc/curcon'.
                                          The default value for this is: {':'.join(settings.CONF_PATH)!r}

    """)
    
    parser = ErrHelpParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=descr
    )
    parser.add_argument('-d', '-dp', '--dp', '--decimals', '--decimal-places', default=CONF.dp, dest='dp',
                        help="The number of decimal places to round rate results to. Default: {CONF.dp}")
    parser.add_argument('-b', '--base', '--base-coin', default=CONF.base_coin, dest='base_coin',
                        help=f"Normally you don't need to change this. This controls the 'base' or 'root' currency "
                             f"which all rates from the API are in, which is used to inversely calculate the "
                             f"exchange rate between two or more arbitrary currencies. Default: {CONF.base_coin!r}")
    parser.add_argument('-c', '--currencies', default=','.join(CONF.cur_list), dest='currencies',
                        help="Use '-c' to override the default 'favourite'/'selected' currency list "
                             "with the currencies you actually want to display, e.g. '-c USD,AUD,NZD,TRY'")
    parser.add_argument('-a', '-ac', '--all-currencies', default=False, action='store_true', dest='all_currencies',
                        help="When querying just the source i.e. '10.32 USD', the '-a' flag results in "
                             "all supported currencies exchange rates being outputted, instead of just "
                             "favourited/selected currencies.")
    parser.add_argument('-f', '--full', default=False, action='store_true', dest='full_mode',
                        help="In full mode, the source amount and currency will be displayed with "
                             "an '=' equals sign before the destination(s), and for direct single "
                             "conversions, it enables displaying the destination currency too, "
                             "e.g. query '50 GBP to EUR' outputs '57.61' normally, but in "
                             "full mode it would output '50 GBP = 57.61 EUR'.")
    parser.add_argument('-G', '-genv', '--gen-env', '--generate-env', default=False,
                        action='store_true', dest='gen_env',
                        help=f"Generate a .env file from current loaded settings. Outputs to stdout "
                             f"unless you pass either '-Gf [file]' to output to a file, or '-Gd' "
                             f"to output to the default config location {str(settings.CONF_DEFAULT)!r}")
    
    parser.add_argument('-Gf', '--env-out', '--gen-env-out', default="-", dest='env_out',
                        help="Set the output location for the .env generated when used with '-G'")
    parser.add_argument('-Gd', '--env-default', '--gen-env-default', default=False,
                        action='store_true', dest='env_out_default',
                        help=f"Generate and output a .env file from current loaded settings "
                             f"to the default config location: {str(settings.CONF_DEFAULT)!r}")
    parser.add_argument('query', nargs='*', help="The conversion query, e.g. '4.20 USD to GBP' or '£5.20 to EUR'")
    zargs = parser.parse_args()
    z_gen = zargs.gen_env or zargs.env_out_default
    
    if z_gen:
        xenv = gen_env()
        if zargs.env_out_default:
            print(f" >>> Generating ENV file to default location: {settings.CONF_DEFAULT}", file=sys.stderr)
            with open(str(settings.CONF_DEFAULT), 'w') as fh:
                fh.write(xenv)
            return print(f" +++ Successfully wrote ENV file to default location: {settings.CONF_DEFAULT}", file=sys.stderr)
        
        if zargs.env_out in ['', '-', '/dev/stdout', 'stdout', 'STDOUT']:
            return print(xenv)
        
        if zargs.env_out in ['/dev/stderr', 'stderr', 'STDERR']:
            return print(xenv, file=sys.stderr)
        out_loc = Path(zargs.env_out).expanduser().resolve()
        print(f" >>> Generating ENV file to custom location: {out_loc!s}", file=sys.stderr)
        with open(str(out_loc), 'w') as fh:
            fh.write(xenv)
        return print(f" +++ Successfully wrote ENV file to custom location: {out_loc!s}", file=sys.stderr)
    
    CONF.dp = zargs.dp
    CONF.base_coin = zargs.base_coin.upper()
    CONF.cur_list = zargs.currencies.split(',')
    if len(zargs.query) == 0:
        return parser.error("No query specified! You must specify a query e.g. '5 usd to gbp' or '2.1 cad'")
    q = ' '.join(zargs.query)
    
    log.debug(f" [main] Entering conversion adapter using 'async with'")
    async with conv_adapter:
        log.debug(f" [main] Calling str_convert with arguments: (0 'q') = {q!r} ; base_coin = {CONF.base_coin!r} ;")
        sv = await str_convert(q, base_coin=CONF.base_coin)
        log.debug(f" [main] Calling str_extract with arguments: (0 'q') = {q!r} ;")
        sq = str_extract(q)
        amt, fcoin = sq[0], sq[1]
    
    if isinstance(sv, dict):
        if zargs.full_mode:
            print(f"  {amt} {fcoin.upper()} =\n")
        rsv = {k: dec_round(v, CONF.dp) for k, v in sv.items()}
        if zargs.all_currencies:
            for k, v in rsv.items():
                if k.upper() == fcoin.upper(): continue
                print(f"{v} {k.upper()}")
        else:
            for k in CONF.cur_list:
                if k.upper() == fcoin.upper(): continue
                print(f"{rsv[k.upper()]} {k.upper()}")
        print()
        return
    dcoin = sq[2]
    sv = dec_round(sv, CONF.dp)
    if zargs.full_mode:
        print(f"{amt} {fcoin.upper()} = {sv} {dcoin.upper()}")
    else:
        print(f"{sv}")


if __name__ == '__main__':
    asyncio.run(main())


