import re
from .field import Field

class FieldEmail(Field):
    '''
    A class for storing the email of a contact.
    '''
    def validation(self, value: str) -> str:
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        
        if not isinstance(value, str) or not re.match(email_pattern, value):
            raise FieldEmailValueError("Incorrect email format.")

        return value

class FieldEmailValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
