class Components:
    header = None
    assignment = None
    study = None
    statistic = None
    login = None

    def set_component(self, header, assignment, study, statistic, login):
        self.header = header
        self.assignment = assignment
        self.study = study
        self.statistic = statistic
        self.login = login
