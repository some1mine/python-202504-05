def to_double(x): #x라는 매개변수를 이용해 a값을 전달함
    x = x * 2

a = 10              #a라는 변수와 함수의 매개변수인 x는 서로 다른 공간이다.
to_double(a)        #지역 매개변수에 값을 복사하고 복사한 x의 값은 수정됨
print(a)            

def to_double2(my_dic):
    my_dic['x'] *= 2
    my_dic['y'] *= 2

my_dic = {'x' : 1, 'y' : 2}
to_double2(my_dic)
print(my_dic)

#변경 가능한 참조 인자는 매개 변수로 전달 되더라도 전역 객체 값 수정이 되지만,
#변경 불가능한 객체는 주소값이 아니라 해당 객체 자체를 복사해 전달한다

def my_add(x = 3, y = 5, z = 8): return x + y + z
result = my_add(1,2,3)
print(result)
result = my_add()
print(result)
print(my_add())
print(my_add(1))
print(my_add(1, 2))
print(my_add(1, 2, 3))

#기본값이 있는 매개변수 다음에 기본값이 없는 매개변수가 올 수 없다 ex. def func(a = 1, b = 3, c) => x
def my_func(a, b, c = 0, d = 0, e = 0):
    print(f'a={a} b={b} c={c} d={d} e={e}')
    return a + b + c + d + e
print(my_func(1, 2))

def sigma(limit = 10):
    return sum(range(1, limit + 1))

print(sigma())
print(sigma(5))
print(sigma(100))