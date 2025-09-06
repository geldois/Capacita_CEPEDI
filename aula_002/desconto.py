preco = float(input("Digite o preço do produto: "))
while preco:
    if preco <= 0:
        print("Digite um preço racional > 0!")
        preco = float(input("Digite o preço do produto: "))
    if preco <= 1000:
        novo_preco = preco - (preco * 5 / 100)
        print(f"5% de desconto! Novo preço = {novo_preco}!")
        preco = float(input("Digite o preço do produto: "))
    else:
        novo_preco = preco - (preco * 10 / 100)
        print(f"10% de desconto! Novo preço = {novo_preco}")
        preco = float(input("Digite o preço do produto: "))