# Ejercicio 10
# cree un programa que lea dos valores a Y b, introducidos. su programa de calcular y mostrar:
# • La suma de a y b
# • La diferencia cuando a es sustraido de b
# • El producto de a y b
# • El cociente cuando a divide a b
# • El resto cuando a divide a b
# • El resultado de log a
# • El resultado de a a la potencia de b

from math import log
a = int(input('insete el valor de a: '))

b = int(input('insete el valor de b: '))
print('')
print(a, '+', b, 'es:                  ', a+b)
print('')
print(a, '-', b, 'es:                  ', a-b)
print('')
print(a, '*', b, 'es:                  ', a*b)
print('')
print(a, '/', b, 'es:                  ', a/b)
print('')
print(a, '%', b, 'es:                  ', a%b)
print('')
print('El logaritmo para', a, 'es:     %.2f' % log(a))
print('')
print(a, '^', b, 'es:                  ', a**b)