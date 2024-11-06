class CategoryInfo:
    LIST_COLUMNS = [["카테고리", "완료인원 / 총인원", "평균 소요 시간"]]

    category = None
    complete_count = 0              # 완료인원
    total_count = 0                 # 총인원
    total_time_required = 0         # 총 소요 시간
    time_required = []              # 소요 시간

    def __init__(self, category):
        self.category = category

    def __init__(self, category, complete_count, total_count, total_time_required, time_required):
        self.category = category
        self.complete_count = complete_count
        self.total_count = total_count
        self.total_time_required = total_time_required
        self.time_required = time_required

    def complete(self, time_required):
        self.complete_count += 1
        self.total_time_required += time_required
        self.time_required.append(time_required)

    def add_total_count(self):
        self.total_count += 1

    def format_list(self):
        avg = 0
        if self.complete_count > 0:
            avg = (self.total_time_required // self.complete_count)
        return [self.category, str.format('{0} / {1}', self.complete_count, self.total_count), str.format('{0} 분', avg)]

    def get_avg_time(self):
        if self.complete_count < 1:
            return '0분'
        return str(self.total_time_required // self.complete_count) + '분'

    def format_pie(self):
        return [self.complete_count, self.total_count - self.complete_count]
    
    def format_bar(self):
        return self.time_required
    
    def format_file(self, file):
        file.write(f"카테고리: {self.category}\n")
        file.write(f"완료인원: {self.complete_count}\n")
        file.write(f"총인원: {self.total_count}\n")
        file.write(f"총 소요 시간: {self.total_time_required}\n")
        file.write(f"소요 시간: {self.time_required}\n")
        file.write("\n")

    def print(self):
        print('완료인원 : ', self.complete_count)
        print('총인원 : ', self.total_count)
        print('총 소요 시간 : ', self.total_time_required)
        print('소요 시간 : ', self.time_required)

    

        
        


