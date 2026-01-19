#Escreva um programa que leia a velocidade de um carro. Se ele ultrpassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.


vel = float(input('Digite a velocidade: '))
print('\033[31mAnalizando...\033[m')
if vel > 80:
    print('Você foi \033[7;37mMULTADO\033[m, sua velocidade de \033[31m{}Km/h\033[m, está acima do permitido!'.format(vel))
    mul = (vel - 80) * 7
    print('Você deve pagar umna multa de \033[31mR${:.2f}\033[m!'.format(mul))
else:
    print('\033[34mVocê está na velocidade ideal\033[m')
print('\033[1;37mTenha um bom dia! Dirija com segurança!\033[m')
print(' ')