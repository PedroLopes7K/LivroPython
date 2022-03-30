while True:
    print('Quem é você?')
    nome = input()
    if nome != 'Pedro':
      continue
    print('Olá Pedro! Qual sua senha?')
    senha = input()
    if senha == 'Geralda':
       break
print('ACESSO AUTORIZADO')
