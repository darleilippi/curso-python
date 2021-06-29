"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
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
print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc)