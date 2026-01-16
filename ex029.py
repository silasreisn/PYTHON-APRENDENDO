#Escreva um programa que leia a velocidade de um carro. Se ele ultrpassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.


vel = float(input('Digite a velocidade: '))
print('Analizando...')
if vel > 80:
    print('Você foi MULTADO, sua velocidade de {}Km/h, está acima do permitido!'.format(vel))
    mul = (vel - 80) * 7
    print('Você deve pagar umna multa de R${:.2f}!'.format(mul))
else:
    print('Você está na velocidade ideal')
print('Tenha um bom dia! Dirija com segurança!')