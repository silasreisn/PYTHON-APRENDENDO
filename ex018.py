#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, coseno e tangente desse ângulo.

'''import math
ang = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('o ângulo de {} tem o COSSENO de {:.2f}'.format(ang,cos))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))'''

from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o SENSO    de {:.2f}'.format(ang, seno))
cos = cos(radians(ang))
print('O ângulo de {} tem o ACOSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))