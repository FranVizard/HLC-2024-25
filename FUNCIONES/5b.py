"""Una función que nos devuelva el módulo de un vector de 3 dimensiones.
"""

# Importación de librerías:

from os import system

#declaracion de variables
xCoord=0
yCoord=0
zCoord=0
modulo=0
#definicion de funciones
"""devuelve el modulo del ector de 3 dimensiones.
formato: modulo3D(coordX,coordY,coordZ)"""
def modulo3D(coordX, coordY, coordZ):
    resultado= (xCoord**2+yCoord**2+zCoord**2)**0.5
    return resultado


#progrma principal

system("cls")

xCoord=float(input("introduce coordenada x: "))
yCoord=float(input("introduce coordenada y: "))
zCoord=float(input("introduce coordenada z: "))

modulo=modulo3D(xCoord, yCoord, zCoord)
print(f"el modulo del vector ({xCoord}, {yCoord}, {zCoord}) es {modulo}.")