#이름, 시간당 급여액, 근무 시간
name = input("이름 : ")
work_hour = int(input("일한 시간 : "))
pay_per_hour = int(input("시간당 급여액 : "))

total_pay = work_hour * pay_per_hour

#대부분의 언어는 문자열과 정수를 더하면 정수를 문자열로 바꾸지만 파이썬은 문자열 자동 변환이 이루어지지 않아 str로 바꿔서 결합시켜야 한다.
print(name + "님의 급여는", total_pay, "입니다")