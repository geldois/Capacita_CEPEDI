idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Não pode votar.")
elif idade < 18 or idade > 69:
    print("Voto facultativo.")
else:
    print("Voto obrigatório.")