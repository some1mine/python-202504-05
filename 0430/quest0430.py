import random

score = [0, 0, 0]
cases = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
choices = ['가위', '바위', '보']
results = ['비겼습니다', '이겼습니다', '졌습니다']

def continue_or_quit():
    return input('0 종료, 다른 값 계속 : ')

def choice_rock_paper_shears():
    return input('1(가위), 2(바위), 3(보) 중 하나를 숫자로 골라주세요 : ')

def display_result(choice, r):
    print(f'{choices[choice]}를 낸 결과 {results[r]}')

def main():
    while True:
        if continue_or_quit() == '0': break
        user_choice = choice_rock_paper_shears()
        if user_choice in ('1', '2', '3'):
            result = cases[int(user_choice) - 1][random.randint(0, 2)]    
            display_result(int(user_choice) - 1, result)
            score[result] += 1
        else: print('잘못된 입력입니다.[가위바위보 선택 : 1(가위), 2(바위), 3(보)]')
    if sum(score): print(f'{sum(score)}번의 승부 중 {score[1]}번 승리한 승률 {score[1] / sum(score)}의 좋은 게임이었습니다.')

main()
        