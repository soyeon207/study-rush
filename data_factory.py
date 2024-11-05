from member import Member

class DataFactory:
    member = None

    def set_member(self, member):
        self.member = member

    def get_student_number(self):
        return self.member.student_number
    
    def is_student(self):
        return self.member.is_student()


