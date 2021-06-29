try:
    horario = int(input("Informe um horário: "))

    if horario > 0 and horario <= 11:
        print("Bom dia!")
    elif horario > 11 and horario <= 17:
        print("Boa tarde!")
    else:
        print("Boa noite!")
except:
    print("Informe um horário válido!")