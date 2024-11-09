import re
from .field import Field


class FieldName(Field):
    '''
    A class for storing the name of a contact.
    '''

    def validation(self, value: str) -> str:
        pattern = r"^[a-z]+$"
        if not isinstance(value, str) or not re.match(pattern, value):
            raise FieldNameValueError

        return value


class FieldNameValueError(Exception):
    def __init__(self, message="The name must consist of only letters"):
        super().__init__(message)
