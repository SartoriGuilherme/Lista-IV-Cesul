lado1 = int(input('Informe quantos metros tem um dos lados da casa: '))
lado2 = int(input('Informe quantos metros tem o outro lado da casa: '))

Area = lado1 * lado2
TotalDeWatts = Area * 18

print(f'Serão necessários {TotalDeWatts:.2f} para iluminar a casa corretamente.')
