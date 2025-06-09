class Item:
    def __init__(self, name : str, price : int, count : int):
        self.name = name
        self.price = price
        self.count = count

    def output(self):
        print(f'{self.name}상품의 가격은 {self.price}원 입니다.')