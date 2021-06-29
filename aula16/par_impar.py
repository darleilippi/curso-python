try:
    numero = int(input("Informe um número: "))
    e_par = numero % 2 == 0

    if e_par:
        print(f'{numero} é Par!')
    else:
        print(f'{numero} é Ímpar!')
except:
    print("Informe um inteiro válido!")
