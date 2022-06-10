'''
The root entity responsible for consistency of the aggregate
'''
@ dataclass(unsafe_hash=True)
class Address:
    reference: str
    street_address: str
    city: str
    state: str
    zip: int
