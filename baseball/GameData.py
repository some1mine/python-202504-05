import random

class Baseball:
    def __init__(self):
        self.com = [-1, -1, -1]
        self.person = [-1, -1, -1]
        self.resultList = []

    def init_com(self):
        cnt = 0
        while cnt < 3:
            v = random.randint(0, 9)
            if v not in self.com:
                self.com[cnt] = v
                cnt += 1
    
    def init_person(self):
        s = input('숫자 3개(0~9 중 선택)를 중복 없이 입력하세요(ex 0 1 2) : ')
        num_list = s.split()
        self.person[0] = int(num_list[0])
        self.person[1] = int(num_list[1])
        self.person[2] = int(num_list[2])

    def get_result(self):
        strike = 0 
        ball = 0
        out = 0
        for i in range(3):
            if self.com[i] == self.person[i]: strike += 1
            elif self.person[i] in self.com: ball += 1
            else: out += 1
        return strike, ball, out
    
    def start(self):
        flag = False
        self.init_com()
        print(self.com)
        count = 0
        while not flag and count <= 5:
            self.init_person()
            count += 1
            strike, ball, out = self.get_result()
            print(f'strike : {strike} | ball : {ball} | out : {out}')
            if strike == 3: flag = True
        self.resultList = [flag, count]

if __name__ == '__main__':
    b = Baseball()
    # b.init_com()
    # b.init_person()
    # print(b.com)
    # print(b.person)
    # b.get_result()
    b.start()