# 이름 국어 영어 수학 총점 평균     평균으로 수(90) 우(80) 미(70) 양(60) 가(60 미만)

score_list = []
for i in range(3):
    student = {}
    student['name'] = input(f'5 명중 {i + 1}번째 학생 이름 : \t')
    student['kor'] = int(input(f'5 명중 {i + 1}번째 학생 국어 성적 : \t'))
    student['eng'] = int(input(f'5 명중 {i + 1}번째 학생 영어 성적 : \t'))
    student['math'] = int(input(f'5 명중 {i + 1}번째 학생 수학 성적 : \t'))
    score_list.append(student)

for score in score_list: 
    score['total'] = score['kor'] + score['eng'] + score['math']
    score['avg'] = score['total'] / 3
    score['grade'] = '수' if score['avg'] >= 90 else '우' if score['avg'] >= 80 else '미' if score['avg'] >= 70 else '양' if score['avg'] >= 60 else '가'

for score in score_list: print(f"{score['name']}학생 국어:{score['kor']}\t 영어:{score['eng']}\t 수학:{score['math']}\t 총점:{score['total']}\t 평균:{score['avg']}\t 급수:{score['grade']}")