#초기 설정 재고
stock = {
    "팥붕어빵": 10,
    "슈크림붕어빵": 8,
    "초코붕어빵": 5
}

#초기 설정 붕어빵 가격
price = {
    "팥붕어빵": 1000,
    "슈크림붕어빵": 1200,
    "초코붕어빵": 1500
}

#붕어빵 판매량 딕셔너리
sale_amount = {
    "팥붕어빵": 0,
    "슈크림붕어빵": 0,
    "초코붕어빵": 0
}

#최상위 메뉴
while True:
    command = input("주문받기, 관리자모드, 판매종료 중 하나를 입력하세요: ")
    #주문 받기 메뉴. 주문받을 붕어빵의 종류와 개수를 입력받고 종료시까지 연속해서 주문을 받는다.
    if command == "주문받기":
        while True:
            #주문 시작시 stock 아이템들을 가져와 주문자에게 재고를 보여줌.
            print("현재 붕어빵 재고: ")
            for typ, amt in stock.items():
                print(f"{typ}: {amt}개")
            #주문 받을 붕어빵의 종류를 입력받음.
            typ = input("붕어빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵): <주문을 모두 마치시면 종료 를 입력해주세요> ")
            #종료시 상위 메뉴로 돌아감.
            if typ == "종료":
                break
            #stock에 없는 종류의 입력을 받지 않음.
            if typ not in stock:
                print("잘못된 입력입니다.")
                continue
            
            #int 형태로 주문 개수를 입력받음.
            amount = int(input("붕어빵 개수를 입력하세요: "))

            #재고 체크 후, 재고가 충분하면 판매 후 재고와 판매량을 업데이트하고 계속해서 주문을 받는다.
            if stock[typ] >= amount:
                stock[typ] -= amount
                sale_amount[typ] += amount
                print(f"{typ}맛 {amount}개 판매되었습니다.")
            else:
                print(f"주문하신 상품의 재고가 부족합니다.")

    #관리자 메뉴. 재고의 추가와 가격 설정 가능.
    elif command == "관리자모드":
        while True:
            #행동을 입력받는다
            action = input("재고추가, 가격설정, 종료 중 하나를 입력하세요: ")

            #재고추가 메뉴. 재고 추가할 붕어빵 종류와 개수를 입력받는다.
            if action == "재고추가" :
                while True:
                    typ = input("추가할 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵): <추가를 모두 마치시면 종료 를 입력해주세요> ")
                    if typ == "종료":
                        break
                    #재고에 존재하지 않는 입력일 시 무효화
                    if typ not in stock:
                        print("잘못된 입력입니다.")
                        continue
                    #재고에 추가할 개수를 입력받고 추가 완료 메세지 및 재고 현황을 출력한다.
                    add_amount = int(input(f"추가할 {typ} 개수 : "))
                    stock[typ] += add_amount
                    print(f"{typ}이 {add_amount}개 추가되었습니다.")
                    print("현재 붕어빵 재고:")
                    for typ, amt in stock.items():
                        print(f"{typ}: {amt}개")

            #가격설정 메뉴. 가격을 설정할 붕어빵 종류와 새로운 가격을 입력받는다.
            elif action == "가격설정" :
                while True:
                    typ = input("가격을 설정할 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵): <설정을 모두 마치시면 종료 를 입력해주세요>")
                    if typ == "종료":
                        break
                    #가격 딕셔너리에 존재하지 않는 입력일 시 무효화
                    if typ not in price:
                        print("유효하지 않은 붕어빵입니다.")
                        continue
                    #붕어빵 가격 설정을 입력받고 붕어빵 가격 현황을 보여준다.
                    new_price = int(input(f"{typ}의 가격을 설정하세요: "))
                    price[typ] = new_price
                    print(f"가격 설정이 업데이트 되었습니다. 현재 붕어빵 가격: ")
                    for typ, prc in price.items():
                        print(f"{typ}: {prc}원")

            #종료 입력시 관리자모드를 벗어남
            elif action =="종료":
                break
            
            #관리자메뉴에서 유효하지 않는 입력의 무효화.
            else:
                print("유효하지 않은 입력입니다. 다시 입력해주세요.")

    #판매종료시 판매 내역과 매출을 표시한다.
    elif command == "판매종료":
        #하나도 팔지 못했을 때 보여주는 메세지
        all_zero = all(value == 0 for value in sale_amount.values())
        if all_zero :
            print("붕어빵을 하나도 팔지 못했습니다...")
        #판매량을 보여주고 매출을 계산해서 보여준다.
        else:
            print("판매된 붕어빵 내역: ")
            for typ, amt in sale_amount.items():
                if amt > 0:
                    print(f"{typ}: {amt}개")
        revenue = sum(sale_amount[typ] * price[typ] for typ in sale_amount)
        print(f"총 매출: {revenue}원")
        break

    #최상위 메뉴에서 주문받기, 관리자메뉴, 판매종료 이외의 입력을 무효화한다.
    else:
        print("잘못된 입력입니다.")






"""


요구사항:
- 손님이 "종료"를 입력할 때까지 주문을 계속 받습니다.

- 손님이 주문할 붕어빵의 종류와 개수를 입력받습니다.
- 현재 재고를 화면에 출력합니다.
- 손님의 주문 내용을 기반으로 재고를 업데이트합니다.
- 재고가 부족할 경우, 손님에게 재고 부족을 알리고 재고를 감소시키지 않습니다.
- 재고가 충분할 경우, 주문한 만큼 재고를 감소시키고 판매를 완료합니다.

- 판매가 완료된 경우 판매된 붕어빵 맛과 개수를 출력하세요.


관리자 모드를 통해 붕어빵 재고를 추가할 수 있는 기능을 구현하세요.
요구사항:
- 관리자는 특정 붕어빵의 재고를 추가할 수 있습니다.
- "종료"를 입력하면 관리자 모드를 종료합니다.
- 추가된 재고를 업데이트하고 현재 재고를 화면에 출력합니다.


붕어빵 판매 가격을 설정하고, 판매한 붕어빵의 매출을 계산하세요.
요구사항:
- 각 붕어빵의 가격을 딕셔너리로 관리합니다.
- 판매된 붕어빵의 종류와 개수를 딕셔너리로 관리합니다.
- 총 매출을 계산하여 출력합니다.


"""