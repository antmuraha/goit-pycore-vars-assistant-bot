from ..user_command import UserCommand
from record_contact import RecordContact
from fields import FieldName, FieldNameValueError
from address_book import AddressBook


class CommandEditContact(UserCommand):
    def __init__(self):
        self.name = "edit-contact"
        self.description = "The edit contact."
        self.pattern = "edit-contact [username] [new_username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

        if len(params) == 1:
            msg = "Please enter a new_username."
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        result = self.input_validation(args, book)
        if result:
            return result

        name = args[0]
        new_name = args[1]

        try:
            exist_record = book.find_by_name(name)
            if exist_record:
                renamed = exist_record.rename(new_name)
                if renamed:
                    book[new_name] = book[name]
                    del book[name]
                    msg = "Contact renamed."
                    complete = False
                    return (msg, complete)

            msg = "Contact not exist."
            complete = False
            return (msg, complete)

        except FieldNameValueError as e:
            return (f"{e}", False)
