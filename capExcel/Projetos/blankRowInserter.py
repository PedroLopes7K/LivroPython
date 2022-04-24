import sys, openpyxl

#n = int(sys.argv[1])
#m = int(sys.argv[2])
#file = sys.argv[3]
n = int(input('N: '))
m = int(input('M: '))
file = input('File name: ')
rwb = openpyxl.load_workbook(file)
rsheet = rwb.active

wwb = openpyxl.Workbook()
wsheet = wwb.active
#print(rsheet.max_row)
for a in range(1, rsheet.max_row + 1):
    for b in range(1, rsheet.max_column + 1):
        # Write rows normally until n is encountered
        if a < n:
            wsheet.cell(row = a, column = b).value = rsheet.cell(row = a, column = b).value
        # da um salto de m linhas, assim que a == n
        else:
            wsheet.cell(row=(a+m), column=b).value = rsheet.cell(row=a, column=b).value
wwb.save('inserted_{}'.format(file))
        

