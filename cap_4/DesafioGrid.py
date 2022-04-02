# charaterPictureGrid.py

grid = [['.','.','.','.','.','.'],
        ['.','O','O','.','.','.'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','O','.'],
        ['.','O','O','O','O','O'],
        ['O','O','O','O','O','.'],
        ['O','O','O','O','.','.'],
        ['.','O','O','.','.','.'],
        ['.','.','.','.','.','.']]

for coluna in range(len(grid[0])): # executa 6 vezes
  for linha in range(len(grid)): #executa 9 vezes
    # [linha] [coluna]
    print(grid[linha][coluna], end = '') # end evita a quebra de linha
  print('') # usamos apenas para pular a linha
 # print(grid[j][-1])  
