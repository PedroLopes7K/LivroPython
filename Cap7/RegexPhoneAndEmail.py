# Encontra números de telefone e endereços de e-mail no clipboard.

import pyperclip,re

# regex para numero de telefone
telefoneRegex = re.compile(r'''(
     (\d{3}|\(\d{3}\))? # codigo ddd
     (\s|-|\.)?  # separador
     (\d{3})     # primeiros 5 digitos(incluindo o 9)
     (\s|-|\.)   # separador
     (\d{4})    # ultimos 4 digitos
     )''', re.VERBOSE)

#regex para email
emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+  # nomde do usuario
  @   # simbolo @
  [a-zA-Z0-9.-]+   # nome do dominio
  (\.[a-zA-Z]{2,4})  # ponto seguido de outros caracteres
  )''',re.VERBOSE)


# encontrar a correspondência no texto do clipboard
texto = str(pyperclip.paste())

partes = []

for groups in telefoneRegex.findall(texto):
    numeroTel = '-'.join([groups[1], groups[3], groups[5]])
    #if groups[6]!= '':
     #   numeroTel += ' x' + groups[8]
    partes.append(numeroTel)
for groups in emailRegex.findall(texto):
    partes.append(groups[0])

if len(partes) > 0:
    pyperclip.copy('\n'.join(partes))
    print('Copiado para a area de transferência')
    print('\n'.join(partes) )
else:
    print('Não foram encontrados números de telefone e emails')
