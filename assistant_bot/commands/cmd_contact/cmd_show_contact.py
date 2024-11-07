from ..user_command import UserCommand
from address_book import AddressBook


class CommandShowContact(UserCommand):
    def __init__(self):
        self.name = "show-contact"
        self.description = "The show contact."
        self.pattern = "show-contact [username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name = args[0]

        exist_record = book.find_by_name(name)
        if exist_record:
            return (f'{exist_record}', False)

        msg = "Contact not exist"
        complete = False
        return (msg, complete)

