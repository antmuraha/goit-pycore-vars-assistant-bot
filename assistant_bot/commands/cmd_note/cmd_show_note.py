from ..user_command import UserCommand
from record_note import RecordNote
from notes_book import NotesBook
from print_table import PrintTable
from fields import FieldTitleValueError
from messages import Messages

class CommandShowNote(UserCommand):
    def __init__(self):
        self.name = "show-note"
        self.description = "Display a note."
        self.args = [
             {"name": "title", "help": Messages.HELP_FIELD_TITLE.value, "type": str},
        ]

    def execute(self, args, book: NotesBook):
        title = args.title

        exist_record = book.find_by_title(title)
        
        if exist_record:
            note = book[title]
            headers = ["Title", "Text", "Keywords"] 
            rows = [[
                f"{title}",
                f"{note.text}",
                ", ".join([f"{k}" for k in note.keywords]),
            ]]
            table = PrintTable(headers = headers, rows = rows)
            return (table, False)

        msg = "Note doesn't exist."
        complete = False
        return (msg, complete)
   
    
