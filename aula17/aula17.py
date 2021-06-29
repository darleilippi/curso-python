"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f = Flutuantes (float)
:.(NUMERO)f - Quantidade de casas defimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f) - completar casas

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:.2f}')

nome = "Darlei"
print(f'{nome:.4s}')

print(f'{num_1:0>10d}')  # num_1 tenha 10 casas a esquerda rjust
print(nome.rjust(10, '#'))