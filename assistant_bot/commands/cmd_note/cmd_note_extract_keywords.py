from ..user_command import UserCommand
from fields import FieldTitleValueError, FieldTextValueError, FieldKeywordValueError
from notes_book import NotesBook
from extract_keywords import extract_keywords
from print_table import PrintTable


class CommandNoteExtractKeywords(UserCommand):
    def __init__(self):
        self.name = "note-extract-keywords"
        self.description = "Extract note keywords using NTLK (Natural Language Toolkit)"
        self.pattern = "note-extract-keywords [title] [-w OR --write]"

    def input_validation(self, params, book):
        if len(params) == 0:
            msg = self.get_enter_command_message()
            complete = False
            return (msg, complete)

    def execute(self, args, book: NotesBook):
        error = self.input_validation(args, book)
        if error:
            return error

        title = " ".join(list(map(lambda x: "" if (x == '-w') or (x == '--write') else x,args)))
        flags = args[1:]
        write_keywords = ('-w' in flags) or ('--write' in flags)

        try:
            exist_record = book.get(title)
            if exist_record:
                keywords = extract_keywords(exist_record.text.value)

                if write_keywords:
                    keywords = list(map(lambda w: w[1], keywords))
                    exist_record.set_keywords(keywords)
                    msg = "Keywords for notation recorded"
                    complete = False
                    return (msg, complete)

                headers = ["Rank", "Keyword"]
                rows = []
                for item in keywords:
                    rows.append([
                        f"{round(item[0], 1)}",
                        f"{item[1]}",
                    ])
                table = PrintTable(headers=headers, rows=rows)
                complete = False
                return (table, complete)

            msg = "Note not exist."
            complete = False
            return (msg, complete)

        except FieldTitleValueError as e:
            return (f"Invalid title value. {e}", False)
        except FieldTextValueError as e:
            return (f"Invalid text value. {e}", False)
        except FieldKeywordValueError as e:
            return (f"Invalid keyword value. {e}", False)
