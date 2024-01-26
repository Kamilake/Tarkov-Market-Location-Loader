스크린샷_저장_경로 = "스크린샷/"
페이지_지연_시간 = 3 # 3초
파일_변경_확인_주기 = 1 # 1초
타르코프_마켓_URL = "https://tarkov-market.com/maps/customs"

######################################

import sys
from selenium import webdriver
import os
import time

import get_chrome_driver
from selenium.webdriver.common.by import By

# ChromeDriver 설정 및 웹 드라이버 초기화
get_chrome_driver.GetChromeDriver().install()
driver = webdriver.Chrome()

# 타르코프 마켓 열기
url = 타르코프_마켓_URL
driver.get(url)

# 약간의 지연 시간을 주어 페이지 로딩 대기 (필요 시 조정 가능)
time.sleep(페이지_지연_시간)

while True:
  # 입력 필드 찾기
  try:
    input_field = driver.find_element(By.XPATH, '//input[@placeholder="Paste file name here"]')
  except:
    button = driver.find_element(By.XPATH, '//button[text()="Where am i?"]')
    button.click()

    input_field = driver.find_element(By.XPATH,'//input[@placeholder="Paste file name here"]')

  # 최신 스크린샷 파일 이름 가져오기
  folder_path = 스크린샷_저장_경로
  files = os.listdir(folder_path)
  paths = [os.path.join(folder_path, basename) for basename in files]
  if len(paths) > 0:
    latest_file = max(paths, key=os.path.getmtime)
    latest_file_name = os.path.basename(latest_file)

    # 현재 값과 새로운 값이 다른 경우에만 입력 필드 업데이트
    current_value = input_field.get_attribute('value')
    if current_value != latest_file_name:
      input_field.clear()
      input_field.send_keys(latest_file_name)
      print ("붙여넣기 완료")
  else:
    input_field.clear()

  # 파일_변경_확인_주기 초마다 반복
  time.sleep(파일_변경_확인_주기)