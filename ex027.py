#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primero e o último nome separadamente. Ex: Ana Maria de Souza, primeiro = Ana, último = Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('\033[34mMuito prazer em te conhecer!\033[m')
print('Seu primeiro nome é \033[33m{}\033[m'.format(nome[0]))
print('Seu último nome é \033[33m{}\033[m'.format(nome[len(nome)-1]))
print(' ')