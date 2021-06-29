"""
    Tipos de Dados

    str - string
    int - inteiro
    float - flutuante
    bool - Boleano ou lógico: True/False
"""

print('Darlei', type('Darlei'))
print(123, type(123))
print(123.45, type(123.45))
print(True, type(True))

"""
    Type cast
"""
print('Darlei', type('Darlei'), bool('Darlei'))
print('10', type(int('10')))
print('10.5', float('10.5'))

# Atividade
print('Nome: Darlei André Lippi', type('Darlei André Lippi'))
print('Idade: 26', type(26))
print('Altura: 1.76', type(1.76))
print('Maior de idade: ', 26 > 18)