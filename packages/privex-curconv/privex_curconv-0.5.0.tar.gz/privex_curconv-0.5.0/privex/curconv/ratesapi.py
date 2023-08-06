"""
RatesAPI.io Currency Adapter for the Python Currency Converter CLI

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
import json
import httpx
from decimal import Decimal
from privex.helpers import empty_if
from privex.curconv import settings
from privex.curconv.base import CurrencyAdapter, Pair, PairList
import logging

__all__ = ['RatesAPIAdapter']

# log = logging.getLogger('privex.curconv')
log = logging.getLogger(__name__)
# log.setLevel('DEBUG')


# log.propagate = True
# log.


class RatesAPIAdapter(CurrencyAdapter):
    DEFAULT_CACHE_PREFIX = "rates_api:conv"
    
    def __init__(self, base_coin: str = settings.CONF.base_coin, **kwargs):
        kwargs = dict(kwargs)
        conf = dict(
            api_base=kwargs.pop('api_base', settings.API_BASE),
            api_uri=kwargs.pop('api_uri', settings.API_URI),
        )
        conf = {**kwargs, **conf}
        super().__init__(
            base_coin, **conf
        )
        if 'http2' not in self.httpx_conf: self.httpx_conf['http2'] = True
        if 'timeout' not in self.httpx_conf: self.httpx_conf['timeout'] = 10
    
    async def _get_rates(self, base: str = None, *symbols, **kwargs) -> PairList:
        symbols = list(symbols)
        if len(symbols) == 1 and "," in symbols[0]:
            symbols = [s.strip() for s in list(symbols[0].split(','))]
        base = empty_if(base, self.base_coin).upper()
    
        raise_status = kwargs.pop('raise_status', kwargs.pop('raise_for_status', True))
    
        data = dict(base=base)
        if len(symbols) > 0:
            data['symbols'] = ','.join(symbols)
    
        uri = f"{self.api_base}{self.api_uri}"
    
        log.info(f"Retrieving exchange rates from {uri!r} - base coin: {base!r} || symbols: {symbols!r}")
        # async with httpx.AsyncClient(http2=True, timeout=10) as h:
        async with self.httpx as h:
            res = await h.get(uri, params=data)
            if raise_status:
                res.raise_for_status()
            dc = ""
            async for ta in res.aiter_text():
                dc += ta
        log.debug(f"Decoding exchange rate JSON: {dc!r}")
        j = json.loads(dc, parse_float=Decimal)
    
        if 'rates' in j:
            if base not in j['rates']:
                j['rates'][base] = Decimal('1.0000000')
        
        xpairs = []
        for curr, rate in j['rates'].items():
            xpairs.append(Pair(base, curr, rate))
        return PairList(pairs=xpairs)
