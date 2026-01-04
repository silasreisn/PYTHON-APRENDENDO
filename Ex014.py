#Escreva um programa que converta uma temperatura digitada °C e converta para °F.#

c = float(input('Informe a tempeatura em °C: '))
f = ((9 * c)/ 5) + 32
print('A temepearatura de {}°C correspnde a {}°F!'.format(c, f))
