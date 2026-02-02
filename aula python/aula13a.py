#Laços e Repetição

#Contara até 6
'''for c in range(1, 7):
    print(c)
print('FIM')'''

#Contara de trás pra frente 
'''for c in range(0, 7, -1):
    print(c)
print('FIM')'''

#Contara de 2 em 2 
'''for c in range(0, 7, 2):
    print(c)
print('FIM')'''

#Exemplo lendo um número
'''n = int(input('Digite um número: '))'
for c in range(0, n+1):
    print(c)
print('FIM')'''

#Exemplo lendo início, meio e fim
'''i = int(input('Início: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

#Exemplo do input dentro do for
'''for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')'''

#Exemplo de um somatorio usando for
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))