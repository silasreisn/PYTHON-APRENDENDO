#Crie um programa que leia o nome de uma  pessoa e mostre:                                    -> O mome com todas as letras maiúsculas.                                                     -> O nome com todas as letras minúsculas.                                                     -> Quantas letras ao todo (sem considar espaços).                                             -> Quantas letras tem o primeiro nome.

'''(strip) serve para cortar os espaços desnecessários no começo e no final da string'''
nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome...')

'''Aqui  mostrar a frase com todas as letras maiúsculas'''
print('Nome em maiúsculas: {}'.format(nome.upper()))

'''Aqui  mostrar a frase com todas as letras minúsculas'''
print('Nome em minúsculas: {}'.format(nome.lower()))

'''len conta todos os caracteres, até os espaços. count conta quantos espaços tem na string'''
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

'''find ler a string até encontrar o primeiro espaço'''
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

'''Outra opção de fazer o ultimo item do exercício'''
'''split separa a string em várias partes onde houver espaços '''
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))