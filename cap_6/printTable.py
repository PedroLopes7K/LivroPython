# Print a right justified table of data
# Imprimir uma tabela de dados justificada à direita

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tData):
    #colWidths = [0]*len(tableData)
    larguraColuna = []

    for fila in tData:
        comprimentoDePalavras = []
        for item in fila:
            comprimentoDePalavras.append(len(item))
        larguraColuna.append(max(comprimentoDePalavras))

    max_width = max(larguraColuna) + 2 
    print(fila,comprimentoDePalavras,larguraColuna,max_width)
    print('\n')
    

  # Print the data with max width
    print(' Table Data '.center(3*max_width,'='))
    for row in tData:
       for i in range(0,len(row)):
         #print(' ', end='')
         print(row[i])
         #print(row[i].rjust(max_width))
    print('/n')
 

  #Print the data with max width
 
    print(' Table Data '.center(4*max_width,'='))
    for row in tData:
     #print(' ', end='')
      print(row[0].rjust(10) + row[1].rjust(10) 
         + row[2].rjust(10) + row[3].rjust(10))

printTable(tableData)
