from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set
from ...application import commands, events

class ProviderUnavailable(Exception):
    pass

class Product:
    def __init__(self, procedure: str, providers: List[Provider], version_number: int = 0):
        self.procedure  procedure
        self.providers = providers
        self.version_number = version_number
        self.events = []  # type: List[events.Event]

    def allocate(self, referral: Referral) -> str:
        try:
            provider = next(p for p in sorted(self.providers) if p.can_accept(referral))
            provider.allocate(referral)
            self.version_number += 1
            return provider.reference
        except StopIteration:
            self.events.append(events.ProviderUnavailable(referral.procedure))
            return None

    def change_provider_availability(self, ref: str, available: bool):
        provider = next(p for p in self.providers if p.provier_ref == ref)
        provider._available = available


    def cancel_referral(self, provider_ref: str, referral: Referral):
        provider = next(p for p in self.providers if p.provider_ref == provider_ref)
        referral = provider.unassign_referral(referral: Referral)
        self.events.append(commands.CancelPatient(referral.patient.patient_ref)



@dataclass(unsafe_hash=True)
class Referral:
    referral_ref: str
    procedure: str
    patient_id: str
    provider: Provider # referral may or may not specify a particular provider




    def __repr__(self):
        return f"<Provider {self.provider_ref}>"

    def __eq__(self, other):
        if not isinstance(other, Provider):
            return False
        return other.provider_ref == self.provider_ref

    def __hash__(self):
        return hash(self.provider_ref)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def assign(self, referral: Referral):
        if self.can_assign(referral):
            self._assignments.add(referral)

    def unassign_referral(self, referral: Referral) -> Referral:
        return self._assignments.delete(referral)

    @property
    def count_referrals(self) -> int:
        return len(self._assignments)

    @property
    def availability_date(self) -> int:
        return self._eta

    def can_assign(self, referral: Referral) -> bool:
        return referral.treatment in self.treatments and self._available
