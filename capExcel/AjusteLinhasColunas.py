# ALTURA DE LINHAS E LARGURA DE COLUNAS
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Linha Alta'
sheet['B2'] = 'Coluna Larga'

# setar aultra e largura
sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20
sheet.column_dimensions['C'].width = 20
wb.save('dimencoes.xlsx')
print('Sucess')
    
