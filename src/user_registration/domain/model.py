from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

@dataclass(unsafe_hash=True)
class User:
    userid: str
    USERNAME_FIELD = 'email'
    userid: str
    email: str
    date_joined: str
    is_active: bool
    is_staff: bool
    is_referrer: bool
