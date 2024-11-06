from datetime import datetime
from utils import *

class AssignmentInfo:
    LIST_COLUMNS = ["", "카테고리", "과제명", "평균 소요 시간", "걸린 시간", ""]

    deadline_date = None
    category = None
    task_name = None
    required_time = 0
    student_number = None

    def __init__(self, student_number, deadline_date, category, task_name):
        self.student_number = student_number
        self.deadline_date = deadline_date
        self.category = category
        self.task_name = task_name

    def complete(self, time):
        self.required_time = time

    def get_required_time(self):
        if self.required_time == 0:
            return ''

        return str(self.required_time) + '분'
    
    def get_button(self):
        if self.required_time == 0:
            return '완료'
        return ''
    
    def difference_date(self):
        now = datetime.now()
        converted_date = datetime.strptime(self.deadline_date, DATE_FORMAT)
        date_difference = now - converted_date 

        day = date_difference.days
        if day == 0:
            return '오늘'
        elif day < 0:
            return 'D'+str(day)
        else:
            return '마감'

    def format_list(self, avg_time):
        return [self.difference_date(), self.category, self.task_name, avg_time, self.get_required_time(), self.get_button()]
        
    def format_file(self, file):
        file.write(f"마감 날짜: {self.deadline_date}\n")
        file.write(f"카테고리: {self.category}\n")
        file.write(f"과제명: {self.task_name}\n")
        file.write(f"걸린 시간: {self.get_required_time()}\n")
        file.write("\n")

    
        