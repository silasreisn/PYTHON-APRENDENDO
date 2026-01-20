#Desenvolva um programa que pergunte a disntância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$o,45 para viagens mais longas.


'''dis = float(input('Qual a distância da sua viagem? '))
cob = dis * 0.50
if dis <= 200:
    print('Sua viagem de até {}km, vai custar R${:.2f}!'.format(dis,cob))
else:
    cob = dis * 0.45
    print('Sua viagem de até {}km, vai custar R${:.2f}!'.format(dis,cob))'''


dis = float(input('\033[1;37mQual é a distância da sua viagem? \033[m'))
print('Você está preste a começar uma viagem de \033[31m{}km\033[m.'.format(dis))
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print('E o preço da sua passagem será de \033[31mR${:.2f}\033[m.'.format(preço))
print(' ')