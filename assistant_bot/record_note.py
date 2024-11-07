from fields import FieldText

class RecordNote:
    '''
    A class to store information about a note, including text.
    '''

    def __init__(self, title, text):
        self.text = FieldText(text)

    def __str__(self):
        return f"Note text: {self.text}"

    def __repr__(self):
        return f"RecordNote(text={self.text[:30]!r})"
    
    
    