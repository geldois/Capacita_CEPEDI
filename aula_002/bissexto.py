ano = int(input("Digite um ano: "))
while ano:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
        ano = int(input("Digite um ano: "))
    else:
        print(f"O ano {ano} não é bissexto.")
        ano = int(input("Digite um ano: "))