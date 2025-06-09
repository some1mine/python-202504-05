class Person:
    # 클래스 공간. 정의 시 실행되며 클래스 공통으로 사용됨
    age = 12
    phone = ['010-0000-0001', '010-0000-0002']

    def append(self, name = '임꺽정', age = 13, phone = '010-0000-0001'):
        self.name = name
        self.age = age
        if phone not in self.phone : self.phone.append(phone)
    
    def output(self):
        print(self.name, self.age, self.phone)

    def __init__(self): # 인스턴스 변수는 생성자에서 정의하는 걸로
        self.name = ''
        self.age = 0
        self.phone = []

p1 = Person()
p1.append('장길산', 11, '010-0000-0003')

p2 = Person()
p2.append('김종서', 12, '010-0000-0004')

p1.output()
p2.output()