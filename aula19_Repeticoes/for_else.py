"""
For/Else
Executa o else ao dar break ou se ele completar o loop
"""

lista = ['Darlei', 'André', 'Lippi']

for valor in lista:
    if valor.startswith('J'):
        break
else:
    print('Não existe nenhuma palavra iniciada em J!')