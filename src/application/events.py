# pylint: disable=too-few-public-methods
from dataclasses import dataclass


class Event:
    pass


@dataclass
class ProviderUnavailable(Event):
    sku: str

@dataclass
class CancelPatient(Event):
    patient_ref: str