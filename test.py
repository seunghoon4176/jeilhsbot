from bs4 import BeautifulSoup
import requests

url = 'https://jeil.jje.hs.kr/' # 학교 메인 홈페이지 URL

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('#container > div.main_content > div.meal_menu > ul > li')
    lunch_menu = content.find_all(text=True) # 텍스트만 찾아서 추출 후 리스트 형태로 저장
    
s = "\n".join(list(lunch_menu))
print(s)