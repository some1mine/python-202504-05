#오늘의 과제
#문제1. filter 사용해서 6글자 이상만 출력
#문제2. map 사용해 대문자로 바꾸어 출력
#문제3. sorted 함수를 사용해 길이순으로 오름차순 정렬해 출력
#문제4. sorted 함수를 사용하여 알파벳 순으로 내림차순으로 정렬하여 출력하기 
#문제5. 단어중에 o가 포함되는 단어가 모두 몇개인지 카운트하기 (힌트,filter를 사용)
words = ['assembly', 'java', 'rain', 'notebook', 'north',
         'south', 'hospital', 'programming', 'house', 'hour']

#x에 전달되는 건 string타입, len(x) 문자열 길이
result_list = list(filter(lambda x : len(x) >= 6, words))
print(result_list)

result_list = list(map(lambda x : x.upper(), words))
print(result_list)

result_list = sorted(words, key = lambda x : len(x))
print(result_list)

result_list = sorted(words, reverse = True)
print(result_list)

result_list = list(filter(lambda x : 'o' in x, words))
print(len(result_list))

a = ['a', 'b', 'c', 'd', 'e']
b = [1, 2, 3, 4, 5]
print(*zip(a, b, a))