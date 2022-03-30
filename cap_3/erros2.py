def spam(divisor):
    return 42 /divisor

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error,argumento invalido')
    
