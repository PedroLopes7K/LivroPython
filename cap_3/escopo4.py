def spam():
    print(eggs) # erro, variavel sendo usanda ntes da atribuição
    eggs = 'spam local'

eggs = 'global'
spam()
