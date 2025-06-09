#이름과 주소를 입력받아 한 문장으로 출력
#변수의 타입 지정하지 않는다.
a = 4
print(a, type(a)) #type 명령어는 변수 a의 타입이 아니라 a가 가리키는 값의 타입이라는 말씀

a = "test"
print(a, type(a))

a = 4.5
print(a, type(a))

name = input("당신의 이름은? :")
address = input("당신의 주소는? :")
#python의 경우에 + 연산자가 다른 값과 문자열을 결합시켜주지 않는다.
print(name + "님의 주소는", address + "입니다.")