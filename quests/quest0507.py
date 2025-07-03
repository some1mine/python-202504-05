import random

class User:
    cases = ['가위', '바위', '보']
    
    def __init__(self):
        self.win_draw_lose = [0, 0, 0]
    
    def pick(self):
        while True:
            try: 
                choice = int(input('1(가위), 2(바위), 3(보), 4(종료) 중 하나를 숫자로 골라주세요 : '))
                if choice not in (1, 2, 3, 4): raise
                self.choice = choice
                return choice != 4
            except: 
                print('올바르지 않은 입력입니다.')

    def fight(self, choice):
        if self.choice == choice : 
            self.win_draw_lose[1] += 1
            print(f'{self.cases[self.choice - 1]}를 선택한 결과 비겼습니다.')
        elif self.choice % 3 + 1 == choice : 
            self.win_draw_lose[2] += 1
            print(f'{self.cases[self.choice - 1]}를 선택한 결과 졌습니다.')
        else : 
            self.win_draw_lose[0] += 1
            print(f'{self.cases[self.choice - 1]}를 선택한 결과 이겼습니다.')
    
    def show_statistics(self):
        print(f'승 : {self.win_draw_lose[0]} | 패 : {self.win_draw_lose[2]} | 무 : {self.win_draw_lose[1]}')


def game(u : User) :
    if not u.pick() : return
    u.fight(random.randint(1, 3))

def main():
    print('======= 가위바위보 =======')    
    u = User()
    while True:
        a = input('0 포기 | 1 게임 | 2 통계 : ')
        if a == '0': break
        elif a == '1': game(u)
        elif a == '2': u.show_statistics()
        else : print('올바르지 않은 입력입니다.')
    u.show_statistics()

if __name__ == '__main__':
    main()