nome = input('Insira seu nome: ')
nomes = nome.split()
inicial_or = nomes[0][0]
inicial = inicial_or.lower()
final_or = nomes[-1][-1]
final = final_or.lower()
count_inicial = 0
count_final = 0
if inicial == "a" or inicial == "e" or inicial == "i" or inicial == "o" or inicial == "u":
    print('Nome inicia com vogal.')
    count_inicial = 1
if final != "a" and final != "e" and final != "i" and final != "o" and final != "u":
    print('Nome termina com consoante.')
    count_final = 1
if count_inicial == 0 and count_final == 0:
    print('Nome neutro.')