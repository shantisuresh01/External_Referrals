# pylint: disable=too-few-public-methods
from datetime import date
from typing import Optional, List
from dataclasses import dataclass


class Command:
    pass


@dataclass
class Match(Command):
    orderid: str
    sku: str
    qty: int


@dataclass
class CreateClinic(Command):
    ref: str
    treatment: List[str]
    doctors: Optional[str] = None


@dataclass
class ChangeClinic(Command):
    ref: str

@dataclass
class CancelPatient(Command):
    ref: str