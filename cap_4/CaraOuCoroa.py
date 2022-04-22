'''
Para este exercício, vamos tentar fazer uma experiência. Se atirar uma moeda ao ar 100 vezes
e escreva um "H" para cada cabeça e um "T" para cada cauda, irá criar
uma lista que se parece com "T T T T H H H H T T". Se pedir a um humano para fazer
mais de 100 moedas ao acaso, provavelmente acabará com cauda de cabeça alternada 
resultados como "H T H T H H T H T T", que parece aleatório (para os humanos),
mas não é matematicamente aleatório. Um humano quase nunca anotará
uma sequência de seis cabeças ou seis caudas seguidas, embora seja altamente provável
para acontecer em verdadeiros lançamentos aleatórios de moedas. Os seres humanos são previsivelmente maus em
ser aleatório.
Escrever um programa para descobrir com que frequência uma sequência de seis cabeças ou uma sequência
de seis caudas vem numa lista gerada aleatoriamente de cabeças e caudas. O seu
programa decompõe a experiência em duas partes: a primeira parte gera
uma lista de valores de 'cabeças' e 'caudas' seleccionados aleatoriamente, e a segunda parte
verifica se há uma raia nela. Colocar todo este código num laço que repete
a experiência 10.000 vezes para que possamos descobrir qual a percentagem da moeda
As voltas contêm uma sequência de seis cabeças ou caudas em fila. Como dica, a função
a chamada random.randint(0, 1) devolverá um valor 0 50% do tempo e um valor 1
os outros 50% do tempo.


'''
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    resultList = []
    for i in range(100):
        result = random.randint(0,1)
        resultList.append(result)

    counterzero = 0
    counterone = 0
    for res in resultList:
        if res == 0:
            counterzero+=1
            counterone=0
        elif res == 1:
            counterzero=0
            counterone+=1

        if counterzero == 6 or counterone == 6:
            counterzero = 0
            counterone = 0
            numberOfStreaks+=1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
