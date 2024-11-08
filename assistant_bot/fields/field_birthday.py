from datetime import date, datetime
from .field import Field


class FieldBirthday(Field):
    '''
    A class for storing the birthday of a contact.
    '''
    date_format = "%d.%m.%Y"  # DD.MM.YYYY

    def __str__(self):
        return self.value.strftime(FieldBirthday.date_format) 

    def validation(self, value: str) -> date:
        try:
            return datetime.strptime(value, FieldBirthday.date_format).date()
        except Exception as e:
            raise FieldBirthdayValueError(
                f"Required format DD.MM.YYYY")


class FieldBirthdayValueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
