


spam =['maça', 'bananas', 'tofu', 'limao']


def funcao(lista):
    palavras = ''
    for i in range(len(lista) - 1):
       palavras += lista[i] + ', '
    palavras += 'And ' + lista[-1]
    print(palavras)

funcao(spam)

        
