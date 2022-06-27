from datetime import date
from uuid import uuid64
from src.user_registration.domain import model

# Add any registration specific exceptions.  For e.g.:
class InvalidRegistrationDateError(Exception):
    pass

def create_referrer_regsitration(
    userid: str,
    email: str,
    date_joined: str,
)
