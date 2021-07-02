# minha resposta
contador_cres = 0
contador_decres = 10

while contador_cres < 9:
    print(contador_cres, contador_decres)
    contador_cres += 1
    contador_decres -= 1


# solução com for e enumerate
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)