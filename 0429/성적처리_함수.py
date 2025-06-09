# 이름 국어 영어 수학 총점 평균     평균으로 수(90) 우(80) 미(70) 양(60) 가(60 미만)

# dictionary 형식 == json 형식(mongoDB) | pandas dataframe 형식으로 변환이 쉬움
# 전역변수는 함수 안에서 사용 가능하고
# 함수 내의 변수는 global 키워드를(nonlocal도 있음) 사용해 전역 스코프에서 사용할 수 있다.

'''
클린 코드
    1. 함수 등 모듈은 하나의 기능에 집중해라(입력과 작업, 그리고 출력 정의)
    2. error handling을 별로로 나누어라(데이터 흐름 초기에 처리하기)
    3. early return 
'''
scores = []

def is_score(n, limit = 100):
    for i in n:
        if ord(i) < ord('0') or ord(i) > ord('9'): return False
    return int(n) <= limit

def user_input():
    while True:
        typed_in = input('학생의 이름과 국어, 영어, 수학 점수를 입력해주세요(ex 홍길동 100 40 80) : ').split() #사용자 입력을 받아서
        if is_score(typed_in[1]) and is_score(typed_in[2]) and is_score(typed_in[3]): 
            break
        else: 
            print('입력 형식을 정확하게 맞춰 주세요(이름 국어점수 영어점수 수학점수, 100점 만점)')
    student = {'name' : typed_in[0], 'kor' : int(typed_in[1]), 'eng' : int(typed_in[2]), 'math' : int(typed_in[3])} #키-값 쌍의 dict 형식으로 변환한 다음
    scores.append(student) #배열에 추가
    cal_static(student) #총점, 평균, 등급 계산

def cal_grade(score):
    if score['avg'] >= 90 : 
        score['grade'] = '수'  
    elif score['avg'] >= 80 : 
        score['grade'] = '우'  
    elif score['avg'] >= 70 : 
        score['grade'] = '미'  
    elif score['avg'] >= 60 : 
        score['grade'] = '양'
    else: score['grade'] = '가'  
    # score['grade'] = '수' if score['avg'] >= 90 else '우' if score['avg'] >= 80 else '미' if score['avg'] >= 70 else '양' if score['avg'] >= 60 else '가'

def cal_static(score):
    score['total'] = score['kor'] + score['eng'] + score['math']
    score['avg'] = score['total'] / 3
    cal_grade(score) #계산 케이스가 많아 위에 별도 함수에서 계산

def print_out(score):
    print(score)

def main():
    n = int(input('성적을 입력할 총 학생수를 입력해주세요 : '))
    for _ in range(n): 
        user_input()
    for s in scores: 
        print_out(s)

main()

def start():
    while True:
        print('1.추가')
        print('2.출력')
        print('0.종료')
        sel = input('선택 : ')
        if sel == '1': user_input()
        elif sel == '2': 
            for s in scores: print_out(s)
        elif sel == '0':
            print('프로그램을 종료합니다.')
            return
        else:
            print('잘못 선택하셨습니다.')

start()