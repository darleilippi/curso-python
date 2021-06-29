"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

lista = []
contador = 0

while contador < 5:
    num1 = input('Informe um número: ')

    if num1.isdigit():
        lista.append(int(num1))
        contador += 1
    else:
        print('Informe um número válido!')
else:
    soma = 0
    for n in lista:
        soma += n

    print(f"Soma dos números: {soma}")
    print(f"Menor valor: {min(lista)}")
    print(f"Maior valor: {max(lista)}")