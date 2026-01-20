#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.


from datetime import date 
ano = int(input('Que ano quer analizar? Coloque \033[31m0\033[m para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;37m{}\033[m é \033[34mBISSEXTO\033[m'.format(ano))
else:
    print('O ano \033[1;37m{}\033[m Não é \033[34mBISSEXTO\033[m'.format(ano))
print(' ')
