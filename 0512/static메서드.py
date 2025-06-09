#사칙연산 클래스
class Calculator:
    def __init__(this, x = 0, y = 0):
        this.x = x
        this.y = y
    def add(this): return this.x + this.y
    def sub(this): return this.x - this.y

c1 = Calculator()
print(c1.add())
print(c1.sub())

class Calculator2:
    @staticmethod
    def add(x, y): return x + y
    def sub(x, y): return x - y