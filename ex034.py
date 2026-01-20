#Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou igual, o aumento é de 15%.


sal = float(input('Qual é o salário do funcionário? \033[32mR$\033[m'))
if sal <= 1250:
    nov = sal + (sal * 15 / 100)
else:
    nov = sal + (sal * 10 / 100)
print('Quem ganhava \033[32mR$\033[m\033[31m{:.2f}\033[m passa a ganhar \033[32mR$\033[m\033[31m{:.2f}\033[m agora.'.format(sal, nov))
print(' ')