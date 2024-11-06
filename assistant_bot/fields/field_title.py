from .field import Field

class FieldTitle(Field):
    '''
    A class for storing the title of a contact or an entry.
    '''
    def validation(self, value: str) -> str:
        if not isinstance(value, str) or len(value) == 0:
            raise FieldTitleValueError("The value must contain at least one character.")

        return value

class FieldTitleValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
