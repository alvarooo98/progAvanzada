import math



lat1=float(input('ingresa la latitud 1:'))
lon1=float(input('ingresa la longitud 1:'))


lat2=float(input('ingresa la latitud 2:'))
lon2=float(input('ingresa la longitud 2:'))


t1=math.radians (lat1)
t2=math.radians (lat2)

g1=math.radians (lon1)
g2=math.radians (lon2)

distancia= 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

print('la distancia entre los puntos es:', distancia,'km')