#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


'''opo =float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente:'))
hip = (opo**2 + adj**2) ** (1/2)
print('O comprimemnto da hipotenusa é {:.2f}'.format(hip))'''

'''import math
opo = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(opo, adj)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))'''

from math import hypot
opo = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(opo, adj)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))