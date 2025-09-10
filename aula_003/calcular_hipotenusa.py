import math
cateto1 = float(input('Insira o primeiro cateto: '))
cateto2 = float(input('Insira o segundo cateto: '))
hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
print('Hipotenusa = {:.2f}'.format(hipotenusa))