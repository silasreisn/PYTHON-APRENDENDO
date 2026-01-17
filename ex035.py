#Desenvolva um programa que leia o comprimento de três retas e diga ao úsuario se elas podem ou não formmar um triângulo.


print('-' * 25)
print('Analisador de Triângulo')
print('-' * 25)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As  retas acima PODEM FORMA triângulo!')
else:
    print('As retas acima NÃO PODEM FORMAR triângulo')
print(' ' * 25)