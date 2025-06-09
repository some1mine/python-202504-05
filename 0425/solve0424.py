# 문제5) 문자열 연습하기
# 5-1     변수에 값 "홍길동, 임꺽정, 장길산, 최영, 윤관, 강감찬, 서희, 이순신, 남이정"
# 5-2     list로 전환한 다음 
# 5-3     "서희"가 몇번째 있는지     
# 5-4     "이순신", "장영실"이 각각 있는지
# 5-5     "정도전", "정약용", "최지원" .... 추가
# 5-6     "서희" -> "김종서"로 바꾸기
# 5-7     "장길산" -> "김길산"으로 바꾸기

names = "홍길동, 임꺽정, 장길산, 최영, 윤관, 강감찬, 서희, 이순신, 남이정"
print(names, type(names))

nameList = names.split(", ") #전달된 값으로 문자열을 쪼개서 list타입으로 변환
print(nameList, len(nameList)) #list와 list길이

#인덱싱 list, String 인덱스를 통해 접근 가능 시작:0
print(nameList[0])

#슬라이싱   [시작값:종료값:증감치] 요소 생략 가능
print(nameList[3:])     #3번째 이후
print(nameList[:3])     #0~3-1까지
print(nameList[::-1])   #역순으로
print(nameList[2:5])    #2,3,4

print('서희의 위치 :', nameList.index('서희'))

#count함수와 in
if nameList.count('이순신') > 0: #0:False, 0아닌 값:True
    print('이순신이 존재한다')
else:
    print('이순신이 존재하지 않는다')
    
if '장영실' in nameList:
    print("'장영실'이 존재한다")
else:
    print("'장영실'이 존재하지 않는다")
    
print(nameList.count('이순신'), '장영실' in nameList)

nameList.append('정도전')
nameList.append('정약용')
nameList.append('최치원')

nameList.extend(['정도전', '정약용', '최치원'])
print(nameList)

pos = nameList.index('서희')
nameList[pos] = '김종서'

print(nameList)

pos = nameList.index('장길산')
nameList[pos] = nameList[pos].replace('장', '김')
print(nameList)