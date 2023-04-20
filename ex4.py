alt = float(input('Informe a altura do pacote: '))
larg = float(input('Informe a largura do pacote: '))
comp = float(input('Informe  o comprimento do pacote: '))

total = (4 * alt) + (2 * larg) + (2 * comp) + 20

print(f'O total de barbante a ser usado é {total:.1f}')