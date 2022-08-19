from calendar import month
from itertools import count
import os
from re import L
from time import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = 'https://jeil.jje.hs.kr/' # 학교 메인 홈페이지 URL

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
content = soup.select_one('#container > div.main_content > div.meal_menu > ul > li')
temp = content.find_all(text=True) # 텍스트만 찾아서 추출 후 리스트 형태로 저장
result = []

for i in temp :
    if "★" in i :
        result.append(i)
    else :
        result.append(i[0:i.find("(")])

lunch_menu = "\n".join(result)

import pandas as pd


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

filename = (f"C:/Users/ssh41/Downloads/{ today }-탑재용.xlsx")
df=pd.read_excel(filename, engine = "openpyxl",usecols = "X")
list_col2 = df.loc[:, df.columns[0]].to_list()
print_list = []
timeTable = []

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
print(s)