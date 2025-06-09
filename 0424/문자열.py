s = "Python String"
s2 = 'Hello'
#여러 줄에 걸칠 때는 '''~''', """~"""

s3 = """
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
"""
print(s)
print(s2)
print(s3)

#인덱싱 0번부터 시작해서 0, 1, 2 ...
print(s[0])
print(s[1])
print(s[2])
# print(s[20]) # IndexError Index out of range

#슬라이싱   [시작:종료:증감치] 시작 위치부터 증감치만큼 증가 또는 감소하며 종료보다 하나 적게
print(s[0:3])
print(s[0:6])
print(s[0:6:2])
print(s[7:])
print("문자열의 길이", len(s))
print(s[len(s) - 1:0:-1])
print(s[len(s) - 1:-1:-1])
print(s[len(s) - 1::-1])
print(s[::-1])