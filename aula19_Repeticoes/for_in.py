"""
For in em Python
Função range(start=0, stop, step=1)
"""
texto = "Estudando Python"

for n, letra in enumerate(texto):
    print(n, letra)

print('----')

for n in range(0, 10, 3):
    print(n)

print('----')

for n in range(20, 10, -1):
    print(n)