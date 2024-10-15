"""Pedirá por teclado una palabra y hemos de decir si es un palíndromo o no.
"""

#DECLARACION DE VARIABLES

palabra="" #CADENA QUE CONTENDRA LA PALABRA A ANALIZAR ( PARA VER SI ES PALINDROMO O NO)
longitud=0 #CONTENDRA EL TAMAÑO DEL TEXTO DE LA PALABRA
indice=0 #INDICE CON EL QUE RECORREMOS LA PALABRA




#PROGRMA PRINCIPAL:


palabra=input("INTRODUCE LA PALABRA PARA VER SI ES PALINDROMO O NO: ")
longitud=len(palabra)
for indice in range(0,longitud):


