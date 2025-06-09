import Weekpay

class WeekpayManger:
    def __init__(self):
        self.worker_list = [
            Weekpay.Weekpay('홍길동', 20, 40000),
            Weekpay.Weekpay('박길동', 10, 60000),
            Weekpay.Weekpay('김길동', 30, 50000),
            Weekpay.Weekpay('이길동', 40, 30000),
            Weekpay.Weekpay('장길동', 20, 20000)
        ]
    
    def output(self):
        for w in self.worker_list: w.output()

    def search(self):
        name = input('찾을 이름 : ')
        result = list(filter(lambda w : w.name == name, self.worker_list))
        if not result: 
            print('찾는 이름의 사람이 없습니다.')
            return
        for w in result : w.output()

    def modify(self):
        name = input("찾을이름 : ")
        resultList = list(filter( lambda w : name in w.name, self.wList))
        if len(resultList) == 0:
            print("데이터가 없습니다")
            return 
        for i, w in enumerate(resultList):
            print(i, end ="\t")
            w.output()

        sel = int(input("수정할 대상의 번호를 아라비아 숫자로 입력하세요 : "))
        temp = resultList[sel]
        temp.name = input("이름 : ")
        temp.work_time = int(input("근무시간 ")) 
        temp.per_pay = int(input("시간당급여액 ")) 
        temp.process()

    def start(self):
        print('start')
    
if __name__ == '__main__':
    mgr = WeekpayManger()
    # mgr.output()
    # mgr.search()
    mgr.modify()
    mgr.output()