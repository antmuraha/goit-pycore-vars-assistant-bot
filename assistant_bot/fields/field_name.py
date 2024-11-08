import re
from .field import Field


class FieldName(Field):
    '''
    A class for storing the name of a contact.
    '''

    def validation(self, value: str) -> str:
        pattern = r"^[A-Za-zА-Яа-яЁёІіЇїЄєҐґ']{2,}\s+[A-Za-zА-Яа-яЁёІіЇїЄєҐґ']{2,}$"
        if not isinstance(value, str) or not re.match(pattern, value):
            raise FieldNameValueError(
                "Required format:[name(at least 2 letters)] space [surname(at least 2 letters)]"
            )

        return value


class FieldNameValueError(Exception):
    def __init__(self, message="Invalid name format."):  # Default message
        super().__init__(message)
