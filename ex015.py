#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
#custa R$60 por dia e R$0,15 por Km rodado. 

km = float (input('Quantos Km foram percorridos com o carro alugado? '))
dias = int (input('Por quantos dias o carro foi alugado? '))
preco = (0.15 * km) + (60 * dias)
print('O preço total a pagar pelo carro alugado é de R${:.2f}'.format(preco))
