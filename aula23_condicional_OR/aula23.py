"""
Condicional OR
 * Para na primeira expressão válida
"""

nome = input('Qual o seu nome?')

print(nome or 'Você não digitou nada!')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Darlei'

valida = a or b or c or d or e or f or g
print(valida)