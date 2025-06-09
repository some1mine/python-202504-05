'''
검색속도
순차검색 > 이분탐색 > 해쉬
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def my_filter(a, key):
    key = 5 #찾을 값
    find = False
    for i in range(len(a)):
        if key == a[i]:
            find = i; break
    if find == -1: print('not fonud')
    else: print(f'{find + 1}번째')

a = ['red', 'green', 'blue', 'cyan', 'gray']
pos = my_filter(a, 'cyan')
print(pos)

a = [{'name' : 'A', 'age': 12},
     {'name' : 'B', 'age': 13},
     {'name' : 'C', 'age': 14},
     {'name' : 'D', 'age': 15},
     {'name' : 'E', 'age': 16},
     ]

pos = my_filter(a, {'name' : 'C', 'age' : 34})
print(pos)

def my_filter2(func_key, lst):
    for i in range(len(a)):
        if func_key(a[i]): return i
    return -1

pos = my_filter2(lambda x : x['name'] == 'C', a)
print(pos)

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
def select_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]: arr[i], arr[j] = arr[j], arr[i]
    print(a)

def select_sorted_list(arr, f):
    a = [n for n in arr]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if f(a[i]) > f(a[j]): a[i], a[j] = a[j], a[i]
    return a

print(a)
print(select_sorted_list(a, lambda x : x))
print(a)
select_sort(a)
print(a)