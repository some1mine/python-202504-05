#이름, 국어, 영어, 수학 성적을 입력 받아 총점과 평균을 구하여 출력

#입력 : 이름, 국어, 영어, 수학
name = input("이름은? : "); kor = int(input("국어 성적은 ? : ")); eng = int(input("영어 성적은 ? : ")); math = int(input("수학 성적은 ? : ")); total = kor + eng + math; avg = total / 3

#출력 : 총점, 평균
print(f"{name}님의 총점은 {total}이고 평균은 {avg}입니다") 