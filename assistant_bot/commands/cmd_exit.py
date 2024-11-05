from .user_command import UserCommand


class CommandExit(UserCommand):
    def __init__(self):
        self.name = "exit"
        self.description = "Exit from the program"
        self.pattern = "exit"

    def execute(self, args, book):
        msg = "Good bye!"
        complete = True
        return (msg, complete)
