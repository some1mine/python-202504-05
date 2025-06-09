#함수란 ? 기능별 코드 묶음
#스파게티 코드 문제(결과만 나오면 좋다) 해결을 위해
#모듈 => 기능별로 나누어(반환값이 없는 프로시저 + 반환값이 있는 함수) => c언어에서 void 도입(합침)
#파이썬의 함수정 키워드 : def
'''
#유지보수의 간편성과 용이성
#반복 작업의 간편화와 공통화, 간결화
#구조적(절차형?) 프로그래밍(c언어), 객체지향 프로그래밍에 필수
#15줄 이하의 단위의 함수들로 나뉘도록 모듈화

def 함수이름(매개변수들):
    ....
    ....
    return 리턴 값은 하나, 파이썬은 return이 여러 개일 때 tuple로 자동으로 묶어 반환한다.
'''

def print_line(): # 함수를 정의한다.
    pass #파이썬은 콜론(:)다음 들여쓰기 블럭을 비워둘 수 없으므로 pass 키워드를 남겨야 한다.
    print('=', 30)

print_line()
print_line()
print_line()
print_line()
print_line()
print_line()
print_line()
print_line()
print(print_line())

#1부터 n까지의 합계를 구하는 함수 만들기
def sigma(limit) : #작은 프로그램 단위 입출력
    #limit : 매개변수, 함수 외부에서 내부로의 변수 또는 값 전달을 위한 목적
    s = 0
    for i in range(1, limit  +1): s += i
    return s
print(sigma(100))