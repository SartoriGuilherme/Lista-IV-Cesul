x = int(input('Informe um número de 3 dígitos: '))

centenas = x // 100
resto = x % 100

dezenas = resto // 10
decimais = resto % 10
somadosnumeros = centenas + dezenas + decimais

print(f'A soma dos números inteiros resulta em:{somadosnumeros:.1f} ')