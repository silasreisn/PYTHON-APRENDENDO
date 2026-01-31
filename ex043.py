#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tebela abaixo:
#- Abaixo de 18.5: Abaixo do Peso      - 30 até 40: Obesidade
#- Entre 18.5 e 25: Peso ideal         - Acima de 40: Obesidade mórbida
#- 25 até 30: Sobrepeso 

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Com o peso de {:.2f}kg e altura de {:.2f}m'.format(peso, altura))
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL!') 
elif imc >= 25 and imc < 30:
    print('SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')
print(' ')