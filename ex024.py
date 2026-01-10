#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cid = str(input('Digite o nome de uma cidade: ')).strip()
print('Alaizando nome da cidade...')
print(cid[:5].upper() == 'SANTO')
