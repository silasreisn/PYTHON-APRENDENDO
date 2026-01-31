#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#-À vista dinhero/cheque: 10% de desconto 
#-À vista no cartão: 5% de desconto
#-Em até 2x no cartão: preço normal
#-3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto: R$'))
print('''Escolha a forma de pagamento:
      [ 1 ] À vista dinheiro/cheque
      [ 2 ] À vista no cartão
      [ 3 ] Em até 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opcao = int(input('Sua opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco - ( preco * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 3:
    total = preco
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    total = preco + (preco * 20 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))