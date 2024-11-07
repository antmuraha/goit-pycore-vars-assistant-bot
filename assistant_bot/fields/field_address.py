import re
from .field import Field

min_value_length = 5


class FieldAddress(Field):
    '''
    A class for storing the address of a contact.
    '''

    def validation(self, value: str) -> str:

        if len(value) <= min_value_length:
            raise FieldAddressValueError(
                f"Incorrect address format.\nThe length of the address must not be shorter than {min_value_length} characters.")

        return value


class FieldAddressValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
