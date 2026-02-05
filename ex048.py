#Façâ um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for s in range(1, 501, 2):
    if s % 3 == 0:
        soma = soma + s
        cont += 1
print('A soma de todos os {} valores solicitados são {}'.format(cont, soma))
print(' ')