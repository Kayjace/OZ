from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pymysql

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

url = "https://kream.co.kr"
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.RETURN)
time.sleep(0.5)

for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

def create_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='username',
            password='pass',
            database='scheme_name',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.Dictcursor
            )
        return connection
    except pymysql.Error as e:
        print(f"Error to connect mySQL: {e}")
        return None
    
def create_table_if_not_exists(connection):
    try:
        with connection.cursor() as cursor:
            # 테이블이 존재하지 않으면 생성
            create_table_query = """
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                brand VARCHAR(255) NOT NULL,
                price INT NOT NULL
            )
            """
            cursor.execute(create_table_query)
        connection.commit()
        print("Table 'products' is ready")
    except pymysql.Error as e:
        print(f"Error creating table: {e}")
    
def insert_product(connection, product_name, product_brand, product_price):
    try:
        with connection.cursor() as cursor:
            query = """INSERT INTO products (name, brand, price) 
                       VALUES (%s, %s, %s)"""
            cursor.execute(query, (product_name, product_brand, product_price))
        connection.commit()
        print("Product inserted successfully")
    except pymysql.Error as e:
        print(f"Error inserting product: {e}")

connection = create_connection()
create_table_if_not_exists(connection)

for item in items:
    product_name = item.select_one(".translated_name").text
    if "후드" in product_name :
        product_brand = item.select_one(".product_info_brand.brand").text
        product_price = item.select_one(".amount").text
        price_int = int(product_price.replace(',', '').replace('원', ''))
        insert_product(connection, product_name, product_brand, price_int)

        print(f"제품명 : {product_name}")
        print(f"브랜드명 : {product_brand}")
        print(f"가격 : {product_price}")
        print()
connection.close()
driver.quit()