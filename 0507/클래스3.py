class Book:
    title = '채식주의자'
    def __init__(self, title = '쌍갑포차', price = 10000, count = 1):
        self.title = title
        self.price = price
        self.count = count
        self.process()

    def process(self):
        self.total_price = self.price * self.count
    
    def output(self):
        print(self.title, self.price, self.count, self.total_price)

    pass

b = Book()
b.output

b2 = Book('We Do Not Part')
b2.output()

b3 = Book('Search Inside Yourself')
b3.output()