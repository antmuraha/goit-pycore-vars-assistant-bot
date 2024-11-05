from .field import Field


class FieldName(Field):
    '''
    A class for storing the name of a contact.
    '''

    def validation(self, value: str) -> str:
        if type(value) != str or len(value) == 0:
            raise FieldNameValueError

        return value


class FieldNameValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
