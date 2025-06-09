#과제1. 정수를 받아 짝수면 True 홀수면 False를 반환하는 함수
def is_even(n):
    return not n % 2
#과제2. 윤년 계산 True/ False(4년마다, 100년 단위는 x, 400년 단위는 o)
def is_leap_year(n):
    # return bool(not n % 400 or (n % 100 and not n % 4))
    if not n % 400: return True
    if not n % 100: return False
    if not n % 4: return True
    else: return False

print(is_even(13))
print(is_even(14))
print(is_leap_year(2000))
print(is_leap_year(2100))
print(is_leap_year(2004))
print(is_leap_year(2003))
