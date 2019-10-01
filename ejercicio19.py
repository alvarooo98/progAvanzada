#EJERCICIO 14  Escriba un programa que determine como un objeto viaja cuando golpea el piso. El usuario insertara la informacion de la altura desde donde el objeto se deja caer,en metros (m), dado que el objeto se deja caer desde el reposo (velocidad inicial v0=0m/s). Asumiendo que la aceleracion debido a la gravead es de 9.81 m/s2 y usando la formula vf= r2 v02+2gd calcule la velocidad final usando velocidad inicial v0, aceleracion g y la distancia d.

import math


V0=float(input('ingresa la velocidad inicial:'))
g=float(input('ingresa la gravedad:'))
d=float(input('ingresa la distancia:'))


Vf=math.sqrt(V0*V0)+math.sqrt(2*g*d)

print('la velocidad final es:', Vf,'m/s')