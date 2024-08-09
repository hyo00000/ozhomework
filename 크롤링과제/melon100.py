from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



header_user= "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36"

options = Options()
options.add_argument(f"user-agent={header_user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://m2.melon.com/index.htm")
print(driver.current_url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".link-logo").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(1)

for i in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

# '더보기' 버튼 클릭
try:
    more_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "moreBtn"))
    )
    more_button.click()
except Exception as e:
    print("Error clicking '더 보기' button:", e)

for i in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".lst50, .lst100")

rankings = []
title_songs = []
singers = []

for item in items:
    ranking = item.select_one(".rank").get_text(strip=True)
    title_song = item.select_one(".ellipsis.rank01 a").get_text(strip=True)
    singer = item.select_one(".ellipsis.rank02 a").get_text(strip=True)

    rankings.append(ranking)
    title_songs.append(title_song)
    singers.append(singer)

driver.quit()

for i in zip(rankings, title_songs, singers):
    print(f"랭킹 : {i[0]}")
    print(f"노래제목 : {i[1]}")
    print(f"가수 : {i[2]}")
