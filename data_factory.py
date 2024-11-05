from member import Member

class DataFactory:
    member = None

    def __init__(self):
        pass

    def set_member(self, member):
        self.member = member

    def get_student_number(self):
        return self.member.student_number


