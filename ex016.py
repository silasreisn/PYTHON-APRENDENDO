#Crie um progrma que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

#Ex: Digite um número: 6.127
#O número 6.127 tem a parte Inteira 6.


'''real = float(input('Digite um número Real qualquer: '))
print('A porção interia do número {} é {}'.format(real, int(real)))'''

'''import math
real = float(input('Digite um número Real qualqer: '))
print('A porção interia do número {} é {}'.format(real, math.trunc(real)))'''

from math import trunc
real = float(input('Digite um número Real qualquer: '))
print('A porção interira do número {} é {}'.format(real, trunc(real)))
