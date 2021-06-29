"""
For/Else
Somente irá executar o else ao dar break no loop
"""

lista = ['Darlei', 'André', 'Lippi']

for valor in lista:
    if valor.startswith('J'):
        break
else:
    print('Não existe nenhuma palavra iniciada em J!')