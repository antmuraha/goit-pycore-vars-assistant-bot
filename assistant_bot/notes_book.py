from collections import UserDict
from record_note import RecordNote
from fields import FieldTitle


class NotesBook(UserDict):
    '''
    A class for storing and managing notes.
    '''

    def __init__ (self):
        self.data = {}
    
    def __str__(self):
        if not self.data:
            return "No notes available."
        
        notes = "\n".join([f"Title: {note.title}, Content: {note.text[:30]}..." for note in self.data])
        return f"Notes: \n{notes}"
    
    def add_record(self, title: str, text: str):
        self.data[title] = RecordNote(title, text)

    def remove_record(self, title):
        if title in self.data:
            return self.data.pop(title)
 
    def find_by_title(self, title) -> RecordNote | None:
        return self.data.get(title)
    
    def edit_title(self, old_title, new_title):
        if old_title in self.data:
            self.data[new_title] = self.data.pop(old_title)

