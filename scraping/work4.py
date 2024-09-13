from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=375,812")  # iPhone X 해상도
options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.76 Mobile/15E148 Safari/604.1")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("excludeSwitches", ["enable-automation"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)

if "onboarding/intro.htm" in driver.current_url:
    logo_element = driver.find_element(By.CLASS_NAME, "link-logo")
    logo_element.click()
    time.sleep(2)  # 페이지 로딩 대기

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(4)  # 페이지 로딩 대기


# 특정 'moreBtn' 클릭 (예: hasMore2() 함수를 호출하는 버튼)
more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='moreBtn' and @onclick='hasMore2();']")))
more_button.click()
time.sleep(2)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# _chartList 내부의 list_item들만 선택
chart_list = soup.select_one("ul#_chartList.service_list.list_music")

songs = chart_list.select("li.list_item")

#아래 순서대로 스크래핑한 자료를 출력해주세요
#순위 :
#노래 제목 :
#가수 이름 :
for song in songs:
    try:
        rank = song.select_one(".ranking_num").text.strip()
        title = song.select_one(".title.ellipsis").text.strip()
        artist = song.select_one(".name.ellipsis").text.strip()
        
        # '위' 텍스트 제거
        rank = rank.replace('위', '').strip()
        
        print(f"순위: {rank}")
        print(f"제목: {title}")
        print(f"가수: {artist}")
        print()
    except AttributeError as e:
        print(f"데이터 추출 중 오류 발생: {e}")

driver.quit()