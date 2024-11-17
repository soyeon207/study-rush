from tkinter import messagebox
from assignment_info import AssignmentInfo
from study_info import StudyInfo

class DataAssignment:
    data = {}

    def complete(self, assignment, time):
        if assignment in self.data:
            self.data[assignment].complete(time)
        
    def format_data(self):
        result = [AssignmentInfo.LIST_COLUMNS]
        for value in self.data.values():
            result.append(value.format_list())
        return result
    
    def assignment_list(self):
        return list(self.data.keys())
    
    def statistic_pie_data(self, assignment):
        return self.data[assignment].format_pie()
    
    def statistic_bar_data(self, assignment):
        return self.data[assignment].format_bar()
    
    def add_assignment(self, assignment):
        if assignment in self.data:
            messagebox.showwarning("알럿", "이미 있는 카테고리 입니다.")
            return

        self.data[assignment] = AssignmentInfo(assignment)

    def add_study(self, assignment):
        self.data[assignment].add_total_count()

    def file(self):
        with open('assignment.txt', 'w', encoding='utf-8') as file:
            for details in self.data.values():
                details.format_file(file)

class DataStudy:
    data = {}

    def complete(self, student_number, idx, time):
        study = self.data[student_number][idx-1]
        study.complete(time)
        DataAssignment().complete(study.assignment, time)

    def format_data(self, student_number):
        result = [StudyInfo.LIST_COLUMNS]
        assignment_data = DataAssignment.data
        
        if student_number in self.data:
            for d in self.data[student_number]:
                result.append(d.format_list(assignment_data[d.assignment].get_avg_time()))
        return result
    
    def add_study(self, number, date, assignment, name):
        if number not in self.data:
            self.data[number] = []

        self.data[number].append(StudyInfo(number, date, assignment, name))
        DataAssignment().add_study(assignment)

    def file(self, student_number):
        with open('studys.txt', 'w', encoding='utf-8') as file:
            for study in self.data[student_number]:
                study.format_file(file)
