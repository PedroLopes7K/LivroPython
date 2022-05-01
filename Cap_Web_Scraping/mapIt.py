import webbrowser

print('digite um endereço: ')
endereco = input()

webbrowser.open('https://www.google.com/maps/place/' + endereco)
