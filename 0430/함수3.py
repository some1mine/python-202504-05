# 가변 매개변수 -> 함수의 매개변수 개수가 바뀌는 경우
# 가변 매개변수 다음에 또다른 매개변수가 올 수 없다
# 일반인자, 가변 매개변수(*), 키-값 매개변수(**) 순서가 지켜져야 함
def my_add(*args):
    print(type(args))
    for a in args: print(a)

my_add(2, 3)
my_add(1, 2, 3)

def my_add2(*data):
    return sum(data)

print(my_add2(1, 3))
print(my_add2(1, 3, 5))
print(my_add2(1, 3, 5, 7))

def my_add3(n, *data):
    print('n', n)
    for i in data: print(i)

my_add3(1, 2, 3, 4, 5)

# dict 타입으로 받는 매개변수 **
# 매개변수 전달 방식이 달라짐

def my_func(n1, n2, **d): 
    print(f'first {n1}\tsecond {n2}')
    print(d)
my_func(1, 2, a = 'a', b = 'b', c = 'c')

def my_func2(name = '홍길도', age = 23):
    pass

def profile(role, *skills, **details):
    print('Role', role)
    print('skills', skills)
    print('details', details)

profile('programmer', 'python', 'react', 'deeplearning', salary = 100_000_000, position = '개발자')