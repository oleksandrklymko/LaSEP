class Job:
    jobs = []

    def __init__(self, title, starting_salary, vacation_days):
        self.title = title
        self.starting_salary = starting_salary
        self.vacation_days = vacation_days
        Job.jobs.append(self)

    def __repr__(self):
        return self.title
