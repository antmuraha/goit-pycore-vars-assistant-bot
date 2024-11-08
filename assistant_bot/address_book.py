import typing
from collections import UserDict
from datetime import datetime, timedelta
from record_contact import RecordContact


# Define the type for a single person
class PersonCongratulation(typing.TypedDict):
    name: str
    congratulation_date: str


# Define the type for a list of such dictionaries
PeopleCongratulationList = typing.List[PersonCongratulation]

class AddressBook(UserDict[RecordContact]):
    def __init__(self):
        self.data = {}
        self.length_week = 7
        self.length_work_week = 5
        self.date_format = "%d.%m.%Y"  # DD.MM.YYYY
        self.today = datetime.today().date()

    def add_record(self, record):
        '''Adds an entry to the address book.'''
        self.data[record.name.value] = record

    def remove_record_by_index(self, index):
        '''Deletes a record by its serial number.'''
        try:
            key = list(self.data.keys())[index]
            del self.data[key]
        except IndexError:
            print("The record with the specified index was not found.")

    def remove_record_by_name(self, name):
        '''Deletes a record by name.'''
        if name in self.data:
            del self.data[name]
        else:
            print("No record with the specified name was found.")

    def find_by_name(self, name: str) -> RecordContact | None:
        '''Searches for a record by name.'''
        return self.data.get(name)

    def find_by_email(self, email):
        '''Searches for a record by email.'''
        for record in self.data.values():
            if hasattr(record, 'email') and record.email.value == email:
                return record
        return "No record found with this email."

    def find_by_phone(self, phone):
        '''Searching for a recording by phone.'''
        for record in self.data.values():
            if hasattr(record, 'phones') and phone in [p.value for p in record.phones]:
                return record
        return "No record found with this phone number."
    
    def edit_contact(self, name, new_name):
        raise NotImplementedError

    def show_birthday(self, name):
        raise NotImplementedError

    def remove_record_by_name(self, name):
        raise NotImplementedError

    def show_upcoming_birthday(self, number=7) -> PeopleCongratulationList:
        upcoming: PeopleCongratulationList = []
        for name in self.data:
            record = self.data[name]
            if not record.birthday:
                continue

            birthday = record.birthday.value
            birthday_this_year = birthday.replace(year=self.today.year)

            if birthday_this_year < self.today:
                birthday_this_year = birthday_this_year.replace(
                    year=self.today.year + 1)

            diff = (birthday_this_year - self.today).days
            if diff < self.forward_days:
                weekday = birthday_this_year.weekday()
                if weekday + 1 > self.length_work_week:
                    days = self.length_week - weekday
                    birthday_this_year = birthday_this_year + \
                        timedelta(days=days)
                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": birthday_this_year.strftime(self.date_format)
                })

        return upcoming
    
