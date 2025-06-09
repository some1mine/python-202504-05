#while문은 조건식을 만족할 때 내부 로직을 수행한다, 한 번도 수행되지 않을 수 있다.

'''
while 조건식 :  조건식의 결과가 True일 때 수행
    ....
    ....
    ....
'''
# i = 1
# while i <= 10:
#     print(i, end = '\t')
#     i += 1 #탈출 조건의 지정을 마지막 줄에 하는 패턴을 교수님이 선호

# useful for processing error, db, file... etc

# num = input('숫자로 입력하세요 : ')
# while ord(num) > ord('9') and ord(num) < ord('0'): 
#     num = input('숫자로 입력하세요(0 ~ 9) : ')

#등차가 1이고 초항이 1인 등차 수열의 합이 1000이 넘는 지점을 구하는 데에는 while문이 적합
plus_one_total = 0; end_point = 1
while plus_one_total < 1000: 
    plus_one_total += end_point
    end_point += 1
print(end_point - 1)