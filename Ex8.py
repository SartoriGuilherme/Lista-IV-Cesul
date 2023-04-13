ClientesIsentos = int(input('Informe o número de clientes isentos de pendências: '))
ClientesEmDia = int(input('Informe o número de clientes com as parcelas em dia: '))
CLientesEmAtraso = int(input('Informe o número de clientes com parcelas em atraso: '))

TotalDeClientes = ClientesEmDia + ClientesIsentos + CLientesEmAtraso
PorcentagemIsentos = (ClientesIsentos / TotalDeClientes) * 100
PorcentagemEmDia = (ClientesEmDia / TotalDeClientes) * 100
PorcentagemEmAtraso = (CLientesEmAtraso / TotalDeClientes) * 100

print(f'Porcentagem de clientes isentos é de {PorcentagemIsentos:.0f}%')
print(f'Porcentagem de clientes com as parcelas em dia é de {PorcentagemEmDia:.0f}%')
print(f'Porcentagem de clientes com as parcelas em atraso é de {PorcentagemEmAtraso:.0f}%')