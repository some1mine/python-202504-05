# 숫자 야구 게임
import random

targets = [0, 0, 0]
LOWER_BOUND = 1
UPPER_BOUND = 9
MIN_TRIAL = 0
MAX_TRIAL = 6

statisctics = {
    'game_count' : 0,
    'trials' : [],
    'trials_avg' : 0,
    'win' : 0,
    'lose' : 0,
    'quit' : 0,
    'win_rate' : 0,
}

'''
1. 숫자 맞추기 한 라운드에 대한 함수들
'''

def one_round():# 숫자 맞추기 한 라운드
    inputs = guess_nums()
    if not inputs:
        return None
    counts = pitch(inputs)
    print(f'{counts[0]}스트라이크, {counts[1]}볼, {counts[2]}아웃')
    return counts[0] == 3

def pitch(inputs):# 사용자 입력과 컴퓨터가 생성한 주어진 세 개의 값들로 계산해 반환하는 함수
    counts = [0, 0, 0]
    for i in range(3):
        if inputs[i] == targets[i]:
            counts[0] += 1
        elif inputs[i] in targets:
            counts[1] += 1
        else:
            counts[2] += 1
    return counts

def guess_nums():# 사용자에게 세 숫자를 입력 받는 함수
    while True:
        try:
            inputs = input('1~9까지의 숫자 중 하나씩 골라 세 자리를 완성해 주세요(ex 1 1 1, 이번 게임을 그만하시려면 -1을 입력해주세요) : ')
            if inputs == '-1':
                return None
            inputs = list(map(int, inputs.split()))
            if len(inputs) != 3:
                raise
            return inputs
        except:
            print('아라비아 숫자 세개를 띄어쓰기로 구분해 입력해주세요')

'''
2. 6회의 시도로 이루어지는 한 이닝(?)에 대한 함수들
'''

def set_targets():# 컴퓨터의 세 숫자를 세팅하는 함수
    for i in range(3):
        targets[i] = random.randint(LOWER_BOUND, UPPER_BOUND)

def play_inning():# 시도와 포기를 포함해 한 이닝을 플레이하는 함수
    for i in range(MAX_TRIAL):
        print(f'총 6번의 시도 중 {i + 1} 번째 시도')
        result = one_round()
        if result is None:
            return i, False, True
        if result:
            return i + 1, True, False
    return MAX_TRIAL, False, False

def show_results(trial, success):# 이닝의 결과를 보여주는 함수
    if success:
        print(f'{trial}번의 시도 끝에 성공했습니다.')
    else:
        print(f'{trial}번의 시도, 주어진 숫자는 {targets}였습니다.')

def inning():# 6번의 기회가 주어지는 한 게임
    set_targets()
    trial, success, quit = play_inning()
    show_results(trial, success)
    save_statistics(trial, success, quit)

'''
3. 전체 게임 진행과 승률 통계에 대한 함수들
'''

def save_statistics(trial, success, quit):# 통계 정보 저장
    if success: statisctics['win'] += 1
    elif quit: statisctics['quit'] += 1
    else: statisctics['lose'] += 1
    statisctics['game_count'] += 1
    statisctics['trials'].append(trial)
    statisctics['trials_avg'] = sum(statisctics['trials']) / statisctics['game_count']
    statisctics['win_rate'] = statisctics['win'] / statisctics['game_count'] * 100

def show_statistics():# 통계 정보 출력
    print(f'총 {statisctics["game_count"]}번의 게임')
    print(f'성공 {statisctics["win"]}')
    print(f'포기 {statisctics["quit"]}')
    print(f'실패 {statisctics["lose"]}')
    print(f'평균 시도 횟수는 {statisctics["trials_avg"]:.2f}')
    print(f'승률{statisctics["win_rate"]:.2f}%입니다.')

def choice_menu():# 게임 진행 여부 등 메뉴 선택
    print('메뉴를 선택해주세요')
    print('0. 그만하고 통계 보기')
    print('1.통계 보고 한 게임 더 진행하기')
    print('2.통계 정보 초기화 후 한 게임 더 진행하기')
    print('다른 값. 그냥 한 게임 더 진행하기')
    return input('입력 : ')

def clear_statistics():
    global statisctics
    statisctics = {
        'game_count' : 0,
        'trials' : [],
        'trials_avg' : 0,
        'win' : 0,
        'lose' : 0,
        'quit' : 0,
        'win_rate' : 0,
    }

def main():
    print('============= 숫자 야구 게임을 시작합니다 =============')
    while True:
        inning()
        choice = choice_menu()
        if choice == '0':
            break
        if choice == '1':
            show_statistics()
        if choice == '2':
            clear_statistics()
        print()
    show_statistics()
    
main()