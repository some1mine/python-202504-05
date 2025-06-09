#성적 처리 3명이면
#name1, name2, name3
#list타입 => 배열
words = ['red', 'green', 'blue'] #list타입, 인덱싱과 슬라이싱을 지원한다
print(words[0])
print(words[1])
print(words[2])
print(words)

words.append('black')
words.append('cyan')
print(words)
print('단어개수', len(words))
print('red개수', words.count('red'))
print('red위치', words.index('red'))
print(f'yello위치 {words.index('yellow') if words.count("yellow") > 0 else -1}')

if words.count('yellow') > 0: print('yello의 위치', words.index('yellow'))
else: print('yello 없습니다')

if 'yellow' in words: print('yello의 위치', words.index('yellow'))
else: print('yello 없습니다')

#리스트는 인덱스로 요소 변경 가능
words[0] = 'white'
print(words)

s = 'white' #문자열은 불가능
s = s.replace('w', 'W')
print(s)
s = 'white'
s2 = 'W' + s[1:]
print(s2)

words.extend(['brown', 'violet', 'purple', 'margenta'])
print(words)

s = ', '.join(words)
print(s)

words2 = s.split(',')
print(words2)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0])
print(numbers[0::2])
print(numbers[0::-1])
print(numbers[1::2])

#리스트 만들기
names = []
names.append('홍길동')
names.append('임꺽정')
names.append('장길산')
names.append('홍경래')
print(names)

names = list()
names.append('모란')
names.append('작약')
names.append('불두화')
names.append('목련')

print(names)
