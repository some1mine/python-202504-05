'''
1세대 - 기계어와 어셈블리어
2세대 - 고급언어, 코볼(데이터 처리 전용), 포트란(과학기술용), 범용 언어 | goto, 의식의 흐름 코딩 
3세대 - C, algol, pascal, etc ...
    스파게티 코드에 대한 반성 -> 구조적 프로그래밍
    1. top - down 설계
    2. 설계 개념 시도
    3. 순서도
    4. 모듈화(함수와 프로시저로 프로그램을 작은 단위로 나누어 프로그래밍)
    5. 주석을 열심히
    6. 소프트웨어 공학
4세대 - 객체지향 프로그래밍
    1. bottom-up, 부품 요소들을 모아 제품을 완성
    2. 객체지향
        1) 추상화   : 내부 구조를 몰라도 사용에 지장은 없음, 사용자 편의성
        2) 캡슐화   : 접근 권한별 외부 노출 제한
        3) 상속     : 만들어진 클래스들을 상속받아 사용해 사용함, 코드의 재활용도를 높인다
        4) 다형성   : 이름은 같은데 형태가 여러개, python에 overwriting은 있지만, overloading은 지원하지 않는다.


def 함수이름():
    ....
    ....

함수 이름 규칙은 변수 규칙과 동일하다
    1. 영문자 시작(_가능 : private, protected methods)
    2. 대소문자 구분
    3. 예약어 안됨
작명 규칙
    1. 소문자 시작
    2. camel | snake case

'''

global_x = 10 # 함수 외부에 변수를 선언
def my_func1(): # 함수 내부에서 값 할당 시 새로운 변수가 만들어져 할당, 외부 scope와 변수의 값을 공유하려면 global 키워드 붙여야 함
    global_x = 30
    y = 20
    print(global_x, y)

global_x = 100
my_func1()
print(global_x)

# 함수의 매개변수 기본값
# dict타입 매개변수
def my_func2(name = '홍길동', age = 11, phone = '010-0000-0001'):
    print(name, end = '\t')
    print(age, end = '\t')
    print(phone)

my_func2()
my_func2("임꺽정")
my_func2("임꺽정", 33)
my_func2(name = '둘리')
my_func2(age = 33)
my_func2(phone = '018-333-3333')
# 함수가 실행 시점에 결정됨 -> 동적 할당 | 컴파일 시점에 결정 -> 정적 할당
# 컴파일 언어 : 전처리 -> 컴파일링 -> 어셈블링 -> 링킹
# 자바는 컴파일 언어라도 동적 할당, 파이썬은 전부 동적 할당

# generator - ex) range, filter
# return : 값 반환하며 함수 종료 | yield 대기 상태로 함수 반환
# 값을 얻고자 할 때 next나 for문으로
def my_range(start = 1, end = 5):
    i = start
    while i <= end:
        yield i
        i = i + 1

gen = my_range()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in my_range(1, 10): print(i, end = '\t')
print()

'''
1. 데이터가 너무 커서 나누어 처리해야 할 때
2. 상시 작업 필요시
3. 파일을 지속적으로 읽어서 퍼리하고자 할 때
'''

'''
문제1.

입력 화면 면적을 구할 도형의 길이(?) 1.원의 반지름 | 2.사각형 가로 세로 | 3.사다리꼴 윗변 아랫변 높이 | 0.종료
'''

from math import pi

def circle():
    r = int(input('원의 반지름을 입력해주세요 : '))
    return r * r * pi

def oblong():
    width = int(input('직사각형의 가로 길이를 입력해주세요 : '))
    height = int(input('직사각형의 가로 길이를 입력해주세요 : '))
    return width * height

def trapezoid():
    upper = int(input('사다리꼴의 윗변 길이를 입력해주세요 : '))
    lower = int(input('사다리꼴의 아랫변 길이를 입력해주세요 : '))
    height = int(input('사다리꼴의 높이를 입력해주세요 : '))
    return (upper + lower) * height / 2

get_areas = {'1' : circle, '2' : oblong, '3' : trapezoid}

def game():
    while True:
        print('도형의 길이를 입력받아 면적을 구하기')
        choice = input('0~3중 하나의 메뉴를 골라주세요 1.원 | 2.직사각형 | 3.사다리꼴 | 0.종료 : ')
        if choice == '0': return
        elif choice in get_areas.keys(): print(f'면적은 {get_areas[choice]()}입니다')
        else: print('잘못 입력하셨습니다')

game()

'''
문제2. 리스트에서 중복을 제거하고 반환
'''

def remain_only_one(lst):
    return list(set(lst))

'''
문제3. my_int 정수 전환 함수, 잘못된 데이터 -> -1
'''

def my_int(n):
    # try: return int(n)
    # except: return -1
    s = 0
    for c in n:
        if ord(c) < ord('0') or ord(c) > ord('9'): return -1
        s *= 10; s += ord(c) - ord('0')
    return s

print(remain_only_one([1,2,3,3,2]))
print(my_int(input('숫자를 입력해주세요')))

'''
문제4. 문자열 뒤집는 함수
'''

def reverse(s):
    res = ''
    for i in range(len(s) - 1, -1, -1): res += s[i]
    return res
