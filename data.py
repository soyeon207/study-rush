from datetime import datetime
from tkinter import messagebox
from utils import *
from category_info import CategoryInfo

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

        print(result)
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
        '2024311126': [{
            '마감 날짜': '2024-11-01',
            '카테고리': '러닝페어',
            '과제명': '러닝페어 계획서 제출 (중요중요)',
            '걸린 시간': '',
            '버튼': '완료'
        },
        {
            '마감 날짜': '2024-11-03',
            '카테고리': '문제해결과 알고리즘 과제',
            '과제명': '과제 2 제출하기',
            '걸린 시간': '',
            '버튼': '완료'
        },
        {
            '마감 날짜': '2024-10-20',
            '카테고리': '문제해결과 알고리즘 과제',
            '과제명': '과제 1 제출하기',
            '걸린 시간': '15분',
            '버튼': ''
        }]
    }

    def complete(self, student_number, idx, time):
        assignment = self.data[student_number][idx-1]
        assignment['걸린 시간'] = str(time) + '분'
        assignment['버튼'] = ''
        DataCategory().complete(assignment['카테고리'], time)

    def difference_date(self, target):
        now = datetime.now()
        converted_date = datetime.strptime(target, DATE_FORMAT)
        date_difference = now - converted_date 

        day = date_difference.days
        if day == 0:
            return '오늘'
        elif day < 0:
            return 'D'+str(day)
        else:
            return '마감'
        

    def format_data(self, student_number):
        result = [["", "카테고리", "과제명", "평균 소요 시간", "걸린 시간", ""]]
        category_data = DataCategory.data
        
        if student_number in self.data:
            for d in self.data[student_number]:
                result.append([
                    self.difference_date(d['마감 날짜']),
                    d['카테고리'],
                    d['과제명'],
                    category_data[d['카테고리']].get_avg_time(),
                    d['걸린 시간'],
                    d['버튼']
                ])

        return result
    
    def add_assignment(self, number, date, category, name):
        temp = {
            '마감 날짜': date,
            '카테고리': category,
            '과제명': name,
            '걸린 시간': '',
            '버튼': '완료'
        }

        if number not in self.data:
            self.data[number] = []

        self.data[number].append(temp)
        DataCategory().add_assignment(category)

    def file(self, student_number):
        with open('assignments.txt', 'w', encoding='utf-8') as file:
            for assignment in self.data[student_number]:
                file.write(f"마감 날짜: {assignment['마감 날짜']}\n")
                file.write(f"카테고리: {assignment['카테고리']}\n")
                file.write(f"과제명: {assignment['과제명']}\n")
                file.write(f"걸린 시간: {assignment['걸린 시간']}\n")
                file.write("\n")
