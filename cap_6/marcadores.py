#! python3
#Marcadores.py - Acrescenta martcadores no inicio de cada linha copiada

import pyperclip
texto = pyperclip.paste()

# separa as linhas e acrescenta os asteriscos
linhas = texto.split('\n')
for i in range(len(linhas)): # percorre todos os indices da lista 'linhas' em um loop
    linhas[i] =  str([i]) + '*' + linhas[i]# acrescenta um asterisco em cada string da lista 'linhas'

texto = '\n'.join(linhas)
pyperclip.copy(texto)
