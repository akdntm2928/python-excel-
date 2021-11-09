import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

search  = '유미의세포'

sheet.append([search,'기사제목','기사요약'])


for p in range(1,10+1):
    # request을 통해서  해당 사이트에 dom정보을 가져온다.
    raw = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q={s}&p={p}".format(s = search, p = p)) 

    # 
    html =BeautifulSoup(raw.text,'html.parser')
    container = html.select('ul.list_news li')
    for c in container:
        # 기사 제목: div.wrap.tit a
        title = c.select_one("a.tit_main.fn_tit_u").text.strip()

        content = c.select_one("p.desc").text.strip()
        sheet.append([search,title,content])

wb.save('daum_news.xlsx')

