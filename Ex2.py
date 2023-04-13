TotalPrestacoes = int(input('Informe a quantidade total de prestaçoes a pagar: '))
PrestacoesPagas = int(input('Informe a quantidade de prestações pagas: '))
ValorDaPrestacao = int(input('Informe o valor de cada prestação: '))

TotalPrestacoesPagas = PrestacoesPagas * ValorDaPrestacao
ValorRestante = TotalPrestacoes * ValorDaPrestacao - TotalPrestacoesPagas

print(f'O valor total de prestações pagas pelo devedor é de R$ {TotalPrestacoesPagas:.2f}')
print(f'e o valor total das prestações ainda não pagas é de R$ {ValorRestante:.2f}')

