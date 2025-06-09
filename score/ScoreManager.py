from ScoreData import ScoreData
import sys; import os; import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ScoreManager:
    def __init__(self):
        self.scoreList = [
            ScoreData(),
            ScoreData('조승연', 90, 80, 90),
            ScoreData('안세영', 80, 80, 70),
            ScoreData('김연경', 90, 90, 90),
            ScoreData('김연아', 100, 80, 100),
        ]

    def display_menu(self):
        print("--------")
        print("  메뉴   ")
        print("--------")
        print("1. 추가  ")
        print("2. 출력  ")
        print("3. 검색  ") #이름
        print("4. 수정  ") #이름
        print("5. 삭제  ") #이름
        print("6. 정렬  ") #총점 내림차순으로 
        print('7. 저장  ')
        print('8. 불러오기')
        print("0. 종료  ")
        print("--------")

    def append(self):           # 1. 추가
        s = ScoreData()
        s.name = input('이름 : ')
        s.kor = int(input('국어 : '))
        s.eng = int(input('영어 : '))
        s.math = int(input('수학 : '))
        s.process()
        self.scoreList.append(s)

    def printAll(self):        # 2. 출력
        for s in self.scoreList: s.print()


    def search(self):           # 3. 검색
        name = input('대상의 이름을 입력해주세요 : ')
        try: 
            s = next(filter(lambda x: x.name == name, self.scoreList))
            s.print()
            return s
        except: 
            print('찾으시는 데이터가 없습니다.')
            return None
    
    def modify(self):           # 4. 수정
        self.delete()
        self.append()

    def delete(self):           # 5. 삭제
        found = self.search()
        if found is not None: self.scoreList.remove(found)

    def sort(self):             # 6. 정렬
        self.scoreList.sort(key = lambda x: -x.total)

    def save(self):             # 7. 저장
        with open('data/score.bin', 'wb') as file:
            pickle.dump(self.scoreList, file)

    def load(self):             # 8. 불러오기
        with open('data/score.bin', 'rb') as file:
            data = pickle.load(file)
            for r in data: r.print()
            return r

    def start(self):
        funcList = [None, self.append, self.printAll, 
                     self.search, self.modify, self.delete, 
                     self.sort, self.save, self.load]
        while True:
            self.display_menu()
            choice = int(input('선택 : '))
            if choice > 0 and choice < len(funcList): funcList[choice]()
            elif choice == 0: return
            else: print('잘못된 메뉴입니다.')

if __name__ == '__main__':
    sm = ScoreManager()
    sm.printAll()
    sm.start()
        