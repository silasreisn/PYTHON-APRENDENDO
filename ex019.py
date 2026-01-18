#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um progrma que ajude ele, lendo o nome deles e escrevendo  o nome do escolhido.

'''
import random
a1 = str (input('Digite o nome do primeiro aluno: '))
a2 = str (input('Digite o nome do segundo aluno: '))
a3 = str (input('Digite o nome do terceiro aluno: '))
a4 = str (input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''

from random import choice
a1 = str (input('Digite o nome do primeiro aluno: '))
a2 = str (input('Digite  o nome do segunto aluno: '))
a3 = str (input('Digite o nome do terceiro aluno: '))
a4 = str (input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('\033[1;31mO aluno escolhido foi\033[m \033[1;41m{}\033[m'.format(escolhido))
print(' ')