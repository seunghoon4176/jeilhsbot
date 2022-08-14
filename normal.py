import time, win32con, win32api, win32gui, requests
from bs4 import BeautifulSoup

# 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
kakao_opentalk_name = '공동연구'

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

# 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# 크롤링(급식)
url = 'https://jeil.jje.hs.kr/' # 학교 메인 홈페이지 URL

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # content = soup.select_one('#container > div.main_content > div.meal_menu > ul > li')
    content = soup.select_one('#container > div.main_content > div.meal_menu > ul > li')
    lunch_menu = content.find_all(text=True) # 텍스트만 찾아서 추출 후 리스트 형태로 저장

    for i in lunch_menu :
        print(i)

# 크롤러가 웹 사이트에 접근할 수 없다면 status code 출력
else : 
    print(response.status_code)

# 크롤링(시간표)
url = 'https://jeil.jje.hs.kr/jeil-h/0208/board/16996'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # content = soup.select_one('#container > div.main_content > div.meal_menu > ul > li')
    content = soup.select_one('#container > div.main_content > div.meal_menu > ul > li')
    lunch_menu = content.find_all(text=True) # 텍스트만 찾아서 추출 후 리스트 형태로 저장

    for i in lunch_menu :
        print(i)

# 핸들
hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit50W", None)
hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

# 채팅 전송
text = ''.join(lunch_menu)
kakao_sendtext(text)