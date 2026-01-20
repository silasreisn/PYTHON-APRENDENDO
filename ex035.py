#Desenvolva um programa que leia o comprimento de três retas e diga ao úsuario se elas podem ou não formmar um triângulo.


print('\033[31m-\033[m' * 25)
print('\033[1;37mAnalisador de Triângulo\033[m')
print('\033[31m-\033[m' * 25)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mAs retas acima\033[m \033[1;37mPODEM FORMA\033[m \033[34mtriângulo!\033[m')
else:
    print('\033[34mAs retas acima\033[m \033[1;37mNÃO PODEM FORMAR\033[m \033[34mtriângulo!\033[m')
print(' ')