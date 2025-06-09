a = [1,2,3,4]
b = [5,6,7,8]

c = a + b
print(c)

a.extend(b)
print(a)

s = 'hello'
if s == 'hello': #if s.equals('hello') -- java
    print('같다')
else: print('다르다')

del c[0]
print(c)

del c[4:]
print(c)

a = [4,3,5,7,9,11,17,12,15,8]
a.sort()
print(a)
a.reverse()
print(a)

a.insert(0, 100)
print(a)
a.insert(5, 77)
print(a)
a.insert(len(a), 88)
print(a)

a.remove(77)
print(a)

'''
pop함수 필요

stack - Last in First Out   |   Queue - First In First Out
'''
a = []
a.insert(0, 'A')
a.insert(0, 'B')
a.insert(0, 'C')
a.insert(0, 'D')
a.insert(0, 'E')

print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)
print(a.pop())
print(a)

#tuple : immutable, 빠른 접근
a = (1,2,3,4,5)
print(a, type(a))

a = 5
b = 7
c = 9

a, b, c = 5, 7, 9
print(a, b, c)

#함수 -> 코드를 묶어놓은 것
def myfunc1():
    return 3, 4

a = myfunc1()
print(type(a))

b, c = a
print(b, c)

a = 5
b = 7

#두 개의 변수값을 서로 exchange, swap
c = a; a = b; b = c
print('a=',a,'b=',b)

b, a = a, b
print('a=',a,'b=',b)

a = (1,2,3,4,5,6,7,8,9,10)
print(a[0])
print(a[1])
print(a[2])

# del a[2] 
# a[2] = 11

print(a[:5])
print(a[2:5])
print(a[::-1])

b = a + a
print(b)

b = a * 3
print(b)