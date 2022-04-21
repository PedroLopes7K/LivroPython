# exercicio Collatz

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

#print(collatz(16))

def getNum():
    try:
      print('Insira um Numero:')
      numero = int(input())
      resultado = collatz(numero)
      while resultado != 1:
             print(str(resultado))
             numero = int(input())
             resultado = collatz(numero)
             if resultado == 1:
                print(str(resultado))
                print('Programa encerrad0!')
                break
    except ValueError:
        print('Tipo de entrada invalida')
    

getNum()

        
