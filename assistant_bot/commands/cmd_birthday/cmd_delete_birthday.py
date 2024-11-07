from address_book import AddressBook
from ..user_command import UserCommand


class CommandDeleteBirthday(UserCommand):
    def __init__(self):
        self.name = "delete-birthday"
        self.description = "The delete birthday."
        self.pattern = "delete-birthday [username]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: AddressBook):
        error = self.input_validation(args, book)
        if error:
            return error

        name, = args

        exist_record = book.find_by_name(name)
        if exist_record:
            value = exist_record.show_birthday()
            if value:
                exist_record.delete_birthday()
                return (f"Birthday value has been removed", False)

            msg = "You haven't added a birthday yet."
            complete = False
            return (msg, complete)

        msg = "Contact not exist"
        complete = False
        return (msg, complete)
