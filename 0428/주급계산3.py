#주급계산 이름, 근무 시간, 시간당 급여액 - 5명에 대한

infos = [input('주급 계산을 위한 5명의 이름, 근무 시간, 시간당 급여액을 입력해주세요[ex. 홍길동 13 10030] : ').split() for _ in range(5)]
work_hours = [i[1] for i in infos]; pays = [i[2] for i in infos]