
class PrintTable():
    def __init__(self, headers: list[str], rows: list[list[str]]):
        self.headers = headers
        self.rows = rows

    def show(self):
        print("Headers:", self.headers)
        print("Rows:", self.rows)
