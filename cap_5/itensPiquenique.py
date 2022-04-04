
convidados = {
    'Alice': {
        'maça': 5,
        'salgadinhos': 12
        },
    'Pedro': {
        'sanduiches': 3, 
        'maça': 2
        },
    'Carol': {
        'copos': 3, 
        'torta de frango': 1
        }
        }

def totalComidas(convidados, item):
    quantidade = 0
    for k, v in convidados.items():
        quantidade = quantidade + v.get(item, 0)
    return quantidade

print('Number of things being brought:')
print(' - maça ' + str(totalComidas(convidados, ',aça')))
print(' - copos ' + str(totalComidas(convidados, 'copos')))
print(' - salgadinhos ' + str(totalComidas(convidados, 'salgadinhos')))
print(' - sanduiches ' + str(totalComidas(convidados, 'sanduiches')))
print(' - torta de frango ' + str(totalComidas(convidados, 'torta de frango')))
