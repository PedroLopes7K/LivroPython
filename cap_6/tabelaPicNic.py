def printPicnic(itensDicionario, larguraEsquerda, larguraDireita):
    print('PICNIC ITEMS'.center(larguraEsquerda + larguraDireita, '-'))
    for k, v in itensDicionario.items():
        print(k.ljust(larguraEsquerda, '.') + str(v).rjust(larguraDireita))

picnicItems = {'sanduiche': 4, 'maça': 12, 'copos': 4, 'biscoitos': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
