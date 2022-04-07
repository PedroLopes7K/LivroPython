#! python3
#pw.py - Um programa para repositório de senhas.

SENHAS = {'email': 'F7MinBBD4756OLJbcd343',
             'facul': 'Hp@2021@',
             'udemy': '12345'}

import sys, pyperclip

'''if len(sys.argv) < 2:
    print('Use: python pw.py [conta] - copia senha da conta')
    sys.exit()
  
conta = sys.argv[1]
conta = input()'''

print('SUAS CONTAS:')
for chave in SENHAS:
    print('----' + chave + '----')
print('Qual senha deseja?')
conta = input()

if conta in SENHAS:
    pyperclip.copy(SENHAS[conta])
    print('Senha para ' +conta+ ' copiada!')
else:
    print('Essa conta não existe ' + conta)
