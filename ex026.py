#Faça um programa que leia uma frase pelo teclado e mostre:                                   -> Quantas vezes aprarece a letra "A".                                                        -> Em que posição ela aparece a primeira vez.                                                                                           -> Em que posição ela aparece a última vez.

frase = str(input('Digite um frase: ')).upper().strip()
print('\033[31mAnalizando frase.. \033[m')
print('A letra \033[33mA\033[m aparece \033[31m{}\033[m vezes na frase.'.format(frase.count('A')))
print('A primeira letra \033[33mA\033[m parece na posição \033[31m{}\033[m.'.format(frase.find('A')+1))
print('A última letra \033[33mA\033[m apareceu na posição \033[31m{}.\033[m'.format(frase.rfind('A')+1))
print(' ')