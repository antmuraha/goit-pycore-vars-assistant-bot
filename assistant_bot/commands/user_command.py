import typing


class ArgumentDescription(typing.TypedDict):
    name: str
    type: str | int
    help: str
    default: typing.Any
    nargs: str


class UserCommand():
    '''
    Abstract command class.
    '''

    def __init__(self):
        # The name of the executable command
        self.name = None
        # Short description of the command
        self.description = None
        # The command call template
        self.pattern = None
        self.args: list[ArgumentDescription] = []

    def execute(self, **kwarg) -> tuple[str, bool]:
        raise NotImplementedError

    def __str__(self):
        return f"Command: {self.name}. Template: {self.pattern}"
