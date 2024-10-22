"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total.
"""
#IMPORTACION DE LIBRERIAS

from os import system

#VARIABLEES

nombrearticulo = " " #contiene el nombre del articulo a comprar
precioarticulo = "" #precio del articulo (se pide por teclado)
dicarticulos={} #diccionario
sumacompra=0
#PROGRAMA PRINCIPAL

system("cls")

while(nombrearticulo != ""):
    nombrearticulo=input("Introduce el nombre del articulo a añadir a la cesta de la compra (enter para finalizar)")
    if nombrearticulo !="": 
        precioarticulo=float(input("Teclea su recio: "))
        dicarticulos[nombrearticulo] = precioarticulo
    print("")


for nombrearticulo, precioarticulo in dicarticulos.items():
    print(f"Artiuclo: {nombrearticulo}, precio {precioarticulo}")
    sumacompra += precioarticulo # equivale a sumaCompra

print (f"El importe total de la compra es {sumacompra}.")


