import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

keyword = input("검색할 키워드를 입력해주세요 : ")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&stab_jum&query=" + keyword

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html,"html.parser")

names = soup.select("a.name")
titles = soup.select(".title_link")

for title, name in zip(titles, names):
    print(f"블로그 제목: {title.text.strip()}")
    print(f"작성자: {name.text.strip()}")
    if 'href' in name.attrs:
        print(f"작성자 링크: {name['href']}")
    else :
        print(f"링크 정보를 가져올 수 없습니다")
    print()