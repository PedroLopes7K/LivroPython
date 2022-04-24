import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = 100
sheet['A4'] =  '=SUM(A1:A3)'
#celula = sheet['D7']
#print(str(celula.row))
wb.save('Formulas.xlsx')
