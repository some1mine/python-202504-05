import random
titles = ['가위', '바위', '보']
titles2 = ['컴퓨터 승', '사람 승', '무승부']
game_list = []

def is_winner(computer, person):
    # 마지막 \기호는 여러 줄에 걸친 문장을 같은 라인으로 인식하게 한다
    if computer == person : return \
        3
    if person % 3 + 1 == computer: return 0
    return 1

def test():
    for i in range(10):
        computer = random.randint(1, 3)
        person = random.randint(1, 3)
        winner = is_winner(computer, person)
        print(f'컴퓨터 : {titles[computer]} | 사람 : {titles[person]} | 승자 : {titles2[winner]}')

def game_start():
    game_list.clear()
    while True:
        computer = random.randint(1, 3)
        person = int(input('1. 가위 2. 바위 3. 보 : '))
        winner = is_winner(computer, person)
        print(f'컴퓨터 : {titles[computer - 1]} | 사람 : {titles[person - 1]} | 승자 : {titles2[winner - 1]}')
        game_list.append({'computer' : computer, 'person' : person, 
                          'winner' : winner})
        again = input('게임을 계속하시곘습니까?y/n')
        if again != 'Y' or again != 'y': return

def game_statistic():
    computer_win = 0
    person_win = 0
    equal_count = 0
    for game in game_list:
        if game['winner'] == '1':
            computer_win += 1
        elif game['winner'] == '2':
            person_win += 1
        else:
            equal_count += 1
    for game in game_list:
        print(f'컴퓨터 : {game["computer"]}', end = '\t')
        print(f'사람 : {game["person"]}', end = '\t')
        print(f'승패 : {game["winner"]}')
    
    print('컴퓨터 승 ', computer_win)
    print('사람 승 ', person_win)
    print('무승부 ', equal_count)

# game_start()
def game_main():
    while True:
        print('1. 게임 시작')
        print('2. 게임 통계')
        print('3. 게임 종료')
        sel = input('선택 : ')
        if sel == '1': game_start()
        elif sel == '3': 
            print('게임을 종료합니다')
            return 
        
game_main()
