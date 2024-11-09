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
        self.created = datetime.now().strftime("%d.%m.%Y %H:%M")
        self.updated = None

    def __str__(self):
        birthday_str = f" ({self.birthday})" if self.birthday else ''
        return f"Contact name: {self.name.value}{birthday_str}, phones: {', '.join(p.value for p in self.phones)}"

    
    def rename(self, new_name):
        self.name = FieldName(new_name)
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")
        return self.name.value == new_name

    def add_phone(self, phone: str):
        if not self.find_phone(phone):
            self.phones.append(FieldPhone(phone))
            self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    def add_birthday(self, birthday: str):
        self.birthday = FieldBirthday(birthday)
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")
        
    def show_birthday(self):
        if self.birthday:
            return self.birthday.value.strftime("%d.%m.%Y")
        
    def delete_birthday(self):
        self.birthday = None
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    def remove_phone(self, phone: str) -> bool:
        count = len(self.phones)
        self.phones = list(filter(lambda p: p.value != phone, self.phones))
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")
        return len(self.phones) != count

    def edit_phone(self, phone: FieldPhone, new_phone: FieldPhone):
        record = next(
            (x for x in self.phones if x.value == phone), None)

        if record:
            record.value = new_phone

        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")
        return record

    def find_phone(self, phone: FieldPhone) -> FieldPhone | None:
        record = next(
            (x for x in self.phones if x.value == phone), None)

        return record

    def show_phones(self):
        '''Show all phones'''
        return [p.value for p in self.phones]
    
    def add_email(self, email: FieldEmail):  
        self.email = FieldEmail(email)
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    def edit_email(self, new_email: FieldEmail): 
        self.email = FieldEmail(new_email)
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    def remove_email(self):
        self.email = None
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    def add_address(self, address: FieldAddress): 
        self.address = FieldAddress(address)
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    def edit_address(self, new_address: FieldAddress): 
        self.address = FieldAddress(new_address)
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    def remove_address(self):
        self.address = None
        self.updated = datetime.now().strftime("%d.%m.%Y %H:%M")



class RecordPhoneAlreadyExistError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
