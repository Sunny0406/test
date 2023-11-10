from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 設定瀏覽器選項
options = Options()
# 建立 driver
s = Service(r"C:\Dynamic Web Crawler\chromedriver.exe")
chrome = webdriver.Chrome(service=s, options=options)
# 存取 Website
url = "https://www.google.com.tw/"
chrome.get(url)
search_box = chrome.find_element(By.NAME,'q')
search_query = "new jeans"
search_box.send_keys(search_query)
search_box.send_keys(Keys.ENTER)
# 等待 5 秒鐘以載入頁面
time.sleep(30)
# 關閉瀏覽器視窗
chrome.close()