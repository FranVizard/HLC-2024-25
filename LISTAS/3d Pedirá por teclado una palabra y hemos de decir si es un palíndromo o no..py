"""Pedirá por teclado una palabra y hemos de decir si es un palíndromo o no.
"""

#DECLARACION DE VARIABLES

palabra="" #CADENA QUE CONTENDRA LA PALABRA A ANALIZAR ( PARA VER SI ES PALINDROMO O NO)
longitud=0 #CONTENDRA EL TAMAÑO DEL TEXTO DE LA PALABRA
indice=0 #INDICE CON EL QUE RECORREMOS LA PALABRA
palindromo=True #INDICA SI LA PALABRA ES PALINDRMO O NO



#PROGRMA PRINCIPAL:

palabra=input("INTRODUCE LA PALABRA PARA VER SI ES PALINDROMO O NO: ")
longitud=len(palabra) -1 #LE RESTO UNO PORQUE LA LISTA FORMADA POR LA PALABRA COMIENZA EN 0

while indice < longitud - indice and palindromo==True:
    if palabra[indice] != palabra[longitud - indice]:
        palindromo=False

    indice+=1

if palindromo==True:
    print(f"LA PALABRA {palabra} ES UN PALINDROMO")
else:
    print(f"LA PALABRA {palabra} NO ES UN PALINDROMO")
