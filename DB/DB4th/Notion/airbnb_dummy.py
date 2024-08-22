import pymysql
from faker import Faker
import random

# Faker 객체 초기화
fake = Faker()

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='208300',  # 데이터베이스 비밀번호
    db='airbnb',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


# Products 테이블을 위한 더미 데이터 생성
def generate_product_data(n):
    for _ in range(n):
        product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()
        price = round(random.uniform(10, 100), 2)
        stock_quantity = random.randint(10, 100)
        create_date = fake.date_time_this_year()
        yield (product_name, price, stock_quantity, create_date)

# Customers 테이블을 위한 더미 데이터 생성
def generate_customer_data(n):
    for _ in range(n):
        customer_name = fake.name()
        email = fake.email()
        address = fake.address()
        create_date = fake.date_time_this_year()
        yield (customer_name, email, address, create_date)

# Orders 테이블을 위한 더미 데이터 생성
def generate_order_data(n, customer_ids):
    for _ in range(n):
        customer_id = random.choice(customer_ids)
        order_date = fake.date_time_this_year()
        total_amount = round(random.uniform(20, 500), 2)
        yield (customer_id, order_date, total_amount)

def check_stock_and_update(quantity_sold, product_id, cursor, conn):
    sql_select = "SELECT stockQuantity FROM Products WHERE productID = %s"
    cursor.execute(sql_select, (product_id,))
    result = cursor.fetchone()

    if result is None:
        print(f"Product with ID {product_id} not found.")
        return False

    current_stock = result['stockQuantity']
    if current_stock < quantity_sold:
        print(f"Not enough stock for Product ID {product_id}. Current stock: {current_stock}, Ordered: {quantity_sold}")
        return False

    return True

table_names = ['Customers', 'Orders', 'Products']

# 데이터베이스에 데이터 삽입
with conn.cursor() as cursor:
    #데이터초기화
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    for table_name in table_names:
        try:
            print(f"Truncating table {table_name}")
            cursor.execute(f"TRUNCATE TABLE {table_name}")
        except Exception as e:
            print(f"Failed to truncate table {table_name}: {e}")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    conn.commit()

    # Products 데이터 삽입
    products_sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_product_data(10):
        cursor.execute(products_sql, data)
    conn.commit()

    # Customers 데이터 삽입
    customers_sql = "INSERT INTO Customers (customerName, email, address, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_customer_data(5):
        cursor.execute(customers_sql, data)
    conn.commit()

    # Orders 데이터 삽입
    # Customers 테이블에서 ID 목록을 얻어옵니다.
    cursor.execute("SELECT customerID FROM Customers")
    customer_ids = [row['customerID'] for row in cursor.fetchall()]
    
    orders_sql = "INSERT INTO Orders (customerID, orderDate, totalAmount) VALUES (%s, %s, %s)"
    for data in generate_order_data(15, customer_ids):
        cursor.execute(orders_sql, data)
    conn.commit()

#1. **새로운 제품 추가**: Python 스크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요. 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
    add_sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES (%s, %s, %s, %s)"
    cursor.execute(add_sql, ('Python Book', 29.99, 50, '2024-07-15 03:36:32'))
    print(f"New product added")
    conn.commit()

#2. **고객 목록 조회**: 'Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
    view_sql = "SELECT * FROM Customers"
    cursor.execute(view_sql)
    for row in cursor.fetchall():
        print(row)

#3. **제품 재고 업데이트**: 제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
    quantity_sold = 1
    product_id = 1
    if check_stock_and_update(quantity_sold, product_id, cursor, conn):
        update_sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
        cursor.execute(update_sql, (quantity_sold, product_id))
        print(f"product{product_id} sold {quantity_sold}, stock amount updated.")
        conn.commit()

#4. **고객별 총 주문 금액 계산**: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
    order_calc_sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
    cursor.execute(order_calc_sql)
    for row in cursor.fetchall():
        print(row)

#5. **고객 이메일 업데이트**: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
    new_email = "test@temp.com"
    customer_id = 1
    update_email_sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    cursor.execute(update_email_sql, (new_email, customer_id))
    print(f"customer{customer_id}'s email updated to {new_email}")
    conn.commit()

#6. **주문 취소**: 주문을 취소하는 Python 스크립트를 작성하세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
    order_id = 2
    del_order_sql = "DELETE FROM Orders WHERE orderID = %s"
    cursor.execute(del_order_sql, (order_id,))
    print(f"deleted order {order_id}")
    conn.commit()

#7. **특정 제품 검색**: 제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.
    select_prod_sql = "SELECT * FROM Products WHERE productName LIKE %s"
    cursor.execute(select_prod_sql, ('Python%'))
    for row in cursor.fetchall():
        print(row)

#8. **특정 고객의 모든 주문 조회**: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
    select_cid_sql = "SELECT * FROM Orders WHERE customerID = %s"
    cursor.execute(select_cid_sql, (1,))
    for row in cursor.fetchall():
        print(row)

#9. **가장 많이 주문한 고객 찾기**: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
    find_sql = "SELECT customerID, COUNT(*) as orderCount FROM Orders GROUP BY customerID ORDER BY orderCount DESC LIMIT 1"
    cursor.execute(find_sql)
    top_customer = cursor.fetchone()
    if top_customer:  # Ensure that top_customer is not None
        print(f"Top Customer ID: {top_customer['customerID']}, Orders: {top_customer['orderCount']}")
    else:
        print("No customers found.")

# 데이터베이스 연결 종료
conn.close()