import random
# 이름 국어 영어 수학 총점 평균     평균으로 수(90) 우(80) 미(70) 양(60) 가(60 미만)

# dictionary 형식 == json 형식(mongoDB) | pandas dataframe 형식으로 변환이 쉬움
# 전역변수는 함수 안에서 사용 가능하고
# 함수 내의 변수는 global 키워드를(nonlocal도 있음) 사용해 전역 스코프에서 사용할 수 있다.
# 변수 스코프 : 지역변수 -> 전역변수 -> 빌트인 변수
'''
클린 코드
    1. 함수 등 모듈은 하나의 기능에 집중해라(입력과 작업, 그리고 출력 정의)
    2. error handling을 별로로 나누어라(데이터 흐름 초기에 처리하기)
    3. early return 
'''
scores = []

'''
    === 0 초기화 및 사용자 프로세스 제어 ===
'''

#초기값 세팅
def init():
    names = ['홍길동', '홍경래', '강길산', '강감찬', '서희', '윤관', '감강찬', '김연아', '안세영', '조승연']
    for name in names: scores.append({'name' : name, 'kor' : random.randint(0, 100), 'eng' : random.randint(0, 100), 'math' : random.randint(0, 100)})
    for s in scores: cal_static(s)

#시작 함수
def main():
    init()
    n = int(input('성적을 입력할 총 학생수를 입력해주세요 : '))
    for _ in range(n): user_input()
    start()

#사용자 선택 표시
def select_menu():
    return input('1.추가\n2.출력\n3.검색\n4.수정\n5.삭제\n0.종료\n선택 : ')
    # print('2.출력')
    # print('3.검색')
    # print('4.수정')
    # print('5.삭제')
    # print('0.종료')

#사용자 상호작용 시작 함수
def start():
    sel = '1'
    while sel != '0':
        sel = select_menu()
        # if sel >= 3: menus[sel](input('학생의 이름을 입력해주세요 : '))
        # elif sel < 3: menus[sel]()
        if sel == '0': print('프로그램을 종료합니다.')
        elif sel == '1': user_input()
        elif sel == '2': print_all()
        elif sel == '3': print_out(search(input('학생의 이름을 입력해주세요 : ')))
        elif sel == '4': modify(input('학생의 이름을 입력해주세요 : '))
        elif sel == '5': remove(input('학생의 이름을 입력해주세요 : '))
        else: print('잘못 선택하셨습니다.')

'''
    === 1 입력과 입력값 검사 ===
'''

#성적 입력 받는 함수
def user_input():
    while True:
        typed_in = input('학생의 이름과 국어, 영어, 수학 점수를 입력해주세요(ex 홍길동 100 40 80) : ').split() #사용자 입력을 받아서
        if is_score(typed_in[1]) and is_score(typed_in[2]) and is_score(typed_in[3]): break
        else: print('입력 형식을 정확하게 맞춰 주세요(이름 국어점수 영어점수 수학점수, 100점 만점)')
    student = {'name' : typed_in[0], 'kor' : int(typed_in[1]), 'eng' : int(typed_in[2]), 'math' : int(typed_in[3])} #키-값 쌍의 dict 형식으로 변환한 다음
    scores.append(student) #배열에 추가
    cal_static(student) #총점, 평균, 등급 계산

#성적의 범위와 형식이 맞는지 검사
def is_score(n, limit = 100):
    for i in n:
        if ord(i) < ord('0') or ord(i) > ord('9'): return False
    return int(n) <= limit

#통계 정보를 계산해 학생 정보에 추가하는 함수
def cal_static(score):
    score['total'] = score['kor'] + score['eng'] + score['math']
    score['avg'] = score['total'] / 3
    cal_grade(score) #계산 케이스가 많아 위에 별도 함수에서 계산

#등급을 계산하는 함수
def cal_grade(score):
    # if score['avg'] >= 90 : score['grade'] = '수'  
    # elif score['avg'] >= 80 : score['grade'] = '우'  
    # elif score['avg'] >= 70 : score['grade'] = '미'  
    # elif score['avg'] >= 60 : score['grade'] = '양'
    # else: score['grade'] = '가'  
    score['grade'] = '수' if score['avg'] >= 90 else '우' if score['avg'] >= 80 else '미' if score['avg'] >= 70 else '양' if score['avg'] >= 60 else '가'


'''
    === 2 출력 ===
'''

#전체를 출력하는 함수
def print_all():
    for score in scores: 
        print_out(score)

#하나의 데이터를 출력하는 함수
def print_out(score):
    print(score)

'''
    === 3 검색 ===
'''

#이름으로 학생 검색 함수
def search(name):
    result = next(filter(lambda x : x['name'] == name, scores))
    return result if result else False

'''
    === 4 수정 ===
'''

def modify(name):
    if remove(name): user_input()

'''
    === 5 삭제 ===
'''

def remove(name):
    target = search(name)
    if target: 
        scores.remove(target)
        return True
    else: print(f'{name}은 없는 이름입니다.')
    return False

# menus = [print('프로그램을 종료합니다'), user_input, print_all, print_out, modify, remove]
main()