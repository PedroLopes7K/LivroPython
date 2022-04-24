import os, openpyxl, sys
# Mention the final xlsx filename in a command line argument
wb = openpyxl.Workbook()
wb.create_sheet(index= 0, title = 'converted')
sheet = wb.active
x = 1

for file in os.listdir():
    if file.endswith('.txt'):
        y = 1
        with open(file) as f:
            for a in f:
                sheet.cell(row = x,column = y).value = a
                y+=1
        x+=1

wb.save('texts.xlsx')
