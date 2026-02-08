#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Primeir termo: '))
razao = int(input('Razão: '))
decimo = termo + (11 - 1) * razao
for c in range(termo, decimo, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU!')
print('')