name_list = []
work_time_list = []
pay_per_list = []
total_pay_list = []

for _ in range(5):
    name = input('이름 : ')
    work_time = int(input('일한 시간 : '))
    pay_per_hour = int(input('시간당 급여액 : '))

    name_list.append(name)
    work_time_list.append(work_time)
    pay_per_list.append(pay_per_hour)

for i in range(5):
    total = work_time_list[i] * pay_per_list[i]
    total_pay_list.append(total)

for i in range(5):
    print(f'{name_list[i]} {work_time_list[i]} {pay_per_list[i]} {total_pay_list[i]}')