class Field:
    '''
    Base class for record fields.
    '''

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

    def validation(self, value):
        raise NotImplementedError

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = self.validation(new_value)
