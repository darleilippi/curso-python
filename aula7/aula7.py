"""
Formatação de Strings = f

Arredondamento = .2f - duas casas

"""

nome = 'Darlei'
idade = 26
altura = 1.76
e_maior = idade > 18
peso = 87.6
imc = (peso / (altura ** 2))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))