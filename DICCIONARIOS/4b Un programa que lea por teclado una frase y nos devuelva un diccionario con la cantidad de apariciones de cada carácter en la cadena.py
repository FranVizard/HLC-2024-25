"""Un programa que lea por teclado una frase y nos devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
"""
#IMPORTACION DE LIBRERIAS

from os import system

#VARIABLEES

frase="" #contiene la cadena de caracteres a escanear. la tratamos como lista
letra= "" #caracter que extraemos de la lista
dicletras= {} #diccionario que contendra: {"letra": nºde apariciones}


#PROGRAMA PRINCIPAL

system("cls")

frase=input("Teclea la frase a escanear: ")
for letra in frase:
    if letra in dicletras:  #busca en el diccionario la letra
        dicletras[letra] += 1   #si esta, incrementa su valor en uno
    else:
        dicletras[letra] = 1    #si no esta, es la primera vez, y asigna uno al caracter



for letra, numveces in dicletras.items():
    if letra!= " ":
        print(f"La letra {letra} esta {numveces} en la frase")
    else:
        print(f"El espacio esta {numveces}")
