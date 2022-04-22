# jogo da vida
import random, time, copy
WIDTH = 60
HEIGHT = 20


#criando uma lista de listas para as celulas
proximasCelulas = []
for x in range(WIDTH):
    coluna = [] # cria uma nova coluna
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            coluna.append('#') # adiciona uma celula viva
        else:
            coluna.append(' ') # adiciona uma celula morta
    proximasCelulas.append(coluna) # 'proximasCelulas e uma lista de listas de colunas'
while True:  # loop do programa principal
    print('\n\n\n\n\n') #Separar cada passo com novas linhas
    celulasAtuais = copy.deepcopy(proximasCelulas)

    #imprimir as celulas atuais
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(celulasAtuais[x][y], end='') # imprimir # ou ' '
        print() # imprimir uma nova linha no final da fila

    #Calcular as células do passo seguinte com base nas células do passo atual
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Obter coordenadas vizinhas
            # `% WIDTH`assegura que o cordenada esquerda está sempre entre 0 e LARGURA - 1
            cordenadaEsquerda = (x - 1) % WIDTH
            cordenadaDireita = (x + 1) % WIDTH
            cordenadaAcima = (y - 1) % HEIGHT
            cordenadaAbaixo = (y + 1) % HEIGHT

            #Contar o número de vizinhos vivos:
            numVizinhos = 0
            if celulasAtuais[cordenadaEsquerda][cordenadaAcima] == '#':
                numVizinhos += 1 # O vizinho de cima-esquerda está vivo
            if celulasAtuais[x][cordenadaAcima] == '#':
                numVizinhos += 1 # O vizinho de cima está vivo
            if celulasAtuais[cordenadaDireita][cordenadaAcima] == '#':
                numVizinhos += 1 # O vizinho de cima-direita está vivo
            if celulasAtuais[cordenadaEsquerda][y] == '#':
                numVizinhos += 1 # O vizinho da esquerda está vivo
            if celulasAtuais[cordenadaDireita][y] == '#':
                numVizinhos += 1 # O vizinho da direita está vivo
            if celulasAtuais[cordenadaEsquerda][cordenadaAbaixo] == '#':
                numVizinhos += 1 # O vizinho de baixo-esquerda está vivo
            if celulasAtuais[x][cordenadaAbaixo] == '#':
                numVizinhos += 1 # O vizinho de baixo está vivo
            if celulasAtuais[cordenadaDireita][cordenadaAbaixo] == '#':
                numVizinhos += 1 # O vizinho de baixo-direita está vivo

         #   Definir célula com base nas regras do Jogo da Vida da Conway
            if celulasAtuais[x][y] == '#' and (numVizinhos == 2 or numVizinhos == 3):
                # As células vivas com 2 ou 3 vizinhos permanecem vivas
                proximasCelulas[x][y] = '#'
            elif celulasAtuais[x][y] == ' ' and numVizinhos == 3:
                #Células mortas com 3 vizinhos tornam-se vivas
                proximasCelulas[x][y] = '#'
            else:
                #Tudo o resto morre ou permanece morto
                proximasCelulas[x][y] = ' '
    time.sleep(1) #Acrescentar uma pausa de 1 segundo para reduzir a cintilação(tremulação)
                

                
            
    
    
    
