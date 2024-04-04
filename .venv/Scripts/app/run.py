import xlwt
from bs4 import BeautifulSoup
import requests
def parse():
    page = requests.get("https://omsk.rabota.ru/vacancy/?query=Python")
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('h3', class_='vacancy-preview-card__title')
    description = ''
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')
    count = 1
    for data in block:
        if data.find('a'):
            description = data.text
            ws.write( count, 1, description)
            count=count+1
    wb.save('D:\output.xlsx')
parse()
