#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('\033[1;37mDigite seu nome: \033[m')).strip()
print('\033[31mAlnalizando seu nome...\033[m')
print('\033[32mSeu nome tem Silva?\033[m \033[1;37m{}\033[m'.format('silva' in nome.lower()))
print(' ')