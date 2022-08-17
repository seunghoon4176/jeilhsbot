from ctypes.wintypes import HWND
import time, requests, win32con, win32api, win32gui
from bs4 import BeautifulSoup

# 메세지 입력
def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

# 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# 핸들
def setupHwnd(kakao_opentalk_name) :
    global hwndMain, hwndEdit, hwndListControl
    hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit50W", None)
    hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None) 