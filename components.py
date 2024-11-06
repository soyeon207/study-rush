class Components:
    header = None
    category = None
    assignment = None
    statistic = None
    login = None

    def set_component(self, header, category, assignment, statistic, login):
        self.header = header
        self.category = category
        self.assignment = assignment
        self.statistic = statistic
        self.login = login
