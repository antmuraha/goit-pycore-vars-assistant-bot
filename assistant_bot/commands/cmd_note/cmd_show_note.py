from ..user_command import UserCommand
from record_note import RecordNote


class CommandShowNote(UserCommand):
    def __init__(self):
        self.name = "show-note"
        self.description = "The show note."
        self.pattern = "show-note [title]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book):
        result = self.input_validation(args, book)
        if result:
            return result

        title, = args

        exist_record = book.show_note(title)
        if exist_record:
            return (f'{exist_record}', False)

        msg = "Note does not exist"
        complete = False
        return (msg, complete)
