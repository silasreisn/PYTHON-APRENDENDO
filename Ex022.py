#Crie um programa que leia o nome de uma  pessoa e mostre:                                    -> O mome com todas as letras maiúsculas.                                                     -> O nome com todas as letras minúsculas.                                                     -> Quantas letras ao todo (sem considar espaços).                                             -> Quantas letras tem o primeiro nome.

#(strip) serve para cortar os espaços desnecessários no começo e no final da string
nome = str(input('\033[7;30mDigite seu nome completo:\033[m ')).strip()

print('\033[31mAnalizando seu nome...\033[m')

#Aqui  mostrar a frase com todas as letras maiúsculas
print('\033[7;30mNome em maiúsculas:\033[m \033[35m{}\033[m'.format(nome.upper()))

#Aqui  mostrar a frase com todas as letras minúsculas
print('\033[7;30mNome em minúsculas:\033[m \033[35m{}\033[m'.format(nome.lower()))

#len conta todos os caracteres, até os espaços. count conta quantos espaços tem na string
print('Seu nome tem ao todo \033[31m{}\033[m letras'.format(len(nome) - nome.count(' ')))

#find ler a string até encontrar o primeiro espaço
print('Seu primeiro nome tem \033[31m{}\033[m letras'.format(nome.find(' ')))

#Outra opção de fazer o ultimo item do exercício
#split separa a string em várias partes onde houver espaços
separa = nome.split()
print('Seu primeiro nome é \033[31m{}\033[m e ele tem \033[31m{}\033[m letras'.format(separa[0], len(separa[0])))
print(' ')