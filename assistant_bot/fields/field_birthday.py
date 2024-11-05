from datetime import date, datetime
from .field import Field


class FieldBirthday(Field):
    '''
    A class for storing the birthday of a contact.
    '''
    date_format = "%d.%m.%Y"  # DD.MM.YYYY

    def validation(self, value: str) -> date:
        # DD.MM.YYYY
        try:
            return datetime.strptime(value, FieldBirthday.date_format).date()
        except Exception as e:
            raise FieldBirthdayValueError(
                f"Required format {FieldBirthday.date_format}")


class FieldBirthdayValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
