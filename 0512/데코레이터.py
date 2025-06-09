# @
# 함수의 호출 전후에 실행할 동작을 정의
# 데코레이터 안에서 받아온 함수 호출하며, 중첩 함수를 반환

def decorator1( func ): #매개변수는 중첩함수 안에서 호출될 함수
    def wrapper(): 
        print('함수호출전')
        func()
        print('함수호출후')
    return wrapper #중첨함수의 참조를 반환

@decorator1
def hello():
    print('hello')

hello()

import time
def timeDecorator( callback ):
    def innerFunc():
        start = time.time()
        callback()
        end = time.time()
        print(f'{callback.__name__} 실행시간 {end - start}')   
    return innerFunc

@timeDecorator
def sigma():
    print('test')

sigma()

def myDecorator( callback ):
    def wrapper(*args, **kwargs):
        result = callback(*args, **kwargs)
        return result
    return wrapper

@myDecorator
def add(x, y): return x + y

print(add(1, 2))

# 로그 남기는 데코레이터
# myLog

def myLog( callback ):
    def wrapper(*args, **kwangs):
        result = callback(*args, **kwangs)
        print(f'[LOG] 함수이름 {callback.__name__}')
        print(f'[LOG] 입력값 {*args, kwangs}')
        print(f'[LOG] 출력값 {result}')
        return result
    return wrapper

@myLog
def sigma2(a): return a ** 2

sigma2(10)