#지방 노동청에 회사에 남녀 임금차별 신고가 들어옴 
#전체 10명, 성별과 연봉을 입력 받아 남/녀 각각의 평균을 구하기
workers = []
for i in range(1, 11):
    sex = input(f'전체 10명 중 {i:2}번째 사람의 성별(남/여) : ')
    salary = int(input(f'전체 10명 중 {i:2}번째 사람의 연봉 : '))
    workers.append({'sex' : sex, 'salary' : salary})

man_salaries = [w['salary'] for w in workers if w["sex"] == "남"]
woman_salaries = [w['salary'] for w in workers if w["sex"] == "여"]

if man_salaries: print('남자평균 : ', sum(man_salaries) / len(man_salaries))
if woman_salaries: print('여자평균 : ', sum(woman_salaries) / len(woman_salaries))