"""
CPF = 168.995.350-09
---------------------------------------
1 * 10 = 10     #       1 * 11 = 11
6 * 9 = 54      #       
8 * 8 = 54      #       
9 * 7 = 64      #       
9 * 6 = 54      #       
5 * 5 = 25      #       
3 * 4 = 12      #       
5 * 3 = 15      #       
0 * 2 = 0       #       
"""
#cpf = '168.995.350-09'
"""
cpf = '035.181.000-50'

primeiro_digito, ultimos_digitos = cpf.split('-')
primeiro_digito = primeiro_digito.replace('.', '')

print(primeiro_digito, ultimos_digitos)
print()

soma_primeiros_digitos = 0
for indice, valor in enumerate(range(10, 1, -1)):
    soma_primeiros_digitos += (int(primeiro_digito[indice]) * valor)

digito_1 = 11 - (soma_primeiros_digitos % 11)
if(digito_1 > 9):
    digito_1 = 0

soma_ultimos_digitos = 0
ultimos_digitos = primeiro_digito + str(digito_1)

for indice, valor in enumerate(range(11, 1, -1)):
    soma_ultimos_digitos += (int(ultimos_digitos[indice]) * valor)

digito_2 = 11 - (soma_ultimos_digitos % 11)
if(digito_2 > 11):
    digito_2 = 0

print(digito_1, digito_2)  #ta com erro do digito
"""

# solucao da aula

while True:
    cpf2 = input('Informe um CPF: ')
    novo_cpf2 = cpf2[:-2]  #ultimos 2

    reverso = 10
    total = 0
    for index in range(19):
        if(index > 8):
            index -= 9

        total += int(novo_cpf2[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11

            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf2 += str(d)

    # Evita seguencias
    sequencia = novo_cpf2 == str(novo_cpf2[0]) * len(cpf2)

    if cpf2 == novo_cpf2 and not sequencia:
        print('Válido')
    else:
        print('Inválido')