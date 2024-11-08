from .field import Field


class FieldKeyword(Field):
    '''
    A class for keyword field.
    '''

    def validation(self, value: str) -> str:
        if not isinstance(value, str) or len(value) == 0:
            raise FieldKeywordValueError(
                "The value must contain at least one character.")

        return value


class FieldKeywordValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
