#람다 : 한 줄 함수
def add(x = 0, y = 0, z = 0): return x + y + z

my_add = add #my_add라는 변수에 add함수가 들어감
print(my_add(1, 2, 3))

#함수는 일급객체

def my_func(x, y, callback): #세 번째 인자가 callback, 함수 주소를 받아옴
    result = callback(x, y)
    print(x, y, callback)

def add(x, y): return x + y

my_func(4, 5, add)
my_func(4, 5, lambda x, y : x + y) 

func_list = [lambda x, y : x + y,
             lambda x, y : x - y,
             lambda x, y : x * y,
             lambda x, y : x / y,]

for func in func_list: print(func(9, 5))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#첫번째 매개변수로 올 함수를 호출하는 호출자는 filter
#매개변수가 하나여야 하고, return값은 bool타입
def is_even(n): return n % 2 == 0
for i in filter(is_even, a): print(i, end = '\t')
for i in filter(lambda x: x % 2 == 0, a): print(i, end = '\t')
print()
person_list = [
    {'name' : '홍길동'  , 'age' : 34, 'phone' : '010-0000-0001'},
    {'name' : '강감찬'  , 'age' : 70, 'phone' : '010-0000-0001'},
    {'name' : '서희'    , 'age' : 54, 'phone' : '010-0000-0001'},
    {'name' : '윤관'    , 'age' : 39, 'phone' : '010-0000-0001'},
    {'name' : '김종서'  , 'age' : 38, 'phone' : '010-0000-0001'},
    {'name' : '이순신'  , 'age' : 44, 'phone' : '010-0000-0001'},
    {'name' : '곽재우'  , 'age' : 62, 'phone' : '010-0000-0001'},
]

#이름이 서희인 사람의 자료를 갖고 오고자 한다
key_name = '서희'
for person in filter(lambda e : e['name'] == key_name, person_list): print(f'{person["name"]} {person["age"]} {person["phone"]}')
print(*filter(lambda e : e['name'] == key_name, person_list))

#40세 이상만
print(*filter(lambda e : e['age'] >= 40, person_list), sep = '\n')

#map : 중간 연산을 수행한 후 반환한다, 나이 - 5
#첫번째 인자인 함수의 매개변수는 하나, 리턴도 하나
for i in map(lambda x : x * 10, a): print(i, end = '\t')
print(a)

def my_func2(x):
    x['age'] += 5
    return x
for per in map(my_func2, person_list): print(per)

print(*map(lambda x : (x, x['age'] + 5), filter(lambda e : e['age'] >= 40, person_list)), sep = '\n')

#데이터 정렬 list 객체는 sort(원본 정렬), sorted(정렬 후 반환) 메서드가 있는데
#key 매개변수로 함수를 넘겨 정렬 조건을 줄 수 있다.
#key 함수에서 비교 연산이 가능해야 하고 오름차순이 기본 (reversed = False)
a = [9, 4, 5, 6, 7, 8, 1, 2, 10, 3]
a.sort()
print(a)
print(*sorted(person_list, key = lambda x : x['name']), sep = '\n')
print(*sorted(person_list, key = lambda x : x['name'], reverse = True), sep = '\n')

a = [9, 4, 5, 6, 7, 8, 1, 2, 10, 3]
b = sorted(a)
print(f'a = {a}\tb = {b}')

list2 = sorted(person_list, key = lambda per:per['name'], reverse = True)
print(*list2, sep = '\n')