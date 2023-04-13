ValorDoProduto = int(input('Informe o valor do produto a ser pago: '))
ValorDado = int(input('Informe o valor que o cliente está fornecendo: '))

Troco = ValorDado - ValorDoProduto
if Troco > 0:
    print(f'O valor do troco é {Troco:.2f}')
else:
    TrocoFinal = Troco * -1
    print(f'O cliente ainda deve R${TrocoFinal:.2f}')

NdeCelulasCem = int(Troco / 100)
print(f'Células de 100 reais: {NdeCelulasCem:.0f}')

resto = Troco - NdeCelulasCem * 100
NdeCelulasDez = int(resto / 10)

print(f'Células de 10 reais: {NdeCelulasDez:.0f}')

resto1 = resto - NdeCelulasDez * 10
NdeCelulasUm = int(resto1) / 1
print(f'Células de 1 real: {NdeCelulasUm:.0f}')

