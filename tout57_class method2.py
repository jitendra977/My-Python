class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_das(cls, string):
        return cls(*string.split("-"))

    def printer(self):
        return print(f"{date1.year}/{date1.month}/{date1.day}")


date1 = Date.from_das("2020-08-20")
date1.printer()
