from datetime import datetime
from tkinter import messagebox
from utils import *

class DataCategory:
    data = {
        '문제해결과 알고리즘 과제': {
            '완료인원': 1,
            '총인원': 2,
            '총 소요 시간': 15,
            '소요 시간': [15]
        },
        '러닝페어': {
            '완료인원': 0,
            '총인원': 1,
            '총 소요 시간': 0,
            '소요 시간': []
        }
        ,
        '문제해결과 알고리즘 퀴즈': {
            '완료인원': 0,
            '총인원': 0,
            '총 소요 시간': 0,
            '소요 시간': []
        }
    } 

    def format_data(self):
        result = [["카테고리", "완료인원 / 총인원", "평균 소요 시간"]]
        for key, value in self.data.items():
            avg = 0
            if value['완료인원'] > 0:
                avg = (value['총 소요 시간'] // value['완료인원'])

            result.append([key, str.format('{0} / {1}', value['완료인원'], value['총인원']), str.format('{0} 분', avg)])
        return result
    
    def category_list(self):
        return list(self.data.keys())
    
    def statistic_pie_data(self, category):
        return [self.data[category]['완료인원'], self.data[category]['총인원']- self.data[category]['완료인원']]
    
    def statistic_bar_data(self, category):
        return self.data[category]['소요 시간']
    
    def add_category(self, category):
        if category in self.data:
            messagebox.showwarning("알럿", "이미 있는 카테고리 입니다.")
            return

        self.data[category] = {
            '완료인원': 0,
            '총인원': 0,
            '총 소요 시간': 0,
            '소요 시간': []
        }

    def add_assignment(self, category):
        print(self.data)
        self.data[category]['총인원'] = self.data[category]['총인원'] + 1
        print(self.data)
    

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
        

    def format_data(self):
        result = [["", "카테고리", "과제명", "평균 소요 시간", "걸린 시간", ""]]
        category_data = DataCategory.data
        for d in self.data['2024311126']:

            avg_time = '0분'
            if category_data[d['카테고리']]['완료인원'] > 0:
                avg_time = str(category_data[d['카테고리']]['총 소요 시간'] // category_data[d['카테고리']]['완료인원']) + '분'

            result.append([
                self.difference_date(d['마감 날짜']),
                d['카테고리'],
                d['과제명'],
                avg_time,
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
            
            

