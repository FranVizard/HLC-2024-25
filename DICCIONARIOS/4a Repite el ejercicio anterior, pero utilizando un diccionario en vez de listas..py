"""Repite el ejercicio anterior(3e), pero utilizando un diccionario en vez de listas."""
#IMPORTACION DE LIBRERIAS

from os import system

#VARIABLEES

asignatura=" " #CONTENDRA EL NOMBRE DE LA ASIGNATURA (TIPO CADENA)
calificacion=0 #NOTA DE LA ASIGNATURA (TIPO FLOAT)
dicAsignatura={} #diccionario CON {"NOMBRE DE LA ASIGNATURA", CALIFICACION DE LA ASIGNATURA}
sumacalificaciones=0 #suma de las notas para hacer la media aritmetica

#PROGRAMA PRINCIPAL

system("cls")
while(asignatura != ""):
    asignatura = input("INTRODUCE EL NOMBRE DE LA ASIGNATURA (ENTER PARA FINALIZAR):")
    if asignatura != "":
        calificacion = float(input("TECLEA SU CALIFICACION: "))
        dicAsignatura[asignatura] = calificacion
    print("") #HAGO UN SALTO DE LINEA

for asignatura, calificacion in dicAsignatura.items():
    if calificacion >=5:
        print (f"LA ASIGNATURA {asignatura} ESTA APROBADA CON UN {calificacion}")
    sumacalificaciones =sumacalificaciones + calificacion

print(f"LA MEDIA ARITMETICA DE LAS CALIFICACIONES ES {sumacalificaciones/len(dicAsignatura)}")


