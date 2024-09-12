import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

keyword = input("검색할 키워드를 입력해주세요 : ")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&stab_jum&query=" + keyword

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html,"html.parser")

blog_items = soup.select("li.bx:not([class*='type_ad'])")

for item in blog_items:
    title_elem = item.select_one(".title_link")
    name_elem = item.select_one("a.name")
    
    if title_elem and name_elem:
        print(f"블로그 제목: {title_elem.text.strip()}")
        print(f"작성자: {name_elem.text.strip()}")
        
        if 'href' in name_elem.attrs:
            print(f"작성자 링크: {name_elem['href']}")
        else:
            print("작성자 링크를 찾을 수 없습니다.")
        
        print()