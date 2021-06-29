"""
* Criar variáveis para nome (str), idade (str),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings
"""

nome = "Darlei"
idade = 26
altura = 1.76
peso = 87.6
ano_atual = 2021
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e peso {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}')