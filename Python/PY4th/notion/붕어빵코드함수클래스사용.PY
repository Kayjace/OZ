#붕어빵가게 클래스 선언
class BungeoppangShop:
    #생성자에서 재고, 가격, 판매량 dafault 설정
    def __init__(self):
        self.stock = {
            "팥붕어빵": 10,
            "슈크림붕어빵": 8,
            "초코붕어빵": 5
        }
        self.prices = {
            "팥붕어빵": 1000,
            "슈크림붕어빵": 1200,
            "초코붕어빵": 1500
        }
        self.sales = {
            "팥붕어빵": 0,
            "슈크림붕어빵": 0,
            "초코붕어빵": 0
        }

    #재고 출력 함수
    def check_stock(self):
        print("현재 붕어빵 재고:")
        for bread, quantity in self.stock.items():
            print(f"{bread}: {quantity}개")
        print('----------------------------------')

    #가격 출력 함수
    def check_prices(self):
        print("현재 붕어빵 가격:")
        for bread, price in self.prices.items():
            print(f"{bread}: {price}원")
        print('----------------------------------')
    
    #재고와 가격을 같이 보여주는 함수
    def check_stock_and_prices(self):
        print("현재 붕어빵 재고와 가격:")
        for bread in self.stock:
            quantity = self.stock[bread]
            price = self.prices.get(bread, '정보 없음')  # 가격이 없는 경우 '정보 없음'으로 표시
            print(f"{bread}: {quantity}개, {price}원")
        print('----------------------------------')

    #주문 함수
    def process_order(self):
        while True:
            #주문시마다 주문자 편의를 위해 붕어빵의 목록, 재고, 가격을 보여줌.
            self.check_stock_and_prices()
            #붕어빵 종류 입력받음. 종료시 Break.
            bread_type = input("주문할 붕어빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵). 종료를 원하시면 '종료'를 입력하세요: ")
            if bread_type == "종료":
                break
            #재고에 존재하는 붕어빵인지 확인하고 아닐 시 다시 주문받음
            if bread_type not in self.stock:
                print("존재하지 않는 붕어빵입니다. 다시 입력해 주세요.")
                print('----------------------------------')
                continue
            #붕어빵 개수 입력받고 없을시 다시 주문받음
            bread_count = self.get_integer_input("주문할 붕어빵 개수를 입력하세요: ")
            if bread_count is None:
                continue
            #재고 수량 체크 후, 판매 가능하면 재고 감소, 판매량 증가 후 판매메시지 출력
            if self.stock[bread_type] >= bread_count:
                self.stock[bread_type] -= bread_count
                self.sales[bread_type] += bread_count
                print(f"{bread_type} {bread_count}개를 판매했습니다.")
                print('----------------------------------')
            #재고 수량이 모자랄 시 부족메세지 출력
            else:
                print(f"죄송합니다. {bread_type} 재고가 부족합니다.")
                print('----------------------------------')

    #관리자모드 함수
    def admin_mode(self):
        #종료시 break 혹은 재고추가, 가격설정, 품목추가, 품목제거 메뉴로 진입 가능.
        while True:
            action = input("재고추가, 가격설정, 품목추가, 품목제거, 종료 중 하나를 입력하세요: ")
            if action == "종료":
                break
            if action == "재고추가":
                self.add_stock()
            elif action == "가격설정":
                self.set_price()
            elif action == "품목추가":
                self.add_item()
            elif action == "품목제거":
                self.remove_item()
            else:
                print("잘못된 입력입니다. 다시 입력해 주세요.")

    #재고 추가 함수
    def add_stock(self):
        #종료 혹은 붕어빵 재고 보여주고 재고 추가 반복.
        while True:
            #사용자 편의와 로직상 재고 확인 등은 이 위치가 가장 좋아보임.
            self.check_stock()
            bread_type = input("추가할 붕어빵 종류를 입력하세요 (종료를 원하시면 '종료'를 입력하세요): ")
            if bread_type == "종료":
                break
            #붕어빵이 존재하는지 체크
            if bread_type not in self.stock:
                print("존재하지 않는 붕어빵 종류입니다. 다시 입력해 주세요.")
                continue
            #재고 추가 수량 설정. 재고 숫자형인지 체크
            additional_stock = self.get_integer_input(f"{bread_type}의 추가할 개수를 입력하세요: ")
            if additional_stock is None:
                continue
            #재고 추가 후 메세지 출력
            self.stock[bread_type] += additional_stock
            print(f"{bread_type}의 재고가 {additional_stock}개 추가되었습니다.")


    #가격 추가 함수
    def set_price(self):
        #종료 혹은 가격표 보여준 뒤 가격 설정 반복
        while True:
            self.check_prices()
            bread_type = input("가격을 설정할 붕어빵 종류를 입력하세요 (종료를 원하시면 '종료'를 입력하세요): ")
            if bread_type == "종료":
                break
            #붕어빵 종류가 존재하는지 체크
            if bread_type not in self.prices:
                print("존재하지 않는 붕어빵 종류입니다. 다시 입력해 주세요.")
                continue
            #가격 설정, 가격 숫자형인지 체크.
            new_price = self.get_integer_input(f"{bread_type}의 새로운 가격을 입력하세요: ")
            if new_price is None:
                continue
            #가격 변경 후 메세지 출력
            self.prices[bread_type] = new_price
            print(f"{bread_type}의 가격이 {new_price}원으로 변경되었습니다.")

    #품목 추가 함수
    def add_item(self):
        #종료 전까지 품목 추가 반복. 현재 존재하는 품목의 재고, 가격을 보여줌.
        while True:
            self.check_stock_and_prices()
            bread_type = input("추가할 붕어빵 종류를 입력하세요 (종료를 원하시면 '종료'를 입력하세요): ")
            if bread_type == "종료":
                break
            #동일한 종류 존재하는지 체크
            if bread_type in self.stock:
                print(f"{bread_type}는 이미 존재하는 품목입니다.")
                continue
            #초기 재고 설정 및 가격 설정, 숫자인지 체크
            initial_stock = self.get_integer_input(f"{bread_type}의 초기 재고 수량을 입력하세요: ")
            if initial_stock is None:
                continue
            price = self.get_integer_input(f"{bread_type}의 가격을 설정하세요: ")
            if price is None:
                continue
            #딕셔너리에 종류에 따른 재고, 가격 추가 후 판매량 0으로 디폴트값 설정. 품목추가 메세지.
            self.stock[bread_type] = initial_stock
            self.prices[bread_type] = price
            self.sales[bread_type] = 0
            print(f"{bread_type} 품목이 추가되었습니다. 초기 재고: {initial_stock}, 가격: {price}원")

    #항목 제거 함수
    def remove_item(self):
        while True:
            #종료 이전까지 품목 제거 가능. 존재하는 붕어빵인지 체크 후 재고, 가격 딕셔너리에서 삭제.
            self.check_stock_and_prices()
            bread_type = input("제거할 붕어빵 종류를 입력하세요 (종료를 원하시면 '종료'를 입력하세요): ")
            if bread_type == "종료":
                break
            if bread_type not in self.stock:
                print("존재하지 않는 붕어빵 종류입니다. 다시 입력해 주세요.")
                continue
            del self.stock[bread_type]
            del self.prices[bread_type]
            print(f"{bread_type} 품목이 제거되었습니다.")

    #정수형 체크 함수. 붕어빵 수량이 정수형으로 주어지는지 체크하기 위해 쓰임.
    def get_integer_input(self, prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            return None

    #전체 매출 계산 함수
    def calculate_total_sales(self):
        #총매출 계산
        total_sales = sum(self.sales[bread] * self.prices[bread] for bread in self.sales)
        #하나도 팔지 못했을 시 메세지
        if total_sales == 0:
            print("붕어빵을 하나도 팔지 못했습니다...")
        #판매된 붕어빵의 종류, 개수, 해당 종류의 매출 기록 후 총매출 출력
        else:
            print("판매된 붕어빵 내역:")
            for bread in self.sales:
                print(f"{bread}: {self.sales[bread]}개, 총 {self.sales[bread] * self.prices[bread]}원")
            print(f"총 매출: {total_sales}원")
#메인
def main():
    #클래스 지정
    shop = BungeoppangShop()
    while True:
        #판매 종료 시 전체 매출 계산 함수 출력 후 종료. 그외엔 주문받기, 관리자 모드 메서드 호출 가능.
        mode = input("원하는 모드를 선택하세요 (주문받기, 관리자모드, 판매종료): ")
        
        if mode == "판매종료":
            break
        
        if mode == "관리자모드":
            shop.admin_mode()
        
        elif mode == "주문받기":
            shop.process_order()
        
        else:
            print("잘못된 입력입니다.")
    shop.calculate_total_sales()

#스크립트로 실행될때만 실행되게 설정
if __name__ == "__main__":
    main()