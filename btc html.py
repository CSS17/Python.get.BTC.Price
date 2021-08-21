from selenium import webdriver
import time
import os
from datetime import date
from datetime import datetime
import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
sayac=0
driver = webdriver.Chrome(options=options)
driver.get("https://www.binance.com/tr/trade/BTC_USDT")


while True: 
    now=datetime.now()
    if(now.second==10):
        tarih=str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"    "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)
        try:
            sonuc=driver.title.split(' ')[0].strip()
            print(tarih+" "+(driver.title.split(' ')[0].strip()))
            sheet1.write(sayac, 1, sonuc)
            sheet1.write(sayac,0, tarih)
        except Exception as ex:
            print('Exception:', ex)
        sayac+=1
        time.sleep(1)
    if(sayac==10):
        wb.save('BTC-USDT.xls')
        break        
                
        
        
   
   