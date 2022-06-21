'''
The root entity responsible for consistency of the aggregate
'''
from dataclasses import dataclass
from typing import Optional, List, Set
from datetime import date
from ...domain.model import Referral

@dataclass(unsafe_hash=True)
class Procedure:
    reference: str(hash=True)
    procedure: str(init=False, compare=False, hash=False)

class Provider:
    def __init__(self, ref: str, procedures: List[Procedure], available: bool, eta: Optional[date]):
        self.provider_id = ref
        self.eta = eta
        self._available = available
        self._assignments = set()  # type: Set[Referral]
        self._procedures = set()  # type: Set[Procedure]
    def unassign_referral(self, referral: Referral) -> Referral:
        return referral