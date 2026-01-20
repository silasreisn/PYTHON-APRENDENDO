#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cid = str(input('\033[1;37mDigite o nome de uma cidade: \033[m')).strip()
print('\033[31mAnalisando nome da cidade...\033[m')
print(cid[:5].upper() == 'SANTO')
print(' ')