nome = input("Informe seu primeiro nome: ")
len_nome = len(nome)
if len_nome <= 4:
    print("Seu nome é curto")
elif len_nome > 4 and len_nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
