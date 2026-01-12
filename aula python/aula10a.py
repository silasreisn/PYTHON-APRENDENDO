#Condições Simples e Compostas 

#Estrutura condiçonal simples 
'''nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {}'.format(nome))'''


#Estrutura condiçonal Composta
'''nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''


#Estrutura Composta
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
'''

#Condições simplificadas 
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')