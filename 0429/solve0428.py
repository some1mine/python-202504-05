def is_even(n):
    if n % 2 == 0: return True
    return False

def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): return True
    return False

print(is_even(13))
print(is_even(14))
print(is_leap(2000))
print(is_leap(2100))
print(is_leap(2004))
print(is_leap(2003))