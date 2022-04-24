import openpyxl

'''
Note-se que todas as filas 
acima e todas as colunas à esquerda desta célula serão congeladas, mas a fila 
e a coluna da própria célula não será congelada
'''
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2' # Congelar as filas acima de A2
wb.save('freezeExample.xlsx')
print('SUCESS')

#To unfreeze all panes, set freeze_panes to None or 'A1'
