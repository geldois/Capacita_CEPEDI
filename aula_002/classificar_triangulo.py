angulo1 = float(input("Digite o ângulo 1: "))
angulo2 = float(input("Digite o ângulo 2: "))
angulo3 = float(input("Digite o ângulo 3: "))
while angulo1:
    if angulo1 <= 0 or angulo2 <= 0 or angulo3 <= 0:
        print("Digite ângulos racionais > 0.")
        angulo1 = float(input("Digite o ângulo 1: "))
        angulo2 = float(input("Digite o ângulo 2: "))
        angulo3 = float(input("Digite o ângulo 3: "))

    if angulo1 == angulo2 == angulo3:
        print("Triângulo equilátero.")
        angulo1 = float(input("Digite o ângulo 1: "))
        angulo2 = float(input("Digite o ângulo 2: "))
        angulo3 = float(input("Digite o ângulo 3: "))
    elif angulo1 == angulo2 or angulo1 == angulo3 or angulo2 == angulo3:
        print("Triângulo isósceles.")
        angulo1 = float(input("Digite o ângulo 1: "))
        angulo2 = float(input("Digite o ângulo 2: "))
        angulo3 = float(input("Digite o ângulo 3: "))
    else:
        print("Triângulo escaleno.")
        angulo1 = float(input("Digite o ângulo 1: "))
        angulo2 = float(input("Digite o ângulo 2: "))
        angulo3 = float(input("Digite o ângulo 3: "))