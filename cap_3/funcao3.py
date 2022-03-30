import random #importando modulo random

def pegaNumeroAleatorio(num):
    if num == 1:
        return 'O numero gerado foi ' + str(num)
    elif num == 2:
        return 'O numero gerado foi ' + str(num)
    elif num == 3:
        return 'O numero gerado foi ' + str(num)
    elif num == 4:
        return 'O numero gerado foi ' + str(num)
    elif num == 5:
        return 'O numero gerado foi ' + str(num)
aleatorio = random.randint(1,5)
resultado = pegaNumeroAleatorio(aleatorio)
print(resultado)
