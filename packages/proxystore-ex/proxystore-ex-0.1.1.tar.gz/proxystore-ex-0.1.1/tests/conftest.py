from __future__ import annotations

import asyncio
import sys
from typing import Generator

import pytest

try:
    import pydaos
except ImportError:
    from testing.mocked import pydaos

    sys.modules['pydaos'] = pydaos

try:
    import pymargo
except ImportError:
    from testing.mocked import pymargo

    sys.modules['pymargo'] = pymargo
    sys.modules['pymargo.bulk'] = pymargo
    sys.modules['pymargo.core'] = pymargo

try:
    import ucp
except ImportError:
    from testing.mocked import ucp

    sys.modules['ucp'] = ucp

from testing.connectors import connectors
from testing.connectors import daos_connector
from testing.connectors import margo_connector
from testing.connectors import ucx_connector
from testing.connectors import zmq_connector


@pytest.fixture(scope='session')
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Get event loop.

    Share event loop between all tests. Necessary for session scoped asyncio
    fixtures.

    Source: https://github.com/pytest-dev/pytest-asyncio#event_loop
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
