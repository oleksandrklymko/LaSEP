class Employee:
    employee_id = 1

    def __init__(self, sname, date_of_birthday, address):
        self.employee_id = self.__class__.employee_id
        self.sname = sname
        self.date_of_birthday = date_of_birthday
        self.address = address
        self.__class__.employee_id += 1

    def __repr__(self):
        return self.sname + ', Role: ' + self.__class__.__name__
