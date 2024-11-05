import readline
from parse_input import parse_input
from address_book import AddressBook
from notes_book import NotesBook
import constants
from commands import CommandHello, CommandExit, CommandAddContact

common_command_list = [CommandHello(), CommandExit()]
address_command_list = [CommandAddContact()]
notes_command_list = []


try:
    # Load the history from the file if it exists
    readline.read_history_file(constants.history_file)
except FileNotFoundError:
    # If no history file exists, it will be created when commands are saved
    pass


def main():
    addressBook = AddressBook()
    notesBook = NotesBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not len(user_input.strip()):
            print("Please enter a command.")
            continue

        command, *args = parse_input(user_input)

        # Find the target class of the command
        book = None
        cmd = None
        common_cmd = next(
            (x for x in common_command_list if x.name == command), None)
        if common_cmd:
            cmd = common_cmd
        else:
            address_cmd = next(
                (x for x in address_command_list if x.name == command), None)
            if address_cmd:
                cmd = address_cmd
                book = addressBook
            else:
                cmd = next(
                    (x for x in notes_command_list if x.name == command), None)
                book = notesBook

        if cmd:
            msg, complete = cmd.execute(args, book)
            if msg:
                print(msg)
            if complete:
                readline.write_history_file(constants.history_file)
                exit(0)
        else:
            print(f"Unknown command <{command}>.")
