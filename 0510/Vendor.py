from Item import Item

class Vendor:
    def __init__(self):
        self.items : list[Item] = [Item(f'상품{i}', (i + 1) * 1000, 20) for i in range(5)]
        self.coins : dict[int, int] = {c : 100 for c in (50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1)}
    
    '''
    관리자 메뉴
    '''

    def addItem(self) :
        try:
            name, price, amount = input('추가할 상품의 이름과 가격, 그리고 수량을 입력해주세요(ex. 음료 300 10) : ').split()
            self.items.append(Item(name, int(price), int(amount)))
        except ValueError:
            print('입력 형식을 맞춰주세요')
    
    def fillItem(self, idx : int, amount : int):
        self.items[idx].count += amount

    def delItem(self, idx : int):
        del self.items[idx]
            
    def fillCoin(self, coin, amount):
        self.coins[coin] += amount


    '''
    사용자 메뉴
    '''

    def purchase(self, choices : list[int], pay : int):
        for c in choices: 
            if not self.hasEnough(c):
                print('상품의 수량이 부족합니다.'); return None
        total = self.calcChangeAmount(choices, pay)
        if total < 0:
            print('금액이 부족합니다.'); return None
        change = self.calcChanges(total)
        if not change:
            print('거스름돈이 부족합니다.'); return None
        for k, v in change.items(): 
            self.coins[k] -= v
            print(f'=== {k}원짜리 {v}개 ===')
        for c in choices:
            self.items[c].count -= 1
        return change
    
    def hasEnough(self, choice : int):
        return self.items and \
            0 <= choice < len(self.items) and \
                self.items[choice].count > 0
    
    def calcChangeAmount(self, choices : list[int], pay : int):
        return pay - sum([self.items[c].price * choices.count(c) for c in set(choices)])

    def calcChanges(self, change : int):
        result = {c : 0 for c in self.coins}
        for k in sorted(self.coins.keys(), reverse = True):
            amount = min(self.coins[k], change // k)
            if change > 0 and amount:
                result[k] += amount; change -= k * amount
        if change: return None
        return result
    
    '''
    공통 메뉴
    '''

    def hasStock(self):
        for m in self.items:
            if m.count > 0: return True
        return False

    def showItems(self):
        for i in range(len(self.items)): print(f'{i}번 상품 {self.items[i].name}의 재고는 {self.items[i].count}개이며 가격은 {self.items[i].price}원입니다.')

    def showCoins(self):
        for coin, cnt in self.coins.items(): print(f'{coin}원 짜리는 {cnt}개 있습니다.')
