#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


num = int(input('\033[1;37mDigite um número: \033[m'))
res = num % 2
if res == 0:
    print('O número \033[31m{}\033[m é \033[34mPAR\033[m'.format(num))
else:
    print('O número \033[31m{}\033[m é \033[34mÍMPAR\033[m'.format(num))
    print(' ')