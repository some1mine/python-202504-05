for i in [1,2,3,4,5,6,7,8,9,10]: print(i)

#range(시작, 종료 기준 인덱스, 증감치)
print(range(1, 11))
for i in range(1, 11): print(i)

a = list(range(1, 11))
print(a)

for k in range(2, 100, 2): print(k, end = ' ')
print()

#문제1. 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
for i in range(1, 101):
    print(i, end = '\t')        
    if not i % 10: print()
    
#문자의 unicode -> ord
print(ord('A'))
print(ord('B'))
print(ord('a'))
print(ord('0'))
print(ord('1'))
#chr(unicode값) -> 문자
print(chr(49))
print(chr(65))

#문제2. for문을 써서 알파벳 A~Z까지 출력하기
for i in range(ord('A'), ord('Z') + 1): print(chr(i), end = '\t')
print()

#문제3. 문장를 입력받아 각 문자의 개수를 출력하기[대소문자 구분하지 않음]
sentence = input("대소문자를 구분하지 않고 알파뱃이 등장한 횟수를 세기 위한 문장을 입력해주세요 ::").upper()
for i in range(ord('A'), ord('Z') + 1):
    print(f'{chr(i)}의 개수는 입력 안에 ====> {sentence.count(chr(i))}개 있습니다.')
print()

unicode_indices = [0,0,0,0,0 ,0,0,0,0,0,
       0,0,0,0,0 ,0,0,0,0,0,
       0,0,0,0,0 ,0]

for c in sentence:
    unicode_indices[ord(c) - ord('A')] += 1
for i in range(len(unicode_indices)):
    print(f'{chr(i + ord('A'))}의 개수는 :: {sentence.count(chr(i + ord('A')))}개 입니다.')
print()

d = {}
for c in sentence:
    if c in d: d[c] += 1
    else: d[c] = 1
for item in d.items(): print(item)