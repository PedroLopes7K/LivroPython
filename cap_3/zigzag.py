import time, sys
espacos = 0 # quantos espaços de identação
espacosAumentando = True # se a identação vai aumentar ou não


try:
    while True: # Loop do programa principal
        print(' ' * espacos, end='')
        print('********')
        time.sleep(0.1)  #pausa de 1/10(um decimo de segundo)
        # sem essa pausa os * seriam impressos muito rapido

        if espacosAumentando:
            # Aumenta o numero de espaços quando 'espacosAumentando' e Trur
            espacos = espacos + 1
            # Muda de direção alterando 'espacosAumentando' para False e diminuindo os espaços
            if espacos == 20:
                espacosAumentando = False
        else:
            # se 'espacosAumentando' for False, diminui o numero de espaços
            espacos = espacos -1
            if espacos == 0:
                # Muda de direção alterando 'espacosAumentando' para True e aumentando os espaços
                espacosAumentando = True
except KeyboardInterrupt:
    sys.exit()
