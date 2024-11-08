from ..user_command import UserCommand
from fields import FieldTitleValueError, FieldTextValueError, FieldKeywordValueError
from notes_book import NotesBook
from extract_keywords import extract_keywords


class CommandNoteExtractKeywords(UserCommand):
    def __init__(self):
        self.name = "note-extract-keywords"
        self.description = "Extract note keywords using NTLK (Natural Language Toolkit)"
        self.pattern = "note-extract-keywords [title] [-w OR --write] [-m OR --min-rank]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: NotesBook):
        error = self.input_validation(args, book)
        if error:
            return error

        title = args[0]
        flags = args[1:]
        write_keywords = ('-w' in flags) or ('--write' in flags)

        try:
            exist_record = book.get(title)
            if exist_record:
                keywords = extract_keywords(exist_record.text.value)
                print("keywords", keywords)
                keywords = list(map(lambda w: w[1], keywords))

                if write_keywords:
                    exist_record.set_keywords(keywords)
                    msg = "Keywords for notation recorded"
                    complete = False
                    return (msg, complete)

                msg = keywords
                complete = False
                return (msg, complete)

            msg = "Note not exist."
            complete = False
            return (msg, complete)

        except FieldTitleValueError as e:
            return (f"Invalid title value", False)
        except FieldTextValueError as e:
            return (f"Invalid text value", False)
        except FieldKeywordValueError as e:
            return (f"Invalid keyword value", False)
