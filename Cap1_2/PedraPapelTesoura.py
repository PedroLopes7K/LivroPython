import random, sys

print('PEDRA, PAPEÇ, TESOURA')

# Variaveis para armazenar numeros de vitorias,derrotas e empates

wins = 0
loss = 0
ties = 0

while True: #Laço principal do jogo
    print('%s Vitorias, %s Derrotas, %s Empates' % (wins,loss, ties))
    while True: # Laço de entrada do jogador
        print('Digite a sua jogada: (R)ocha/Pedra  (P)apel  (T)esoura ou (S)air')
        movimentoJogador = input()
        if movimentoJogador == 'S':
            sys.exit() # Sai do programa
        if movimentoJogador == 'R' or movimentoJogador == 'P' or movimentoJogador == 'T':
            break # quebra o loop de entrada do jogador
        print('Digite apenas um R, P, T OU S.')
    #Mostrar oque o jogador escolheu
    if movimentoJogador == 'R':
        print('Pedra contra...')
    elif movimentoJogador == 'P':
        print('Papel contra...')
    elif movimentoJogador == 'T':
        print('Tesoura contra...')

    #Mostra oque o computador escolheu
    numeroAleatorio = random.randint(1,3)
    if numeroAleatorio == 1:
        movimentoComputador = 'R'
        print('Pedra')
    elif numeroAleatorio == 2:
        movimentoComputador = 'P'
        print('Papel')
    elif numeroAleatorio == 3:
        movimentoComputador = 'T'
        print('Tesoura')

    #monstra os registrod de vitorias/derrotas/empates
    if movimentoJogador == movimentoComputador:
        print('Empatou!')
        ties = ties + 1
    elif movimentoJogador == 'R' and movimentoComputador == 'T':
        print('Você venceu!!')
        wins = wins + 1
    elif movimentoJogador == 'P' and movimentoComputador == 'R':
        print('Você venceu!!')
        wins = wins + 1
    elif movimentoJogador == 'T' and movimentoComputador == 'P':
        print('Você venceu!!')
        wins = wins + 1
    elif movimentoJogador == 'R' and movimentoComputador == 'P':
        print('Você perdeu!')
        loss = loss + 1
    elif movimentoJogador == 'P' and movimentoComputador == 'T':
        print('Você perdeu!')
        loss = loss + 1
    elif movimentoJogador == 'T' and movimentoComputador == 'R':
        print('Você perdeu!')
        loss = loss + 1
    
