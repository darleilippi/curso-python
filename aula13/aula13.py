"""
len - Quantidade de caracteres
"""

usuario = input("Digite o seu usuário: ")

qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Informe um usuário com pelo menos 6 caracteres!')
else:
    print('Você foi registrado')