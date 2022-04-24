import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
wb.sheetnames
['Sheet']
sheet = wb['Sheet']
italicFont = Font(size=15, italic=True)
sheet['A1'].font = italicFont
sheet['A1'] = 'Meu nome:'
sheet['B1'] = 'Pedro'
# quando não especificamos o tamanha, o padrao e size 11
estilo2 = Font(name='Times New Roman', bold=True)
sheet['B1'].font = estilo2

wb.save('styles.xlsx')
