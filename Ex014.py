#Escreva um programa que converta uma temperatura digitada °C e converta para °F.#

c = float(input('Informe a tempeatura em °C: '))
f = ((9 * c)/ 5) + 32
print('A temepearatura de \033[32m{}°C\033[m correspnde a \033[34m{}°F\033[m!'.format(c, f))
print(' ')
