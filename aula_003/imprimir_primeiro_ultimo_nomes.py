nome_completo = input('Insira o seu nome: ')
delimitador = " "
nomes = nome_completo.split(delimitador)
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]
print('{} {}'.format(primeiro_nome, ultimo_nome))