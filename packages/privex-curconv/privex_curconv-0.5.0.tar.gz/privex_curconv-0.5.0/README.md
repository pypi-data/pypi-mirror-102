# Privex Python Currency Converter CLI

A small CLI tool for quick currency conversions on the command line

Official Repo: https://github.com/Privex/python-curconv

```
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
```

## Quickstart

### Install

```sh
# We recommend using the highest version of Python available on your system,
# check by typing 'python3.' and pushing tab (on some shells you may need to 
# press tab two or three times for tab suggestions).
python3.8 -m pip install -U privex-curconv

# If you can't use 'python3.x -m pip', then you can install using the classic 'pip3'
# command, which will generally use your system default python3 version.
pip3 install -U privex-curconv

# If you want to be able to support caching rates in both Redis and Memcached,
# install privex-curconv with the 'cache' extra:
python3.8 -m pip install -U 'privex-curconv[cache]'

# If you only want either Redis OR Memcached support, you can install with
# the appropriate extra, depending on which cache you want.
python3.8 -m pip install -U 'privex-curconv[redis]'
python3.8 -m pip install -U 'privex-curconv[memcached]'
```

### Using the tool

First figure out whether you can use `conv` - or if you'll need to use `python3 -m privex.curconv`

```sh
# By default, this package should install the 'conv' utility into /usr/local/bin, or ~/.local/bin
# so that you can just type the 'conv' command like so:
conv --help

# If for some reason the 'conv' command doesn't work, you can also run the CLI tool using the
# python3 module executor argument:
python3 -m privex.curconv --help
```

Now lets try it out - it should work out of the box:

Get the exchange rate for **20 USD** to **GBP**

```sh
conv 20 usd to gbp
```

If you'd rather it show `x.xx USD = x.xx GBP` rather than just `x.xx`, you can pass `-f` to enable "full mode":

```sh
conv -f 20 usd to gbp
```

If you want a different number of decimal places on the exchange rates, you can use the flag `-d` / `-dp` / `--dp` / `--decimals`

e.g. `-dp 5` means 5 decimal places, so this would output `14.48240` (at the time of writing):

```sh
conv -dp 5 20 usd to gbp
```

Get all exchange rates for GBP, but only show the **favourite currencies** which by default are: `USD, EUR, GBP, CAD, SEK, TRY`

```sh
conv 1 gbp
```

You can also specify currency amounts with symbols, however, you may need to quote your query if you use symbols, as they may upset your shell:

```sh
conv '£20.00'
conv '$50 to CAD'
conv -f 'CA$30 to £'
```

If you want to dynamically adjust the **favourite currencies** for a single query, you can use the `-c` flag:

```sh
conv -c AUD,NZD,CAD,HKD,CHF 5000 SEK
```

If you want to see ALL available exchange rates for a given currency + amount, you can use the `-a` flag:

```sh
conv -a 20 gbp
```

### Configuring the tool

#### Dynamically pass ENV vars via the system environment

For a single command, you can pass "inline ENV variables" to change the environment for just that
single command:

```sh
CURRENCY_LIST="CHF,CAD,AUD,BZD" DEFAULT_DP=4 CACHE_ADAPTER=redis conv -f '5 usd'
```

If you want to temporarily change certain settings, and have them persist for several commands, but
without having to permanently alter your configuration - you can simply EXPORT the ENV vars in your shell,
and they'll stick until you either close your terminal/shell, or manually unset them:

```sh
export CURRENCY_LIST="CHF,CAD,AUD,BZD"
export DEFAULT_DP=4
export CACHE_ADAPTER=redis

conv -f '5 usd'
conv -f '10.2361 eur'

unset CURRENCY_LIST
conf -f '2.4829 HKD'
unset DEFAULT_DP CACHE_ADAPTER
```

#### Generate and create the default ENV file in one command

You can quickly generate a template default ENV config file at `~/.curconv.env` by running
the tool with the `-Gd` (G = generate, d = default config) flag:

```sh
user@example ~ $ conv -Gd
 >>> Generating ENV file to default location: /Users/example/.curconv.env
 +++ Successfully wrote ENV file to default location: /Users/example/.curconv.env
```

The ENV generator commands generate an ENV config with all major supported ENV vars set to their
default settings, unless it inherited some config vars from the environment, or from a config file.

The settings that it dumps, are the ones that were actually configured in memory at the time of
running the command.

All of the generated ENV vars are optional, so you should remove or comment out any ENV vars which
you aren't changing from the default, so that it's clear which ENV vars you've changed, and which ones
are still set to their defaults.

#### Config search path

By default, the tool searches the following locations in order for a config file, and it will
only use the first file it finds:

- `~/.curconv`
- `~/.curconv.env` (the file which `-Gd` outputs to)
- `/etc/curconv`
- `/etc/curconv.env`

#### Generate an ENV file to stdout

If you want to generate/dump the current configuration in ENV format, but without it being written
to a file, you can use `-G` on it's own, which will generate the same ENV configuration as `-Gd` does,
but outputs it to STDOUT instead of to a file (which you can easily pipe).

```sh
user@example ~ $ conv -G
DEBUG=false
LOG_LEVEL=WARNING
API_BASE=https://api.ratesapi.io/api
API_CACHE_TIME=3600
CACHE_ADAPTER=sqlite
DEFAULT_DP=3
BASE_COIN=EUR
CURRENCY_LIST=USD,EUR,GBP,CAD,SEK,TRY
CUR_SYMBOLS=CA$:CAD,CAD$:CAD,AU$:AUD,AUD$:AUD,NZ$:NZD,NZD$:NZD,$:USD,€:EUR,£:GBP,kr:SEK
```

For example, you could pipe it into `sudo tee` to write the configuration to a file which isn't
writable by your current user, e.g. `/etc/curconv.env`

```sh
conv -G | sudo tee /etc/curconv.env
```

#### Generate an ENV file and output it directly to a file

You can also use `-G` with `-Gf [file]` to generate an ENV file AND output it to a file of your choice.

NOTE: Unlike `-Gd`, the `-Gf` argument does not work on it's own, you must specify `-G` to generate an ENV
configuration, and use `-Gf` to override where it outputs from the default of stdout.

```sh
user@example ~ $ conv -G -Gf /tmp/convtest.env
 >>> Generating ENV file to custom location: /tmp/convtest.env
 +++ Successfully wrote ENV file to custom location: /tmp/convtest.env
```




