
# 1. 패키지 install

import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()

sheet= wb.active

sheet.append(['제목','채널명','조회수','좋아야수'])

raw = requests.get('https://tv.naver.com/r')

html = BeautifulSoup(raw.text,'html.parser')

container = html.select('div.inner')

for con in container:
    t = con.select_one("dt.title").text.strip() #제목
    c = con.select_one("dd.chn").text.strip() #채널
    h = con.select_one("span.hit").text.strip() #조회수
    l = con.select_one("span.like").text.strip() #좋아요수
    sheet.append([t,c,h,l])
wb.save('naver_tv.xlsx')
