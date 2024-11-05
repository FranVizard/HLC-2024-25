"""Una función que nos devuelva True si un valor parámetro está dentro de un rango, que también introduciremos como parámetros. Si no es así, devolverá False."""


# Importación de librerías:

from os import system


#DECLARACION DE VARIABLES

valor=0
liminferior=0
limsuperior=0

#DEFINICION DE FUNCIONES
def rango(valor, liminferior, limsuperior):
    if valor >= liminferior and valor <= limsuperior:
        return True
    else:
        return False
#PROGRAMA PRINCIPAL
system("cls")

valor = input("numero a comprobar: ")
liminferior = input("teclea el extremo inferior del intervalo: ")
limsuperior = input("teclea el extremo superior del intervalo: ")


if rango(valor, liminferior, limsuperior):
    print("esta dentro del intervalo")
else:
    print("no esta dentro del intervalo")

