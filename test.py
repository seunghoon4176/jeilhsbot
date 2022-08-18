import os
from bs4 import BeautifulSoup
import requests

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

today ="8월19일(금)-탑재용.xlsx"
filename = ("C:/Users/Jeju/Downloads/8월19일(금)-탑재용.xlsx")
df=pd.read_excel(filename, engine = "openpyxl",usecols = "X")


print(df)
