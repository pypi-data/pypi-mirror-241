import torch
from omegaconf.errors import UnsupportedValueType
import datetime
import hashlib
import logging
import os
import asyncio
import threading
from omegaconf import OmegaConf
import contextvars
from collections import OrderedDict

import contextvars

class SingletonMeta(type):