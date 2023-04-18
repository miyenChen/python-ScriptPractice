# 爬蟲基本套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# python基本套件不用下載，用於將數據存儲到CSV文件中。
import csv
from datetime import datetime

#設定執行檔路徑
options = Options()
options.chrome_executable_path = "E:/softave/chromedriver/chromedriver.exe"

#建立 Driver物件，用程式操作瀏覽器
driver = webdriver.Chrome(options=options)
driver.get("https://www.ptt.cc/bbs/stock/index.html")

# 抓取標題
tags = driver.find_elements(By.CLASS_NAME,"title")
for tag in tags:
    print(tag.text)

# 將數據存儲到CSV文件中
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 注意繁中需要指定編碼方式，否則會呈現亂碼
# open() 函數打開檔案，'date.csv' 檔案名稱，"a"附加模式，保存已有的資料往後新增，若檔案不存在會創建一個
# newline='' 則是為了避免在 CSV 檔案中插入空行。csvfile為變數名稱
# flush()防止腳本在資料正在寫入時關閉
with open('date.csv', "a", newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    for tag in tags:
        print(tag.text)
        writer.writerow([now, tag.text]) 
    csvfile.flush()
driver.quit()
