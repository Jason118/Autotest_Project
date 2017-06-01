# from tools.read_xls import ReadXls

from xlrd import open_workbook

from src.utils import Config

wbpath = Config().get('data', 'path')
XLSX = ['zhigou.xlsx', 'merchantcenter.xlsx', 'personalcenter.xlsx', 'shopping.xlsx']
count = 0
for i in XLSX:
    print 'Case file is: " {0} ",'.format(i),
    book = wbpath + i
    wb = open_workbook(book)
    sheets = wb.nsheets
    print 'there are {0} Sheets in this file. Details:'.format(sheets)
    for j in range(sheets):
        sheet = wb.sheet_by_index(j)
        print '    Case Num in Sheet {0} is {1}'.format(sheet.name, (sheet.nrows - 2))
        count += (sheet.nrows - 2)
    print

print 'Total Num of Cases:{0}'.format(count)