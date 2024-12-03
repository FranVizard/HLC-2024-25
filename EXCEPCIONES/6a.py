"""Añadir un producto: Ingresar el nombre del producto, el precio y la cantidad en stock.
Buscar un producto: Ingresar el nombre de un producto y mostrar su precio y cantidad en stock.
Actualizar la cantidad de un producto: Ingresar el nombre de un producto y cambiar la cantidad en stock.
Eliminar un producto: Ingresar el nombre de un producto y eliminarlo del inventario.
Listar todos los productos: Mostrar todos los productos en el inventario con su precio y cantidad.
Salir del programa.
"""

# Importación de librerías:
from os import system

# Declaración de variables:
inventario = {} # Diccionario que contendrá toda la estructura.

# Definición de funciones:

def agregarProducto():
    nombre = input("¿Qué producto quieres añadir al inventario? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        print(f"El producto '{nombre}' ya está dentro del inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        try:
            precio = float(input("Precio del artículo: "))
            cantidad = int(input("Cantidad de artículos: "))
        except ValueError:
            print(f"Error: Alguno de los dos valores no es un valor numerico. Articulo {nombre} no añadido.")
        else:
           inventario[nombre] = {"precio": precio, "cantidad": cantidad}
           print(f"El producto '{nombre}' ha sido añadido a la lista.")           
        
        print("")
        input("Pulsa una tecla para continuar...")


def listadoProductos():
    print("Listado de los elementos...")
    for nombre, valor in inventario.items(): # Recorro todo el diccionario principal.
        print(f"Producto: {nombre}, Precio: {valor["precio"]}, Cantidad: {valor["cantidad"]}.")

    print("")
    input("Pulsa una tecla para continuar...")     


def actualizarCantidad():
    nombre = input("¿De qué producto quieres modificar el stock? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        cantidad = int(input("Introduce la nueva cantidad en stock: "))
        inventario[nombre]["cantidad"] = cantidad
        print(f"El producto '{nombre}' ha actualizado correctamente su stock a {cantidad} unidades.")
        print("")
        input("Pulsa una tecla para continuar...")

def buscarProducto():
    nombre = input("Qué producto quieres buscar en el stock? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        print(f"El producto '{nombre}' tiene un stock de {inventario[nombre]["cantidad"]} unidades, y {inventario[nombre]["precio"]} €.")
        print("")
        input("Pulsa una tecla para continuar...")


def eliminarProducto():
    nombre = input("Qué producto quieres eliminar en el stock? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        del inventario[nombre]
        print(f"El producto se ha eliminado del inventario.")        
        print("")
        input("Pulsa una tecla para continuar...")


def menu():
    opcion = 0
    while opcion != 6:
        system("cls")
        print("") # Salto de línea para dejar una línea en blanco.
        print("***************   MENÚ PRINCIPAL  ****************")
        print("1.- Agregar un producto al inventario.")
        print("2.- Buscar un producto en el inventario.")
        print("3.- Actualizar la cantidad de un producto del inventario.")
        print("4.- Eliminar un producto al inventario.")
        print("5.- Mostar todos los productos del inventario.")
        print("6.- Salir del programa")
        print("")
        opcion = int(input("Elige la opción correspondiente... "))

        if opcion == 1: # Agregar un producto al inventario.
            agregarProducto()

        elif opcion == 2: # Buscar un producto en el inventario..
           buscarProducto()
        
        elif opcion == 3: #  Actualizar la cantidad de un producto del inventario.
            actualizarCantidad()

        elif opcion == 4: #  Eliminar un producto al inventario.
            eliminarProducto()

        elif opcion == 5: #  Mostar todos los productos del inventario..
            listadoProductos()





# Programa principal:

menu()