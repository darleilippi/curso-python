"""
Funcoes - def em Python
"""

def funcao():
    print('Hello World!')

def porcentagem(value, percent):
    return ((value * percent) / 100) + value

print(porcentagem(50, 10))

def fizz_buzz(numero):
    div_5 = (numero % 5) == 0
    div_3 = (numero % 3) == 0

    if div_5 and div_3:
        return 'FizzBuzz'
    if div_3:
        return 'fizz'
    if div_5:
        return 'buzz'
    
    return numero

print(fizz_buzz(15))