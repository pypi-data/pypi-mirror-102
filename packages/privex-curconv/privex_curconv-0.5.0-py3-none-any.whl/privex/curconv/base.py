"""
Common/shared functions/classes/objects used by various modules in the Python Currency Converter CLI

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
import abc
import asyncio
import contextlib
import time
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Dict, List, Optional, Tuple, Union, AsyncContextManager

import httpx
from async_property import async_property
from privex.helpers import AsyncCacheAdapter, DictDataClass, await_if_needed, empty
from privex.helpers.cache import AsyncCacheWrapper, async_cached

from privex.curconv import settings

import logging

__all__ = [
    'replace_sym', 'sort_dict', 'dump_args', 'to_keyval', 'gen_env',
    '_gen_env', 'Pair', 'AnyPair', 'IterAnyPair', 'PairList', 'CurrencyAdapter',
    'trans_rate', 'trans_dict', 'is_numstr'
]

log = logging.getLogger(__name__)


def replace_sym(data: str) -> str:
    """
    Converts currency strings such as ``£5.00`` to ``5.00 GBP`` - or ``10 kr`` to ``10 SEK``
    """
    origdata = data
    data = data.strip()
    for s, r in settings.CUR_SYMBOLS.items():
        if data.startswith(s) or data.endswith(s):
            log.debug(f"Replacing symbol {s!r} with {r!r}")
            return f"{data.replace(s, '').strip()} {r}".strip()
        if data.upper().startswith(s) or data.upper().endswith(s):
            log.debug(f"Replacing symbol {s!r} with {r!r} (uppercase)")
            return f"{data.upper().replace(s, '').strip()} {r}".strip()
    return origdata


def sort_dict(data: dict) -> dict:
    data = dict(data)
    skeys = sorted(list(data.keys()))
    return {k: data[k] for k in skeys}


def dump_args(*args, _serial_func=repr, **kwargs) -> str:
    """
    Convert positional args and keyword args into a flat string e.g. for cache keys.
    Sorts the keys in kwargs to ensure different ordering of kwargs (e.g. ``a='hello', b=123`` and ``b=123, a='hello'``)
    which have the same value, will still result in the same string.

    Example::

        >>> dump_args('lorem', 'ipsum', hello='world', donkey=420, banana=Decimal('1.23123'))
        "0='lorem';1='ipsum';banana=Decimal('1.23123');donkey=420;hello='world';"
        >>> dump_args('lorem', 'ipsum', donkey=420, hello='world', banana=Decimal('1.23123'), _serial_func=str)
        '0=lorem;1=ipsum;banana=1.23123;donkey=420;hello=world;'

    """
    
    args, kwargs = list(args), sort_dict(kwargs)
    dt = ""
    for i, a in enumerate(args):
        dt += f"{i}={_serial_func(a)};"
    for k, v in kwargs.items():
        dt += f"{k}={_serial_func(v)};"
    return dt


def to_keyval(ob: Union[dict, List[Tuple[Any, Any]]], valsplit=':', csvsplit=',') -> str:
    """
    Convert a :class:`.dict` , or a :class:`.list` of two value :class:`.tuple` 's
    into a "key value" string, which can be parsed by :func:`privex.helpers.common.parse_keyval`
    or manually with a small amount of python.

    Example::

        >>> d = dict(hello='world', lorem=123, ipsum='dolor')
        >>> to_keyval(d)
        'hello:world,lorem:123,ipsum:dolor'
        >>> to_keyval(d, valsplit='=', csvsplit='/')
        hello=world/lorem=123/ipsum=dolor

    """
    xo = ob.items() if isinstance(ob, dict) else ob
    return csvsplit.join([f'{k}{valsplit}{v}' for k, v in xo])


def _gen_env(**kwargs) -> dict:
    # global DEBUG, LOG_LEVEL, API_BASE, API_CACHE_TIME, CACHE_ADAPTER
    rz = dict(
        DEBUG='true' if settings.DEBUG else 'false',
        LOG_LEVEL=str(settings.LOG_LEVEL),
        API_BASE=settings.API_BASE,
        API_CACHE_TIME=str(settings.API_CACHE_TIME),
        CACHE_ADAPTER=settings.CACHE_ADAPTER,
        DEFAULT_DP=str(settings.CONF.dp),
        BASE_COIN=settings.CONF.base_coin,
        CURRENCY_LIST=','.join(settings.CONF.cur_list),
        CUR_SYMBOLS=to_keyval(settings.CUR_SYMBOLS),
    )
    return {**rz, **dict(kwargs)}


def gen_env(**kwargs) -> str:
    dz = _gen_env(**kwargs)
    res = [f"{k}={v}" for k, v in dz.items()]
    return "\n".join(res) + "\n"


@dataclass
class Pair(DictDataClass):
    from_sym: str
    to_sym: str
    rate: Decimal = field(default_factory=lambda: Decimal('0'))
    
    @property
    def pair(self) -> str:
        return f"{self.from_sym.upper()}_{self.to_sym.upper()}"
    
    def __post_init__(self):
        if not isinstance(self.rate, Decimal):
            self.rate = Decimal(self.rate)
        self.from_sym = self.from_sym.upper()
        self.to_sym = self.to_sym.upper()
    
    def is_pair(self, pair: str) -> bool:
        from_sym = self.from_sym.upper()
        to_sym = self.to_sym.upper()
        if pair.upper() == f"{from_sym}{to_sym}": return True
        if pair.upper() == f"{from_sym}_{to_sym}": return True
        if pair.upper() == f"{from_sym}/{to_sym}": return True
        if pair.upper() == f"{from_sym}-{to_sym}": return True
        return False
    
    def is_pair_sym(self, from_sym: str, to_sym: str) -> bool:
        return self.is_pair(f"{from_sym.upper()}_{to_sym.upper()}")
    
    def invert(self) -> "Pair":
        return Pair(from_sym=self.to_sym, to_sym=self.from_sym, rate=Decimal('1') / self.rate)
    
    def __str__(self):
        return str(self.rate)
    
    def __int__(self):
        return int(str(self))
    
    def __float__(self):
        return float(str(self))
    
    def __lt__(self, other):
        if isinstance(other, (str, float, int, Decimal)):
            return self.rate < Decimal(other)
        if isinstance(other, Pair):
            return self.rate < other.rate
        return False

    def __gt__(self, other):
        if isinstance(other, (str, float, int, Decimal)):
            return self.rate > Decimal(other)
        if isinstance(other, Pair):
            return self.rate > other.rate
        return False

    def __eq__(self, other):
        if isinstance(other, str):
            return self.is_pair(other) or other == str(self)
        if isinstance(other, (float, int, Decimal)):
            return Decimal(other) == self.rate
        if isinstance(other, Pair):
            if self.from_sym.upper() != other.from_sym.upper(): return False
            if self.to_sym.upper() != other.to_sym.upper(): return False
            if self.rate != other.rate: return False
            return True
        return False
    
    def __contains__(self, item):
        item = str(item)
        if item == str(self): return True
        if item.upper() == self.from_sym.upper(): return True
        if item.upper() == self.to_sym.upper(): return True
        if self.is_pair(item): return True
        return False


AnyPair = Union[Pair, "PairList"]
IterAnyPair = Union[List[AnyPair], Tuple[AnyPair, ...]]


@dataclass
class PairList(DictDataClass):
    """
    Represents a list of :class:`.Pair` objects, and provides magic methods to make it easy to query the list
    of pairs painlessly, as if the pair list were a dictionary.
    
    Examples::
    
        >>> pl = PairList([Pair('EUR', 'USD', Decimal('1.1986'))])
        >>> pl += Pair('EUR', 'GBP', Decimal('0.86793'))
        >>> 'eurgbp' in pl
        True
        >>> 'EUR/USD' in pl
        True
        >>> pl['eurgbp']
        Pair(from_sym='EUR', to_sym='GBP', rate=Decimal('0.86793'))
        >>> pl['EUR/GBP']
        Pair(from_sym='EUR', to_sym='GBP', rate=Decimal('0.86793'))
        >>> pl.find('eur', 'usd')
        Pair(from_sym='EUR', to_sym='USD', rate=Decimal('1.1986'))
        >>> pl['eur_gbp'].invert()
        Pair(from_sym='GBP', to_sym='EUR', rate=Decimal('1.152166649384166925904162778'))
        >>> pl.filter('eur')
        [Pair(from_sym='EUR', to_sym='USD', rate=Decimal('1.1986')),
         Pair(from_sym='EUR', to_sym='GBP', rate=Decimal('0.86793'))]
    
    """
    pairs: List[Pair] = field(default_factory=list)
    
    def find(self, from_sym: str, to_sym: str) -> Optional[Pair]:
        for p in self.pairs:
            if p.is_pair_sym(from_sym, to_sym): return p
        return None

    def find_pair(self, pair: str) -> Optional[Pair]:
        for p in self.pairs:
            if p.is_pair(pair): return p
        return None
    
    def filter(self, from_sym: str = None, to_sym: str = None) -> List[Pair]:
        if not empty(from_sym) and not empty(to_sym): return [p for p in self.pairs if p.is_pair_sym(from_sym, to_sym)]
        if not empty(from_sym): return [p for p in self.pairs if p.from_sym == from_sym.upper()]
        if not empty(to_sym): return [p for p in self.pairs if p.to_sym == to_sym.upper()]
        return []
    
    def add(self, other: Union[AnyPair, IterAnyPair]) -> "PairList":
        if isinstance(other, (PairList, Pair)): return self._add(other)
        if isinstance(other, (list, tuple)): return self._merge(other)
        raise ValueError(f"Cannot add object of type {type(other)} (repr: {other!r}) to PairList")
    
    append = add

    def _add(self, other: AnyPair) -> "PairList":
        if isinstance(other, PairList): self.pairs += other.pairs
        elif isinstance(other, Pair): self.pairs.append(other)
        else: raise ValueError(f"Cannot add object of type {type(other)} (repr: {other!r}) to PairList")
        return self
    
    def _merge(self, other: IterAnyPair) -> "PairList":
        if len(other) > 0:
            if isinstance(other[0], Pair):
                self.pairs += list(other)
            elif isinstance(other[0], PairList):
                for pl in other:
                    self.pairs += pl.pairs
            else:
                raise ValueError(f"Cannot add object of type {type(other)} (repr: {other!r}) to PairList")
        return self
    
    def __getitem__(self, item) -> Union[Pair, List[Pair]]:
        if item == 'pairs':
            return self.pairs
        
        xpair = self.find_pair(item)
        if not empty(xpair): return xpair
        
        filtered = self.filter(item)
        if len(filtered) > 0: return filtered
        raise KeyError(f"Key/pair '{item}' not found.")
    
    def __add__(self, other: Union[AnyPair, IterAnyPair]) -> "PairList":
        return self.add(other)
    
    def __contains__(self, item):
        if not empty(self.find_pair(item), itr=True): return True
        if not empty(self.filter(item), itr=True): return True
        if not empty(self.filter(to_sym=item), itr=True): return True
        for p in self.pairs:
            if p == item: return True
        return False
    

class CurrencyAdapter(abc.ABC):
    """
    This is the base class for all privex-curconv currency adapters, which includes various functions pre-scaffolded,
    allowing a child class to simply implement :meth:`._get_rates` and ideally change :attr:`.DEFAULT_CACHE_PREFIX`
    to be fully functional.
    
    It handles higher level functionality such as caching and some common configuration options, so
    that child classes only need to worry about obtaining the exchange rates, and converting them
    into a :class:`.PairList` / :class:`.Pair`
    
    An adapter implementing this class can be used like so::
        
        >>> rp = RatesAPIAdapter()
        >>> res = await rp.get_rates()
        >>> 'eurusd' in res
        True
        >>> res['eurusd']
        Pair(from_sym='EUR', to_sym='USD', rate=Decimal('1.1986'))
    
    
    """
    DEFAULT_CACHE_PREFIX: str = "conv:get_rates"
    CTX_SLEEP_PRE: float = 0.1
    CTX_SLEEP_POST: float = 0.1
    _rates: Optional[PairList]
    _rates_timeout: Optional[int]
    rates_refresh: int
    api_base: str
    api_uri: str
    httpx_conf: dict
    base_coin: str
    cache: Union[AsyncCacheAdapter, AsyncCacheWrapper]
    cache_timeout: Union[float, int, Decimal]
    cache_prefix: str
    _http: Optional[httpx.AsyncClient]
    
    def __init__(self, base_coin: Optional[str] = None, **kwargs):
        self.api_base = kwargs.get('api_base', '')
        self.api_uri = kwargs.get('api_uri', '')
        self.httpx_conf = kwargs.get('httpx_conf', {})
        self.base_coin = base_coin
        self._rates = None
        self._rates_timeout = None
        self._http = None
        
        self.cache = kwargs.get('cache', async_cached)
        self.cache_timeout = kwargs.get('cache_timeout', settings.API_CACHE_TIME)
        self.cache_prefix = kwargs.get('cache_prefix', self.DEFAULT_CACHE_PREFIX)
        
        self.rates_refresh = int(kwargs.get('rates_refresh', self.cache_timeout))
    
    def _make_httpx(self, **kwargs) -> httpx.AsyncClient:
        hconf = {k: v for k, v in self.httpx_conf.items()}
        hconf = {**hconf, **kwargs}
        return httpx.AsyncClient(**hconf)
    
    @property
    def httpx(self) -> Union[httpx.AsyncClient, AsyncContextManager]:
        if self._http:
            log.debug(f"Detected {self.__class__.__name__!s}._http - returning http_wrapper for re-using client")
    
            @contextlib.asynccontextmanager
            async def http_wrapper() -> AsyncContextManager:
                log.debug(f"Yielding {self.__class__.__name__!s}._http from http_wrapper")
                yield self._http
                log.debug(f"Returned from yielding {self.__class__.__name__!s}._http in http_wrapper")

            return http_wrapper()
        log.debug(f"No {self.__class__.__name__!s}._http - returning throwaway AsyncClient")
        return self._make_httpx()
    
    @abc.abstractmethod
    async def _get_rates(self, base: str = None, *symbols, **kwargs) -> PairList:
        raise NotImplementedError(f"{self.__class__.__name__} must implement _get_rates!")
    
    async def _get_rate(self, from_sym: str = None, to_sym: str = None, **kwargs) -> Pair:
        r: PairList = await self.rates
        return r.find(from_sym, to_sym)
    
    def _get_prefix(self, *args, _extra_prefix="", **kwargs) -> str:
        return f"{self.cache_prefix}:{_extra_prefix}{dump_args(*args, **kwargs)}"

    async def get_rate(self, from_sym: str = None, to_sym: str = None, **kwargs) -> Pair:
        cpfx = self._get_prefix(from_sym=str(from_sym).upper(), to_sym=str(to_sym).upper(), _extra_prefix='rate:', **kwargs)
        res = await await_if_needed(self.cache.get, cpfx)
        if empty(res, itr=True, zero=True):
            res = await await_if_needed(self._get_rate, from_sym, to_sym, **kwargs)
            await await_if_needed(self.cache.set, cpfx, res, self.cache_timeout)
        return res

    async def get_rates(self, base: str = None, *symbols, reset=False, **kwargs) -> PairList:
        # Unless ._rates is valid and not expired, then we need to try the external cache, or query directly.
        if reset or self.rates_expired:
            log.debug(f" [{self.__class__.__name__}.get_rates] Rates not loaded / expired. Reading cache.")
            cpfx = self._get_prefix(base=str(base).upper(), symbols=sorted(list(symbols)), **kwargs)
            # Try loading rates from the cache. If there's no valid rates in the cache, then call .do_get_rates
            # to get fresh rates + set both the local _rates cache and external cache.
            res = await await_if_needed(self.cache.get, cpfx)
            if reset or empty(res, itr=True, zero=True):
                log.debug(f" [{self.__class__.__name__}.get_rates] Rates not in cache - calling HTTP(S) API")
                res = await self.do_get_rates(base, *symbols, **kwargs)
            return res
        log.debug(f" [{self.__class__.__name__}.get_rates] Rates already in memory. Using in-memory rates: {self._rates}")
        return self._rates

    async def do_get_rates(self, base: str = None, *symbols, set_cache=True, **kwargs):
        cpfx = self._get_prefix(base=str(base).upper(), symbols=sorted(list(symbols)), **kwargs)
        log.debug(f" [{self.__class__.__name__}.do_get_rates] Calling API via ._get_rates")

        res = await await_if_needed(self._get_rates, base, *symbols, **kwargs)
        if set_cache and not empty(res, itr=True):
            log.debug(f" [{self.__class__.__name__}.do_get_rates] Storing results via privex.helpers async cache")
            await await_if_needed(self.cache.set, cpfx, res, timeout=self.cache_timeout)
            self._set_rates(res)
        return res

    @property
    def rates_expired(self) -> bool:
        if empty(self._rates, itr=True, zero=True): return True
        if empty(self._rates_timeout, zero=True): return True
        return not (int(time.time()) < int(self._rates_timeout))
    
    @async_property
    async def rates(self) -> PairList:
        if self.rates_expired:
            return await self.get_rates()
        return self._rates
    
    def _set_rates(self, rates: PairList) -> PairList:
        self._rates = rates
        self._rates_timeout = int(time.time()) + int(self.rates_refresh)
        return self._rates
    
    async def trans_rate(self, from_coin: str, to_coin: str) -> Decimal:
        pass
    
    async def __aenter__(self):
        log.debug(f" [{self.__class__.__name__}.__aenter__] Creating and storing httpx client")
        self._http = self._make_httpx()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._http is not None:
            log.debug(f" [{self.__class__.__name__}.__aexit__] Closing httpx client")
            try:
                if self.CTX_SLEEP_PRE > 0: await asyncio.sleep(self.CTX_SLEEP_PRE)
                await self._http.aclose()
            except Exception as e:
                log.warning(f"Failed to close httpx.AsyncClient. Reason: {type(e)} - {e!s}")
            finally:
                if self.CTX_SLEEP_POST > 0: await asyncio.sleep(self.CTX_SLEEP_POST)
                self._http = None


def trans_rate(from_coin: str, to_coin: str, rates: PairList, base_coin: str = settings.CONF.base_coin) -> Decimal:
    """
    Get a translated rate using ``rates``

    Example::

        >>> rates = await get_rates("EUR")
        >>> trans_rate("USD", "SEK", rates)
        Decimal('8.556303086367841224455470524')
        >>> trans_rate("SEK", "USD", rates)
        Decimal('0.1168729052612956173889112764')

    """
    if from_coin.upper() == to_coin.upper(): return Decimal('1.000000')
    if 'rates' in rates and isinstance(rates.get('rates', None), dict):
        rates = rates['rates']
    # from_rate = rates.get(from_coin, rates.get(from_coin.upper()))
    # to_rate = rates.get(to_coin, rates.get(to_coin.upper()))
    from_rate = rates.find(base_coin, from_coin)
    to_rate = rates.find(base_coin, to_coin)
    if from_rate is None: raise AttributeError(f"from_coin {from_coin!r} was not found in 'rates'!")
    if to_rate is None: raise AttributeError(f"to_coin {to_coin!r} was not found in 'rates'!")
    return (Decimal('1') / from_rate.rate) * to_rate.rate


def trans_dict(from_coin: str, rates: PairList) -> Dict[str, Decimal]:
    # if 'rates' in rates and isinstance(rates.get('rates', None), dict):
    #     rates = rates['rates']
    # return {k: trans_rate(from_coin, k, rates) for k in list(rates.keys())}
    return {p.to_sym: trans_rate(from_coin, p.to_sym, rates) for p in rates.pairs}


def is_numstr(d: str):
    if len(d) == 0: return False
    if not d[0].isdigit() and not d[0] in ['.', '-', '+']:
        return False
    hasdot, has_e = False, False
    for c in d[1:]:
        if c == '.':
            if hasdot: return False
            hasdot = True
            continue
        if c == 'e':
            if has_e: return False
            has_e = True
            continue
        if c.isdigit() or c in [',', '-', '+']:
            continue
        return False
    return True

