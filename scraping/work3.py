import requests
from bs4 import NavigableString
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

response = requests.get(url, headers=header_user)
soup = BeautifulSoup(response.text, 'html.parser')

movie_list = soup.select('div.sect-movie-chart ol > li')

for movie in movie_list:
    #영화 순위 요소가 있는지 체크
    rank_element = movie.select_one('strong.rank')
    if not rank_element:
        print("영화정보 출력 완료")
        break
    # 영화 순위
    rank = rank_element.text
    # 영화 제목
    title = movie.select_one('strong.title').text
    
    # 예매율
    booking_rate = movie.select_one('strong.percent span').text
    
    # 개봉일자
    txt_info = movie.select_one('span.txt-info')
    strong_tag = txt_info.select_one('strong')
    if strong_tag:
        open_date = ''.join(child.strip() for child in strong_tag.children 
                        if isinstance(child, NavigableString)).strip()
    else:
        open_date = "날짜 정보 없음"
    
    print(f"순위: {rank}")
    print(f"제목: {title}")
    print(f"예매율: {booking_rate}")
    print(f"개봉일: {open_date}")
    print("-" * 50)