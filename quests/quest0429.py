#오늘의 과제
words = ['assembly', 'java', 'rain', 'notebook', 'north',
         'south', 'hospital', 'programming', 'house', 'hour']

#문제1. filter 사용해서 6글자 이상만 출력
print(*filter(lambda x : len(x) >= 6, words))
#문제2. map 사용해 대문자로 바꾸어 출력
print(*map(lambda x : x.upper(), words))
#문제3. sorted 함수를 사용해 길이순으로 오름차순 정렬해 출력
print(sorted(words, key = lambda x : len(x)))
#문제4. sorted 함수를 사용하여 알파벳 순으로 내림차순으로 정렬하여 출력하기 
print(sorted(words, reverse =  True))
#문제5. 단어중에 o가 포함되는 단어가 모두 몇개인지 카운트하기 (힌트,filter를 사용)
print(len(list(filter(lambda x : 'o' in x, words))))