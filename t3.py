import random

print("Ingrese el valor de a:")
a = float(input())

print("Ingrese el valor de b:")
b = float(input())

print("Ingrese el valor de c:")
c = float(input())

print("Ingrese el valor de d:")
d = float(input())

print("Ingrese la cantidad de puntos:")
cantidad = int(input())

puntos_elipse = 0
puntos_interseccion = 0

pi = 3.1416

for i in range(cantidad):

    x = -a + (2 * a) * random.random()
    y = -b + (2 * b) * random.random()

    if (x**2 / a**2) + (y**2 / b**2) <= 1:

        puntos_elipse = puntos_elipse + 1

        if (x**2 / c**2) - (y**2 / d**2) >= 1:

            puntos_interseccion = puntos_interseccion + 1


area_elipse = pi * a * b

area_interseccion = area_elipse * puntos_interseccion / puntos_elipse


print("Puntos dentro de la elipse:", puntos_elipse)

print("Puntos en la interseccion:", puntos_interseccion)

print("Area de la elipse:", area_elipse)

print("Area aproximada de la interseccion:", area_interseccion)