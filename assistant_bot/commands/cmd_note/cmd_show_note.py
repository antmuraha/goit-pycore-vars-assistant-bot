from ..user_command import UserCommand
from record_note import RecordNote
from notes_book import NotesBook
from print_table import PrintTable
from fields import FieldTitleValueError

class CommandShowNote(UserCommand):
    def __init__(self):
        self.name = "show-note"
        self.description = "Display a note."
        self.pattern = "show-note [title]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: NotesBook):
        result = self.input_validation(args, book)
        if result:
            return result

        title = args[0]

        exist_record = book.find_by_title(title)
        
        if exist_record:
            text = book[title]
            headers = ["Title", "Text"] 
            rows = [[
                f"{title}",
                f"{text}"
            ]]
            table = PrintTable(headers = headers, rows = rows)
            return (table, False)

        msg = "Note does not exist"
        complete = False
        return (msg, complete)
   
    
