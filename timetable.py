from calendar import month
from itertools import count
import os
from re import L
import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def getTimeTable() :
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

        browser.find_element(By.XPATH,'//*[@id="all-scroll"]/div/form/div/article/div[3]/dl/dd/a[2]/img').click() #xpath값 클릭하기
        time.sleep(3) # 대기 시간

    weekk = { 
        "Sunday" : "일",
        "Monday" : "월",
        "Tuesday" : "화",
        "Wednesday" : "수",
        "Thursday" : "목",
        "Friday" : "금",
        "Saturday" : "토"
    }
    tooday = datetime.today()
    monthh = tooday.month
    weekday = datetime.today().strftime('%A')
    today = datetime.today().strftime(f'{monthh}월%d일({weekk[weekday]})')

    filename = (f"C:/Users/Jeju/Downloads/{ today }-탑재용.xlsx")
    df=pd.read_excel(filename, engine = "openpyxl",usecols = "X")
    list_col2 = df.loc[:, df.columns[0]].to_list()
    print_list = []
    timeTable = ["[오늘의 시간표]"]

    for i in list_col2 :
        if type(i) != float :
            print_list.append(i[0:i.find("\n")])
        else :
            continue

    for i in print_list :
        if i == "" :
            continue
        timeTable.append(i)

    s = "\n".join(timeTable)

    return s

