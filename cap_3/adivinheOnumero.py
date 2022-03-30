#Este é um jogo de adivinhar o numero.
import random
numeroSecreto = random.randint(1,20)
print('Estou pensando em um numero entre 1 e 20')

#Pedindo para o jogador adivinhar 6 vezes
for tentativas in range(1,7):
    print('Tente Adivinhar')
    palpite = int(input())

    if palpite < numeroSecreto:
        print('Seu palpite foi baixo')
    elif palpite > numeroSecreto:
        print('Seu palpite foi alto')
    else:
        break # essa condição corresponde ao palpite correto

if palpite == numeroSecreto:
    print('Parabéns! Você acertou meu numero em ' + str(tentativas) + ' tentativas')
else:
    print('Acabaram suas chances :(')
    print('O numero secreto era: ' + str(numeroSecreto))
