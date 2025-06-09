from Vendor import Vendor

def main():
    vendor = Vendor()
    print('=========================== 자판기 관리 프로그램 ===========================')
    while True:
        vendor.showItems()
        vendor.showCoins()
        try:
            choice = input('메뉴를 숫자로 선택해 주세요 1.상품입고 2.상품등록 3.상품삭제 4.거스름돈충전 0.종료 : ')
            if choice == '0': return
            if choice == '1': vendor.fillItem(*map(int, input('채울 상품의 번호와 수량을 입력해주세요 : ').split()))
            if choice == '2': vendor.addItem()
            if choice == '3': vendor.delItem(int(input('삭제할 상품의 상품번호를 입력해주세요 :')))
            if choice == '4':
                for coin in vendor.coins.keys():
                    vendor.fillCoin(coin, int(input(f'{coin}원의 수량을 입력해주세요 : ')))
        except:
            print('입력 형식을 맞춰주세요')
                
if __name__ == '__main__': 
    main()