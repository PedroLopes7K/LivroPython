catNames = []
while True:
    print('Entre com o nome do gato ' + str(len(catNames) + 1) + 
      ' (Ou apenas tecle enter para sair):')
    nome = input()
    if nome == '':
        break
    catNames = catNames + [nome]  # concatenando lista (adicionando valores)
print('Os nomes dos gatos são:')
for nome in catNames:
    print('  ' + nome)
