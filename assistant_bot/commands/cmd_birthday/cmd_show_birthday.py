from address_book import AddressBook
from ..user_command import UserCommand


class CommandShowBirthday(UserCommand):
    def __init__(self):
        self.name = "show-birthday"
        self.description = "The show birthday."
        self.pattern = "show-birthday [username]"

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
            value = exist_record.show_birthday()
            if value:
                return (value, False)

            msg = "You haven't added a birthday yet."
            complete = False
            return (msg, complete)

        msg = "Contact not exist"
        complete = False
        return (msg, complete)
