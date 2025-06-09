'''
클래스 - 사용자가 정의하는 데이터 타입, 객체(인스턴트)를 만들기 위한 설계도
        관련있는 변수와 함수 집합, 객체 생성 시 메모리 확보

        클래스 정의 로드 시 한 번 호출되는 영역 : 클래스 영역
        변수는 생성자(객체 생성시 호출되는 함수 | 시스템이 호출 | __init__ | 첫번째 매개변수는 self[java의 this])에서

        파이썬 모듈은 내장변수를 가짐(ex. __name__)
        print(__name__) 실행
            해당 파일 안 : __main__
            import되어 실행 : 파일명 전달
'''

class Person: # 객체 생성 시 메모리 할당
    name = '홍길동' #클래스 변수
    age = 12       #클래스 변수

    def __init__(self):
        print('생성자 호출')

p1 = Person()
print(p1.name)
print(p1.age)

print(Person.name)
print(Person.age)
