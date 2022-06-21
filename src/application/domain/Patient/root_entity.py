'''
The root entity responsible for consistency of the aggregate
'''

@dataclass(unsafe_hash=True)
class Patient:
    patient_id: str
    name: str
    dob: date
    email: str
    phone: str
    address: Address