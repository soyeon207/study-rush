from tkinter import messagebox
from category_info import CategoryInfo
from assignment_info import AssignmentInfo

class DataCategory:
    data = {
        '문제해결과 알고리즘 과제': CategoryInfo('문제해결과 알고리즘 과제', 1, 2, 15, [15]),
        '러닝페어': CategoryInfo('러닝페어', 0, 1, 0, []),
        '문제해결과 알고리즘 퀴즈': CategoryInfo('문제해결과 알고리즘 퀴즈', 0, 0, 0, [])
    } 

    def complete(self, category, time):
        self.data[category].complete(time)
        
    def format_data(self):
        result = CategoryInfo.LIST_COLUMNS
        for key, value in self.data.items():
            result.append(value.format_list())
        return result
    
    def category_list(self):
        return list(self.data.keys())
    
    def statistic_pie_data(self, category):
        return self.data[category].format_pie()
    
    def statistic_bar_data(self, category):
        return self.data[category].format_bar()
    
    def add_category(self, category):
        if category in self.data:
            messagebox.showwarning("알럿", "이미 있는 카테고리 입니다.")
            return

        self.data[category] = CategoryInfo(category)

    def add_assignment(self, category):
        self.data[category].add_total_count()

    def file(self):
        with open('category.txt', 'w', encoding='utf-8') as file:
            for category, details in self.data.items():
                details.format_file(file)

class DataAssignment:
    data = {
        '2024311126': [
            AssignmentInfo('2024311126', '2024-11-01', '러닝페어', '러닝페어 계획서 제출 (중요중요)'),
            AssignmentInfo('2024311126', '2024-11-03', '문제해결과 알고리즘 과제', '과제 2 제출하기'),
            AssignmentInfo('2024311126', '2024-10-20', '문제해결과 알고리즘 과제', '과제 1 제출하기')]
    }

    def complete(self, student_number, idx, time):
        assignment = self.data[student_number][idx-1]
        assignment.complete(time)
        DataCategory().complete(assignment.category, time)

    def format_data(self, student_number):
        result = [AssignmentInfo.LIST_COLUMNS]
        category_data = DataCategory.data
        
        if student_number in self.data:
            for d in self.data[student_number]:
                result.append(d.format_list(category_data[d.category].get_avg_time()))
        return result
    
    def add_assignment(self, number, date, category, name):
        if number not in self.data:
            self.data[number] = []

        self.data[number].append(AssignmentInfo(number, date, category, name))
        DataCategory().add_assignment(category)

    def file(self, student_number):
        with open('assignments.txt', 'w', encoding='utf-8') as file:
            for assignment in self.data[student_number]:
                assignment.format_file(file)
