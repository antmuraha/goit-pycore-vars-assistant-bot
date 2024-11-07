from .field import Field

class FieldText(Field):
    '''
    A class for storing generic text fields.
    '''
    def validation(self, value: str) -> str:
        if not isinstance(value, str) or len(value) == 0:
            raise FieldTextValueError("The value must contain at least one character.")

        return value

class FieldTextValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
