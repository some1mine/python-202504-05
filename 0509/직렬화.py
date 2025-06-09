# 직렬화 - 객체를 바이너리 형식으로 저장
# 역직렬화 - 바이너리 형식으로부터 객체 형식으로
'''데이터 직렬화
메모리를 디스크에 저장하거나, 네트워크 통신에 사용하기 위한 형식으로 변환하는 것이다.
데이터 역직렬화
디스크에 저장한 데이터를 읽거나, 네트워크 통신으로 받은 데이터를 메모리에 쓸 수 있도록 변환하는 것이다.'''

import os; import sys; import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

data = {'name' : '홍길동', 'age' : 23, 'phone' : ['010-0000-0001', '010-0000-0002']}

with open('data/data.bin', 'wb') as f :
    pickle.dump(data, f)

r = {}
with open('data/data.bin', 'rb') as f :
    r = pickle.load(f)

print(r)