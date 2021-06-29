"""
Input: Entrada de dados
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2021 - int(idade)

print(f'{nome} tem {idade} anos. Nasceu em {ano_nascimento}.')