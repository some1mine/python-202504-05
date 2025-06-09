from GameData import Baseball

class GameMain:
    def __init__(self):
        self.gameList = []
    
    def start(self):
        while True:
            print('1. 게임시작')
            print('2. 통계보기')
            print('0. 종료')
            sel = input('선택 : ')
            if sel == '0': return
            if sel == '1': self.gameStart()
            if sel == '2': self.showStatistics()

    def gameStart(self):
        b = Baseball()
        b.start()
        self.gameList.append(b)

    def showStatistics(self):
        print(f'{sum([t.resultList[1] for t in self.gameList]) / len(self.gameList) if self.gameList else 0}번의 평균 시도 \
               성공 횟수 {len([t.resultList[0] for t in self.gameList if t.resultList[0]])}')

if __name__ == '__main__':
    g = GameMain()
    g.start()