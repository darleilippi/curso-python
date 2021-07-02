"""
Split, Join, Enumerate em Python
* Slipt - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista #iteráveis (listas e strings)
* Desempacotamento de listas
"""

string = "O Brasil é o pais do futebol, o Brasil é penta"
lista = string.split(' ')
print(lista)
string2 = ' '.join(lista)
print(string2)
for indice, valor in enumerate(lista):
    print(indice, valor)

lista2 = ['Darlei', 'Andre', 'Lippi', 'o resto da lista', 1, 2, 3, 4]

# *_ - significa, por convenção, que não serão utilizados os outros valores restantes
darlei, andre, lippi, *_, penultido_da_lista, ultimo_da_lista = lista2
print(darlei, andre, lippi)
print(penultido_da_lista, ultimo_da_lista)