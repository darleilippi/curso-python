"""
While/Else

break não faz o else executar, somente quando a expressão do while for falsa
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('Else')