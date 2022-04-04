tabuleiro = {'top-L': '','top-M': '', 'top-R': '',
             'mid-L': '', 'mid-M': '', 'mid-R': '',
             'low-L': '', 'low-M': '', 'low-R': ''}

def exibeTabuleiro(tabu):
    print(tabu['top-L'] + '|' + tabu['top-M'] + '|' + tabu['top-R'])
    print('-+-+-')
    print(tabu['mid-L'] + '|' + tabu['mid-M'] + '|' + tabu['mid-R'])
    print('-+-+-')
    print(tabu['low-L'] + '|' + tabu['low-M'] + '|' + tabu['low-R'])
turn = 'X'
for i in range(9):
    exibeTabuleiro(tabuleiro)
    print('Rodada de ' +turn+ ', Mover para qual posicao?')
    move = input()
    tabuleiro[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
   
exibeTabuleiro(tabuleiro)
