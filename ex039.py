#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''
import datetime
atual = datetime.date.today().year 
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano
adiantado = 18 - idade
atrasado = idade - 18 
if idade < 18:
    print('Você ainda irá se alistar ao serviço militar,', end='')
    print(' faltam {} anos para você se alistar.'.format(adiantado))
elif idade == 18:
    print('Está na hora de você se alistar ao serviço militar.')
else:
    print('Você já passou do tempo de se alistar ao serviço militar,', end='')
    print(' você deveria ter se alistado há {} anos.'.format(atrasado))
'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimnento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade 
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo 
    print('Seu alistamento foi em {}.'.format(ano))
print(' ')