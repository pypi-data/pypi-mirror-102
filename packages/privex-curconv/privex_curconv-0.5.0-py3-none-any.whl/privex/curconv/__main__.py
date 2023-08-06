#!/usr/bin/env python3
import asyncio
import sys
from pathlib import Path
loc = Path(__file__).expanduser().resolve().parent
deps_dir = (loc / 'deps').resolve()

##########
# The following code is for the .pyz self-contained executable version
# of privex-curconv - it adds the .pyz virtual folder to the start of
# the Python search path, to allow both the app and modules to be loaded.
#
if str(loc).rstrip('/').endswith('.pyz') or str(loc).rstrip('/').endswith('.zip'):
    # print(f"loc = {str(loc)}")
    # print(f"deps_dir = {str(deps_dir)}")
    # print(f"sys.path = {sys.path!r}")
    sys.path.insert(0, str(loc))
    # print(f"(inserted) sys.path = {sys.path!r}")
    # sys.path.append(str(deps_dir))


from privex.curconv.app import main

if __name__ == '__main__':
    asyncio.run(main())

