import re
from .field import Field


class FieldPhone(Field):
    '''
    A class for storing the phone of a contact.
    '''

    def validation(self, value: str) -> str:
        value = f"{value}"
        regPhone = r"\d{10}"
        if type(value) != str or not re.fullmatch(regPhone, f"{value}"):
            raise FieldPhoneValueError

        return value


class FieldPhoneValueError(Exception):
    def __init__(self, *args):
        super().__init__("The phone number must be 10 characters long.")
