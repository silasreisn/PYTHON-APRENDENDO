#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espoços.

# strips() - remove os espaços do início e do fim da string
# upper()  - converte a string para maiúscula
# split()  - divide a string em uma lista, usando os espaços como separadores
# join()   - junta os elementos de uma lista em uma string, usando um separador (no caso, uma string vazia)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palídromo!')
print('')



# Codigo sem o for, usando macete de fatiamento de string
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palídromo!')
print('')'''