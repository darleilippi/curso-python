"""
Repetições
"""
operadores = ['+', '-', '/', '*']
while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input(f'Qual operação {operadores}?: ')

    if not num1.isdigit() or not num2.isdigit():
        print('Informe números válidos!')
        continue

    if not operador in operadores:
        print('Informe um operador válido', operadores)
        continue

    num1 = int(num1)
    num2 = int(num2)

    print()
    if operador == '+':
        print("Resultado:", num1 + num2)
    elif operador == '-':
        print("Resultado:", num1 - num2)
    elif operador == '/':
        print("Resultado:", num1 / num2)
    elif operador == '*':
        print("Resultado:", num1 * num2)

    sair = input("Deseja sair? [s]im ou [n]ão: ")
    if sair == 's':
        break

