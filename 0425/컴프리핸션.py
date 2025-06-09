#컴프리핸션
a = [1,2,3,4,5,6,7,8,9,10]
b = a
a[2] = -3

print(a)
print(b)

#stack과 heap을 시스템이 프로세스에게 할당
#stack에는 변수들이 쌓여있고
#a = (1,2,3,4,5,6,7,8,9,10)
#b = a => b라는 메모리 공간을 스택에 만들고 a에 들어있는 튜플 데이터의 시작 주소를 복사한다, soft copy[얇은 복사]
#soft copy는 불필요한 복사 과정으로 인한 메모리 공간 낭비 및 오버헤드가 없다
#hard copy, deep copy는 직접 구현하거나 deepcopy 모듈 또는 for문, 컴프리핸션을 사용한다.

#hard copy 구현
b = []
for i in a: b.append(i)
b[3] = 99
print('a=', a, 'b=', b)

#컴프리헨션 : 리스트 복사   [변수 for 변수 in iterable객체 if condition]

c = [item for item in a] #hard copy
c[5] = 55
print('a=', a)
print('c=', c)

d = [item * 2 for item in a]
print('d=', d)

oddList = [x for x in a if x % 2 == 1]
print(oddList)

wordList = ['rain', 'desk', 'hospital', 'building', 'java', 'python',
            'cloud', 'rainbow', 'assembly', 'javascript', 'html', 'css']

#1. hard copy
wordList2 = [w for w in wordList]
print(wordList2)

#1. hard copy[대문자 변환]
wordList3 = [w.upper() for w in wordList]
print(wordList3)

#단어와 단어 길이
wordList3 = [(w, len(w), w.upper()) for w in wordList]
print(wordList3)

#길이 5이상만
wordList3 = [w for w in wordList if len(w) >= 5]
print(wordList3)

#문제1. 단어 중 java가 들어간 것
wordList3 = [w for w in wordList if 'java' in w]
print(wordList3)

#문제2. 단어 중 길이가 5미만인 것
wordList3 = [w for w in wordList if len(w) < 5]
print(wordList3)

#문제3. 단어 중 길이가 5미만이고 java가 들어간 것
wordList3 = [w for w in wordList if 'java' in w and len(w) < 5]
print(wordList3)
