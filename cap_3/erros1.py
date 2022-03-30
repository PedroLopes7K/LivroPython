def spam(divisor):
    try:  
        return 42 / divisor
    except ZeroDivisionError:  # tratando possiveis erros
        print('Error, argumento invalido')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
