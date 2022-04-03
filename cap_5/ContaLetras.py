import pprint
frase = 'Pedro Henrique'

contaLetras = {}

for letra in frase:
    contaLetras.setdefault(letra,0)
    contaLetras[letra] = contaLetras[letra] + 1
#pprint.pprint(contaLetras)

for letra in contaLetras:
   # print(letter)
   print('O caracter ' + letra + ' aparece ' + str(contaLetras[letra])+ ' vezes na frase!' )
