from datetime import datetime
from utils import *

class TaskInfo:
    LIST_COLUMNS = ["", "과제명", "설명", "평균 소요 시간", "걸린 시간", ""]

    deadline_date = None        # 마감일자
    assignment = None           # 과제명
    task_name = None            # 설명
    required_time = 0           # 걸린 시간
    student_number = None       # 학번

    def __init__(self, student_number, deadline_date, assignment, task_name):
        self.student_number = student_number
        self.deadline_date = deadline_date
        self.assignment = assignment
        self.task_name = task_name

    # 과제 완료
    def complete(self, time):
        self.required_time = time

    def get_required_time(self):
        return str(self.required_time) + '분' if self.required_time != 0 else ''
    
    def get_button(self):
        return '완료' if self.required_time == 0 else ''
    
    def difference_date(self):
        now = datetime.now()
        converted_date = datetime.strptime(self.deadline_date, DATE_FORMAT)
        day_difference = (now - converted_date).days

        if self.required_time > 0:
            return '완료'
        elif day_difference == 0:
            return '오늘'
        elif day_difference < 0:
            return f"D{day_difference}"
        else:
            return '마감'

    def format_list(self, avg_time):
        return [self.difference_date(), self.assignment, self.task_name, avg_time, self.get_required_time(), self.get_button()]
        
    def format_file(self, file):
        file.write(f"마감 날짜: {self.deadline_date}\n")
        file.write(f"과제명: {self.assignment}\n")
        file.write(f"설명: {self.task_name}\n")
        file.write(f"걸린 시간: {self.get_required_time()}\n")
        file.write("\n")

    
        