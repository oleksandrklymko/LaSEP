from employee import Employee


class Stewardess(Employee):

    def __init__(self, sname, date_of_birthday, address):
        super().__init__(sname, date_of_birthday, address)
