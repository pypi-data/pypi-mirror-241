import asyncio
import json
from typing import List
import openai
import os
import hashlib
import json
import logging
import time
from pathlib import Path
import pandas as pd
from retry import retry
import nest_asyncio
try:
    nest_asyncio.apply()
except RuntimeError:
    def get_or_create_eventloop():
        try:
            return asyncio.get_event_loop()
        except RuntimeError as ex:
            if "There is no current event loop in thread" in str(ex):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                return asyncio.get_event_loop()


    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    nest_asyncio.apply()

from ..session import Session
from .api_threading import execute_api_requests_in_parallel
from .functions import generate_schema_from_function
from .utils import override
