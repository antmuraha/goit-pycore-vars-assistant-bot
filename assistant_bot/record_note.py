from fields import FieldText, FieldTitle, FieldKeyword


class RecordNote:
    '''
    A class to store information about a note, including text.
    '''

    def __init__(self, title, text):
        self.title = FieldTitle(title)
        self.text = FieldText(text)
        self.keywords: list[FieldKeyword] = []

    def __str__(self):
        keywords = list(map(lambda k: f"{k}", self.keywords))
        return f"Note text: {self.text} Keywords:{keywords}"

    def edit_text(self, new_text):
        self.text = FieldText(new_text)

    def set_keywords(self, keywords: list[str]):
        new_keywords = []
        for word in keywords:
            new_keywords.append(FieldKeyword(word))
        self.keywords = new_keywords[:5]
