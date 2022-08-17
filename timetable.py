from selenium.webdriver.common.by import By
from lib2to3.pgen2 import driver
from os import scandir
from sched import scheduler
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# 크롤링(시간표)
url = 'https://jeil.jje.hs.kr/jeil-h/0208/board/16996'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('#all-scroll > div > div > div.board-text > table.wb > tbody > tr:nth-child(1) > td.link > a')

a = str(content)
b = a.split(',')
c = b[1].strip("'")

# 셀레니움
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

url_path = 'https://jeil.jje.hs.kr/jeil-h/0208/board/16996/{}'.format(c) # URL 저장 

browser.implicitly_wait(1) # 대기 시간
browser.get(url_path) # url로 이동
browser.implicitly_wait(1) # wait time

dwnLink1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[2]/div/form/div/article/div[3]/dl/dd/a[1]') #xpath값 클릭하기
dwnLink2 = dwnLink1.find_element(By.TAG_NAME, 'href')

print(dwnLink1)
time.sleep(3) # 대기 시간