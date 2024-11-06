from fields import FieldName, FieldPhone, FieldBirthday



class RecordContact:
    '''
    A class to store information about a contact, including name and phone list.
    '''

    def __init__(self, name):
        self.name = FieldName(name)
        self.phones: list[FieldPhone] = []
        self.birthday: FieldBirthday = None
        self.email = None
        self.address = None

    def __str__(self):
        birthday_str = f" ({self.birthday})" if self.birthday else ''
        return f"Contact name: {self.name.value}{birthday_str}, phones: {', '.join(p.value for p in self.phones)}"

    def __repr__(self):
        return f"Record: \"{self}\""

    def add_phone(self, phone: str):
        if not self.find_phone(phone):
            self.phones.append(FieldPhone(phone))
        else:
            raise NotImplementedError 

    def add_birthday(self, birthday: str):
        self.birthday = FieldBirthday(birthday)
        
    #TODO show_birthday()    

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, phone: str, new_phone: str):
        record = next(
            (x for x in self.phones if x.value == phone), None)

        if record:
            record.value = new_phone

    def find_phone(self, phone: str) -> FieldPhone | None:
        record = next(
            (x for x in self.phones if x.value == phone), None)

        return record
    
    def add_email(self, email): # email: FieldEmail
        raise NotImplementedError
        # self.email = FieldEmail(email)

    def edit_email(self, new_email): # new_email: FieldEmail
        raise NotImplementedError
        # self.email = FieldEmail(new_email)

    def remove_email(self):
        self.email = None

    def add_address(self, address): # address: FieldAddress
        raise NotImplementedError
        # self.address = FieldAddress(address)

    def edit_address(self, new_address): # new_address: FieldAddress
        raise NotImplementedError
        # self.address = FieldAddress(new_address)

    def remove_address(self):
        self.address = None



class RecordPhoneAlreadyExistError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
