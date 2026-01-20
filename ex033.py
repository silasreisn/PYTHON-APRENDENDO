#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('\033[32m-\033[m' * 30)
#Verificando quem é menor 
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior 
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[1;37mO menor valor digitado foi\033[m \033[31m{}\033[m'.format(menor))
print('\033[1;37mO maior valor digitado foi\033[m \033[31m{}\033[m'.format(maior))
print(' ')