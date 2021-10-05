from openpyxl import Workbook
import csv

def csvtoexcel():
    csvfile = 'new.csv'
    wb = Workbook()
    ws = wb.active
    with open(csvfile, 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save('new.xlsx')


