#escape 문자    \n-줄바꿈, \t 탭
s = 'I like star. \nred start\nblue star'
print(s)
s = 'apple\t pear\t cherry\t banana'
print(s)
s = 'C\test\temp'
print(s)

#escape기능 무력화 1.\\두번 2.앞에 r 붙이기
s = 'C\\test\\temp'
print(s)

s = r'C\test\temp'
print(s)

#문장 안에 ' 또는 "가 있을 때 처리 방식
s = 'I like \'stepany\''
print(s)

s = "I like 'stepany'"

#다른 언어의 경우 문자는 '' 문자열은 ""
#때로는 \를 직접 출력해야 하는 경우가 있다
s = "역슬래시(\\)는 특별한 기능을 갖는 문자이다."
print(s)

#print 사용방법
print("red", "green", "blue", sep = "\t")
print("yellow", "cyan", "magenta", sep = ', ')

print('*' * 20)

#문자열 포맷팅 - 문자, 숫자 섞어 문장 만들 때 사용한다. %s(String) | %d(decimal) | %f(float) | %자릿수 형식 | %10d | f의 경우는  %전체 자리수.소수점 이하 자리수f
name = '홍길동'
age = 34
height = 183.5
s = '%s의 나이는 %d이고 키는 %.2f입니다.' % (name, age, height)
print(s)

a = 37
print('8진수 %o' % a)
print('16진수 %x%%' % a)

print('%10s %10s' % ('hi', 'hello'))
print('%-10s %-10s' % ('hi', 'hello'))

a = 3.141592
print('%f' % a)
print('%.2f' % a)
print('%7.2f' % a)

print('이름 : {0} | 나이 : {1} {0}'.format(name, age))
print('이름 : {} | 나이 : {}'.format(name, age))
print('이름 : {name} | 나이 : {age} {name}'.format(name = name, age = age))

#문자열 앞에 f를 쓰고 {변수명} - f-string
print(f'이름 : {name} 나이 : {age}')

print('{0:<10} {1:<10}'.format('hi', 'hello'))
print('{0:>10} {1:>10}'.format('hi', 'hello'))
print('{0:^10} {1:^10}'.format('hi', 'hello'))
print('{0:=<10} {1:*^10}'.format('hi', 'hello'))

print('{0:.4f}'.format(3.141592))

x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {x + y}')