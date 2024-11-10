import re
from .field import Field


class FieldName(Field):
    '''
    A class for storing the name of a contact.
    '''

    def validation(self, value: str) -> str:
        if not isinstance(value, str):
            raise FieldNameValueError

        return value


class FieldNameValueError(Exception):
    def __init__(self, message="The name must consist of only letters"):
        super().__init__(message)
