# from colorama import Fore, Style
from parse_input import parse_input
from completer import completer, save_history_to_file
from address_book import AddressBook
from notes_book import NotesBook
from print_table import PrintTable
from commands import CommandHello, CommandExit, CommandClose, \
    CommandAddContact, CommandEditContact, CommandDeleteContact, CommandShowContact, CommandAllContacts, \
    CommandAddAddress, CommandEditAddress, CommandDeleteAddress, \
    CommandAddBirthday, CommandDeleteBirthday, CommandShowBirthday, CommandGetUpcomingBirthdays, \
    CommandAddPhone, CommandEditPhone, CommandDeletePhone, CommandShowPhones, \
    CommandAddEmail, CommandEditEmail, CommandDeleteEmail, \
    CommandAddNote, CommandEditNote, CommandDeleteNote, CommandAllNotes, CommandShowNote
import store


common_command_list = [CommandHello(), CommandExit(), CommandClose()]

address_command_list = [CommandAddContact(), CommandEditContact(), CommandDeleteContact(), CommandShowContact(), CommandAllContacts(),
                        CommandAddAddress(), CommandEditAddress(), CommandDeleteAddress(),
                        CommandAddBirthday(), CommandDeleteBirthday(), CommandShowBirthday(), CommandGetUpcomingBirthdays(),
                        CommandAddPhone(), CommandEditPhone(), CommandDeletePhone(), CommandShowPhones(),
                        CommandAddEmail(), CommandEditEmail(), CommandDeleteEmail(),
                        CommandAddNote(), CommandEditNote(), CommandDeleteNote(), CommandAllNotes(), CommandShowNote()
                        ]
notes_command_list = [CommandAddNote(), CommandEditNote(), CommandDeleteNote(), CommandAllNotes()]


def get_help():
    commands = []
    all = common_command_list + address_command_list + notes_command_list
    for cmd in all:
        exist = next((x for x in commands if x[0] == cmd.pattern), None)
        if not exist:
            commands.append((cmd.pattern, cmd.description))
    text = list(
        map(lambda cmd: f"{Fore.BLUE}{cmd[0]}{Style.RESET_ALL} - {cmd[1]}", commands))
    return "\n".join(text)


def get_all_commands():
    commands = ["help"]
    all = common_command_list + address_command_list + notes_command_list
    for cmd in all:
        exist = next((x for x in commands if x == cmd.pattern), None)
        if not exist:
            commands.append(cmd.pattern)
    return commands


def main():
    addressBook = AddressBook()
    notesBook = NotesBook()

    # Uncomment after full implementation
    # addressBook = None
    # notesBook = None
    # try:
    #     addressBook, notesBook = store.load_data()
    # except Exception as e:
    #     print(f"{e}")
    #     addressBook = AddressBook()
    #     notesBook = NotesBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = completer(get_all_commands())
        if not len(user_input.strip()):
            print("Please enter a command.")
            continue

        command, *args = parse_input(user_input)

        if command == "help":
            msg = get_help()
            print(msg)
            continue

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
                if isinstance(msg, PrintTable):
                    msg.show()
                else:
                    print(msg)
            if complete:
                # Uncomment after full implementation
                # store.save_data([addressBook, notesBook])
                save_history_to_file()
                exit(0)
        else:
            print(f"Unknown command <{command}>.")
