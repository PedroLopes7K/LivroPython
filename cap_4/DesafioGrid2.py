lista = [['B','L','J','C'],
         ['O','U','U','A'],
         ['L','I','I','R'],
         ['A','Z','Z','A']
         ]

for coluna in range(len(lista[0])):
    for linha in range(len(lista)):
        print(lista[linha][coluna], end = '')
    print('')
        
