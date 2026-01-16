#Desenvolva um programa que pergunte a disntância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$o,45 para viagens mais longas.


'''dis = float(input('Qual a distância da sua viagem? '))
cob = dis * 0.50
if dis <= 200:
    print('Sua viagem de até {}km, vai custar R${:.2f}!'.format(dis,cob))
else:
    cob = dis * 0.45
    print('Sua viagem de até {}km, vai custar R${:.2f}!'.format(dis,cob))'''


dis = float(input('Qual é a distância da sua viagem? '))
print('Você está preste a começar uma viagem de {}km.'.format(dis))
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))