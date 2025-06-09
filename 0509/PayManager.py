import pickle

class PayManager:
    def __init__(self):
        self.payList = []

    def keyIn(self):
        try:
            arr = input('주급정보를 입력해주세요([이름 시간당급여 근로시간] 형식) : ').split()
            return Worker(arr[0], int(arr[1]), int(arr[2]))
        except:
            print('형식이 일치하지 않습니다.[입력형식 ex. 김이름 10030 15]')
            return None
    
    def add(self):
        w = self.keyIn()
        if w: self.payList.append(w)
        
    def output(self):
        for w in self.payList: w.output()

    def search(self):
        k = input('회원의 이름을 입력해주세요 : ')
        for w in self.payList:
            if w.name == k: return w
        return None
    
    def modify(self):
        target = self.search()
        if not target: return False
        w = self.keyIn()
        if w : self.payList[self.payList.index(target)] = w
        return True
        
    def delete(self, target = None):
        if not target: target = self.search()
        if not target: return False
        self.payList.remove(target)
        return True

    def sort(self):
        self.payList.sort(key = lambda x : -x.total)

    def save(self):
        with open('data/pay.txt', 'wb') as file:
            pickle.dump(self.payList, file)
    
    def load(self):
        with open('data/pay.txt', 'rb') as file:
            r = pickle.load(file)
            print('불러옴')
            self.payList.extend(r)

class Worker:
    def __init__(self, name, wage, workHour):
        self.name = name
        self.wage = wage
        self.workHour = workHour
        self.process()
    
    def process(self):
        self.plusWage = self.workHour // 40 * 8 * self.wage
        self.total = self.wage * self.workHour + self.plusWage

    def output(self):
        print(f'시간당 {self.wage}원을 받으며 {self.workHour}시간 일한 결과 주휴수당 {self.plusWage}원을 포함해 총 {self.total}원 지급 예정인 {self.name}님 고생 많으셨습니다.')

def main():
    manager = PayManager()
    print(' === ==== ==== 주급 관리 === ==== ==== ')
    funcs = [None, manager.add, manager.output, manager.search, manager.modify, manager.delete, manager.sort, manager.save, manager.load]
    while True:
        try:
            c = int(input('관리 메뉴를 숫자로 선택해주세요 1.정보입력 | 2.전체출력 | 3.검색 | 4.수정 | 5.삭제 | 6.정렬 | 7.저장 | 8.불러오기 | 0.종료 : '))
            if c == 0: return
            if 1 <= c <= 8: 
                r = funcs[c]()
                if 3 <= c <= 5:
                    if not r: print('찾는 회원이 존재하지 않습니다.')
                    if type(r) != bool: r.output()
            else: print('메뉴에 없는 입력입니다.')
        except: print('숫자로 입력해주세요')

if __name__ == '__main__':
    main()