from ..user_command import UserCommand
from fields import FieldText

class CommandAllNotes(UserCommand):
    def __init__(self):
        self.name = "all-notes"
        self.description = "Display all notes for all contacts."
        self.pattern = "all-notes"

    def execute(self, args, book):
        all_notes = []

        for record in book.values():
            if hasattr(record, 'notes') and record.notes:
                notes_text = f"Contact '{record.name.value}': {', '.join(record.notes)}"
                all_notes.append(notes_text)
        
        if all_notes:
            msg = "All notes:\n" + "\n".join(all_notes)
        else:
            msg = "No notes found."

        complete = False
        return (msg, complete)
