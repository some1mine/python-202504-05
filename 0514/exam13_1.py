import re

zipcode = input('우편 번호를 입력하세요 : ')
pattern = r'\d{5}$'
regex = re.compile(pattern)
result = regex.match(zipcode)
if result == None: print('형식이 일치하지 않습니다.')

text = '''
    phone : 010-0000-0000   email:test1@nate.com
    phone : 010-1111-1111   email:test2@naver.com
    phone : 010-2222-2222   email:test3@gmail.com
    phone : 02-345-9090     email:dseisk@hanmail.com
'''
print()
print('--- 전화번호 추출하기 ---')
pattern = r'^.*?(0\d{1,2}-\d{3,4}-\d{4}).*$'
result = re.findall(pattern, text, flags = re.MULTILINE)
for i in result: print(i)