#A confederação Nascional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#Até 9 anos: MIRIM        Até 25 anos: SÊNIOR   
#Até 14 anos: INFANTIL    Acima: MASTER
#Até 19 anos: JÚNIOR 

from datetime import date
ano = int(input('Digite o ano de nascimento: '))
print('\033[31mANALIZANDO...\033[m')
idade = date.today().year - ano
if idade <= 9:
    print('Com a idade de {} anos, sua categoria é MIRIN.'.format(idade))
elif idade <= 14:
    print('Com a idade de {} anos, sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('Com a idade de {} anos, sua categoria é JÚNIOR.'.format(idade))
elif idade <= 25:
    print('Com a idade de {} anos, sua categoria é SÊNIOR.'.format(idade))
elif idade > 25:
    print('Com a idade de {} anos, sua categoria é MASTER.'.format(idade))
print(' ')