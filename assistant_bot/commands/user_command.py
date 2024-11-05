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

    def input_validation(self, args: list[str], dict: dict):
        '''
        Validation user input arguments for the current command.
        If the arguments of the command are incorrect, an error should be thrown
        '''
        raise NotImplementedError

    def execute(self, **kwarg) -> tuple[str, bool]:
        raise NotImplementedError

    def get_enter_command_message(self):
        return f"Please enter command in the format: {self.pattern}"

    def __str__(self):
        return f"Command: {self.name}. Template: {self.pattern}"

    def __repr__(self):
        return f"Record: \"{self}\""
