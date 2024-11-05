import re
from .field import Field


class FieldPhone(Field):
    '''
    A class for storing the phone of a contact.
    '''

    def validation(self, value: str) -> str:
        regPhone = r"\d{10}"
        if type(value) != str or not re.fullmatch(regPhone, value):
            raise FieldPhoneValueError

        return value


class FieldPhoneValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
