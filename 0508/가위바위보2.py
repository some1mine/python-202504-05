import random

'''
    객체지향 
    
    클래스(사용자가 만드는 데이터 타입)
    파이썬의 기본 타입들과 다른 점 : 할당시 변수 = 클래스명()
    클래스로 만든 객체는 heap 공간에 저장된다는 말씀(주소 변수에 할당) - 메모리 부족시 None
    객체의 멤버에 접근하려면 .(dot) 사용
    생성자 __init__의 첫번째 인자는 객체 자신을 나타냄(self - 매개변수 이름은 변경 가능)

    추상화 - 클래스 : 내부 구조를 몰라도 쓰는데 지장이 없다
            추상화 <-> 구체화
            추상화가 잘 이루어진 확장성 있는 코드를 작성하기란 어려운 일이어서 잘하는 사람을 고생시키자(?)는 말씀
            디자인 패턴 32가지 이상

    캡슐화 - 파이썬은 기본 public(__함수__ : private, _함수_ : protected)
    상속
    다형성 - 
'''

class GameData:
    def __init__(self):
        self.winner = 0

    def game_start(self):
        self.computer = random.randint(1, 3)
        self.person = int(input('사용자 입력 : '))
        self.winner = self.is_winner()
    
    def is_winner(self):
        if self.computer == self.person: return 3
        elif self.person % 3 + 1 == self.computer: return 2
        return 1

    def print_log(self):
        print(f'컴퓨터:{self.computer} 사람:{self.person} 승부:{self.winner}')

class Game:
    titles1 = ['', '가위', '바위', '보']
    titles2 = ['', '컴퓨터승', '사람승', '무승부']

    def __init__(self):
        self.game_list = []

    def print_log(self, g : GameData):
        print(f'{self.titles1[g.computer]}', end = '\t')
        print(f'{self.titles1[g.person]}', end = '\t')
        print(f'{self.titles1[g.winner]}')

    def start(self):
        while True:
            g = GameData()
            g.game_start()
            g.print_log()
            self.game_list.append(g)

            again = input('1 계속 | 2 종료')
            if again != '1': return

    def print_result(self):
        print(f'{len(self.game_list)}번 게임 진행')
        for g in self.game_list:
            self.print_log(g)
    
    def main_start(self):
        self.start()
        self.print_log()

if __name__ == '__main__':
    # g = GameData()
    # g.game_start()
    # g.print_log()
    game = Game()
    game.start()