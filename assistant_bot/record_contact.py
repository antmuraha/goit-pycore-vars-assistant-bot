from fields import FieldName, FieldPhone, FieldBirthday
from fields import FieldName, FieldPhone, FieldBirthday, FieldAddress, FieldEmail
from datetime import datetime


class RecordContact:
    '''
    A class to store information about a contact, including name and phone list.
    '''

    def __init__(self, name):
        self.name = FieldName(name)
        self.phones: list[FieldPhone] = []
        self.birthday: FieldBirthday = None
        self.email: FieldEmail = None
        self.address: FieldAddress = None

    def __str__(self):
        birthday_str = f" ({self.birthday})" if self.birthday else ''
        return f"Contact name: {self.name.value}{birthday_str}, phones: {', '.join(p.value for p in self.phones)}"

    def __repr__(self):
        return f"Record: \"{self}\""

    def add_phone(self, phone: str):
        if not self.find_phone(phone):
            self.phones.append(FieldPhone(phone))
        else:
            raise ValueError 

    def add_birthday(self, birthday: str):
        self.birthday = FieldBirthday(birthday)
        
    def show_birthday(self):
        if self.birthday:
            return self.birthday.strftime("%d-%m-%Y")
        else:
            return "You haven't added a birthday yet."

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, phone: FieldPhone, new_phone: FieldPhone):
        record = next(
            (x for x in self.phones if x.value == phone), None)

        if record:
            record.value = new_phone

    def find_phone(self, phone: FieldPhone) -> FieldPhone | None:
        record = next(
            (x for x in self.phones if x.value == phone), None)

        return record
    
    def add_email(self, email: FieldEmail):  
        self.email = FieldEmail(email)

    def edit_email(self, new_email: FieldEmail): 
        self.email = FieldEmail(new_email)

    def remove_email(self):
        self.email = None

    def add_address(self, address: FieldAddress): 
        self.address = FieldAddress(address)

    def edit_address(self, new_address: FieldAddress): 
        self.address = FieldAddress(new_address)

    def remove_address(self):
        self.address = None



class RecordPhoneAlreadyExistError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
