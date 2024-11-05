from utils import *

class Member:
    type = None
    student_number = None
    name = None

    def __init__(self, type, student_number, name):
        self.type = type
        self.student_number = student_number
        self.name = name

    def valid_check(self):
        if self.type == None and self.name == None:
            return False

        if self.type == STUDENT and self.student_number == None:
            return False
    
        return True

    def displated_name(self):
        return self.student_number + ' '+ self.name
            