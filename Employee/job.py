class Job:

    def __init__(self, title, salary, vacation_days):
        self.title = title
        self.salary = salary
        self.vacation_days = vacation_days

    def __repr__(self):
        return self.title
