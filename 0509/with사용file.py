import sys; import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# f = open('data/mpg.csv', 'r')
# line = f.readlines()
# print(line[:3])

# 파일과 상호작용하는 객체가 닫히지 않은 채로 새 객체를 변수에 할당하게 됨

# f = open('data/mpg.csv', 'r')
# line = f.readlines()
# print(line[:3])

with open('data/mpg.csv', 'r') as f: print(f.readlines()[:3])