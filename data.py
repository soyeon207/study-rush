from tkinter import messagebox
from assignment_info import AssignmentInfo
from task_info import TaskInfo

class DataAssignment:
    data = {}

    # 과제를 추가하는 메서드
    def add_assignment(self, assignment):
        if assignment in self.data:
            messagebox.showwarning("알럿", "이미 있는 과제 입니다.")
            return

        self.data[assignment] = AssignmentInfo(assignment)

    # 과제를 완료하는 메서드
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
    
    

    def add_task(self, assignment):
        self.data[assignment].add_total_count()

    def file(self):
        with open('assignment.txt', 'w', encoding='utf-8') as file:
            for details in self.data.values():
                details.format_file(file)

class DataTask:
    data = {}

    # 학생 별 과제를 추가하는 메서드
    def add_task(self, number, date, assignment, name):
        if number not in self.data:
            self.data[number] = []

        self.data[number].append(TaskInfo(number, date, assignment, name))
        DataAssignment().add_task(assignment)
        
    # 학생 별 과제를 완료하는 메서드
    def complete(self, student_number, idx, time):
        task = self.data[student_number][idx-1]
        task.complete(time)
        DataAssignment().complete(task.assignment, time)

    def format_data(self, student_number):
        result = [TaskInfo.LIST_COLUMNS]
        assignment_data = DataAssignment.data
        
        if student_number in self.data:
            for d in self.data[student_number]:
                result.append(d.format_list(assignment_data[d.assignment].get_avg_time()))
        return result
    
    

    def file(self, student_number):
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            for task in self.data[student_number]:
                task.format_file(file)
