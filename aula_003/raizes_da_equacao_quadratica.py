import math, sys
a = int(input("Insira o a: "))
if a == 0:
    print('Não é uma função quadrática, pois a == 0.')
    sys.exit()
b = int(input("Insira o b: "))
c = int(input("Insira o c: "))
delta = (b**2) - (4*a*c)
raiz1 = round((-b + math.sqrt(delta)) / (2*a), 2)
raiz2 = round((-b - math.sqrt(delta)) / (2*a), 2)
if delta == 0:
    print("Duas raízes reais e iguais: {} & {}".format(raiz1, raiz2))
elif delta > 0:
    print("Duas raízes reais e diferentes: {} & {}".format(raiz1, raiz2))
elif delta < 0:
    print("Duas raízes imaginárias.")