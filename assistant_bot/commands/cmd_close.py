from .user_command import UserCommand


class CommandClose(UserCommand):
    def __init__(self):
        self.name = "close"
        self.description = "Exit from the program"
        self.pattern = "close"

    def execute(self, args, book):
        msg = "Good bye!"
        complete = True
        return (msg, complete)
