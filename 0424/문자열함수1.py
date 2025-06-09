s = 'hobby'
print(s.count('b'))
print(s.count('t'))

#문자열 인덱스
print(s.find('b'))
print(s.find('k'))
s = 'I like star. red star. blue star. I like star'
print(s.count('star'))
print(s.find('star'))

pos1 = s.find('star')
print(pos1)
pos2 = s.find('star', pos1 + 1)
print(pos2)
pos3 = s.find('star', pos2 + 1)
print(pos3)
pos4 = s.find('star', pos3 + 1)
print(pos4)

# pos1 = s.index('love') 없으면 인덱스 에러
# print(pos1)

print(i for i, c in enumerate(s) if c == 's')

s = ','.join('abcd')
print(s)

#리스트를 문장으로
s = ','.join(['cherry', 'banana', 'pear', 'grape'])
print(s)

#문장을 리스트로
lst = s.split(",")
print(lst)

print('hi'.upper()); print('HI'.lower())

s = '   hi      '
print('*' + s + '*')
print('*' + s.lstrip() + '*')
print('*' + s.rstrip() + '*')
print('*' + s.strip() + '*')

print("python".isalpha())
print('python1'.isalpha())

print('python'.isdigit())
print('123'.isdigit())

s = 'hello' #upper 바뀐 값을 반환, 원래 값은 안 바뀜
print(s.upper(), s)
s = s.upper()
print(s)