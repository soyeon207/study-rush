from datetime import datetime
from tkinter import messagebox

class DataCategory:
    data = {
        '문제해결과 알고리즘 과제': {
            '완료인원': 1,
            '총인원': 3,
            '총 소요 시간': 60,
            '소요 시간': [60]
        },
        '러닝페어': {
            '완료인원': 2,
            '총인원': 5,
            '총 소요 시간': 100,
            '소요 시간': [40, 60]
        }
        ,
        '문제해결과 알고리즘 퀴즈': {
            '완료인원': 3,
            '총인원': 6,
            '총 소요 시간': 15,
            '소요 시간': [1, 7, 7]
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
        f = '%Y-%m-%d'
        converted_date = datetime.strptime(target, f)
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
            result.append([
                self.difference_date(d['마감 날짜']),
                d['카테고리'],
                d['과제명'],
                str(category_data[d['카테고리']]['총 소요 시간'] // category_data[d['카테고리']]['완료인원']) + '분', 
                d['걸린 시간'],
                d['버튼']
            ])

        return result

print(list(DataCategory().category_list()))