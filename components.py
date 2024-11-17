class Components:
    header = None
    assignment = None
    task = None
    statistic = None
    login = None

    def set_component(self, header, assignment, task, statistic, login):
        self.header = header
        self.assignment = assignment
        self.task = task
        self.statistic = statistic
        self.login = login
