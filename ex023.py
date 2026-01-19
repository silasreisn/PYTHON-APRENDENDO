#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite  um número: 1834                                                                                                                                                                   unidade:4                                                                                       dezena: 3                                                                                       centena: 8                                                                                      milhar: 1

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('\033[34mAnalizando o número\033[m \033[7;34m{}\033[m'.format(num))
print('\033[1;37mUnidade:\033[m \033[7;34m{}\033[m'.format(u))
print('\033[1;37mDezena:\033[m \033[7;34m{}\033[m'.format(d))
print('\033[1;37mCentena:\033[m \033[7;34m{}\033[m'.format(c))
print('\033[1;37mMilhar:\033[m \033[7;34m{}\033[m'.format(m))
print(' ')