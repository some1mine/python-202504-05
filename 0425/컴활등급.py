'''
컴퓨터활용능력시험
이름 필기(400) 워드(200) 스프레드시트(200) 프레젠테이션(200)

총점을 구해 A(800 이상) B(600 이상 800미만) C(400이상 600미만) D(400미만, 재시험 요망)
'''
name = input("이름 : ")
theory = int(input("필기(400만점) : "))
word = int(input("워드(200만점) : "))
spread_sheet = int(input("스프레드시트(200만점) : "))
presentation = int(input("프레젠테이션(200만점) : "))

total = sum([theory, word, spread_sheet, presentation])
if total >= 800:
    print(f'등급A, 총점{total}')
elif total >= 600:
    print(f'등급B, 총점{total}')
elif total >= 400:
    print(f'등급C, 총점{total}')
else:
    print(f'등급D, 총점{total}, 재시험 요망')