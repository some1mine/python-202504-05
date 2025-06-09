from Vendor import Vendor

def main():
    vendor = Vendor()
    while True:
        print('=========================== 자판기 프로그램 ===========================')
        vendor.showItems()
        vendor.showCoins()
        if not vendor.hasStock():
            print('재고가 남아있는 상품이 없습니다. 다음에 다시 찾아주세요')
            return
        try:
            choices = [*map(int, input('결제할 상품들의 번호를 공백으로 구분해 모두 입력해주세요(중복가능, 입력 형식 불일치시 프로그램 종료됩니다) : ').split())]
            vendor.purchase(choices, int(input('지불금액을 입력해주세요(입력 형식 불일치시 프로그램 종료됩니다) : ')))
        except:
            return

if __name__ == '__main__': 
    main()