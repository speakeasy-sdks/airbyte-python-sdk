from __future__ import annotations
from enum import Enum

class JobTypeEnum(str, Enum):
    SYNC = "sync"
    RESET = "reset"
