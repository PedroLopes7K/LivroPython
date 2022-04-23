import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData= {}

# TO DO: Fill in countyData with each county's population and tracts.
# A FAZER: Preencher os dados do condado com a população e os dados de cada condado.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    #Each row in the spreadsheet has data for one census tract.
    # Cada fila da folha de cálculo tem dados para um tracto censitário..
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop   = sheet['D' + str(row)].value


    # SETDEFAULT() NÃO FARÁ NADA SE A CHAVE JÁ EXISTIR
    # Certifique-se de que a chave para este estado existe.
    #Make sure the key for this state exists.
    countyData.setdefault(state, {})
    #Certifique-se de que a chave para este condado neste estado existe.
    # Make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    #Cada fila representa um tracto censitário, por isso, incrementado por um.
    # Each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    #Aumentar o pop do condado pelo pop neste recenseamento.
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)
#Open a new text file and write the contents of countyData to it
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')


